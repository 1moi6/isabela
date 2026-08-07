"""Contratos de dados trocados entre os agentes (Seções 4.3.3, 4.4.4 e 4.5.3 da dissertação).

Todos os agentes se comunicam por objetos estruturados, nunca por texto livre —
decisão de projeto que garante rastreabilidade (Seção 4.8).
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, Field, model_validator

from .especificacao import Especificacao, Garantia


def _para_texto(valor):
    """Aceita número onde o contrato pede texto.

    O Gerador escreve JSON, e em JSON `-2` é número: o LLM devolve `{"ponto": -2}`
    tanto quanto `{"ponto": "-2"}`. O núcleo simbólico trabalha com texto (tudo passa
    por `sympify`), então a conversão acontece aqui, na fronteira, e não em cada
    verificador. `bool` fica de fora: `True` não é expressão matemática.
    """
    if isinstance(valor, bool):
        return valor
    return str(valor) if isinstance(valor, (int, float)) else valor


TextoMatematico = Annotated[str, BeforeValidator(_para_texto)]


class Alternativa(BaseModel):
    """Alternativa de múltipla escolha, com o erro que o distrator representa."""

    texto: str
    correta: bool = False
    erro_representado: str | None = Field(
        default=None,
        description="Para distratores: qual erro sistemático do estudante esta alternativa captura",
    )


class ExpressaoVerificavel(BaseModel):
    """Formalização SymPy-friendly de **uma** afirmação da questão, preenchida pelo Gerador.

    É esta ponte que permite ao Verificador operar sem interpretar prosa
    (limite discutido na Seção 2.4.3 da dissertação).

    Uma questão pode ter mais de uma: quando articula dois temas, ou quando a
    habilidade cobra propriedades além do resultado (ver `Questao.verificaveis`).
    """

    tipo: str = Field(description="Roteia a estratégia de verificação: 'equacao', 'funcao', 'progressao'")
    expressao: TextoMatematico = Field(description="Expressão/equação em sintaxe SymPy, ex.: 'Eq(2*x**2 - 5*x + 3, 0)'")
    incognitas: list[str] = Field(default_factory=lambda: ["x"])
    resposta_esperada: TextoMatematico = Field(description="Gabarito em sintaxe SymPy, ex.: '[1, 3/2]'")
    parametros: dict[str, TextoMatematico] = Field(
        default_factory=dict,
        description="Dados extras por tipo, ex.: {'a1': '2', 'razao': '3', 'n': '10', 'consulta': 'termo_geral'}",
    )


class Questao(BaseModel):
    """Saída estruturada do Agente Gerador (Seção 4.3.3)."""

    enunciado: str
    resolucao: str = Field(description="Resolução passo a passo, em Markdown/LaTeX")
    gabarito: TextoMatematico = Field(description="Resposta final em linguagem natural")
    alternativas: list[Alternativa] | None = Field(
        default=None, description="Presente apenas em múltipla escolha (4 alternativas)"
    )
    verificaveis: list[ExpressaoVerificavel] = Field(
        default_factory=list,
        description="Uma entrada por afirmação verificável; vazia quando o Gerador julga a "
        "questão não formalizável. Uma questão que articula dois temas costuma ter duas.",
    )
    especificacao: Especificacao

    @model_validator(mode="before")
    @classmethod
    def _aceitar_verificavel_no_singular(cls, dados):
        """Aceita o campo `verificavel` das versões anteriores.

        As questões já gravadas no banco guardam `"verificavel": {...}` ou `null`.
        Sem esta ponte, reler o banco de quem já usou o sistema falharia --- e o
        LLM, que aprendeu o esquema antigo, também continua atendido.
        """
        if isinstance(dados, dict) and "verificavel" in dados and "verificaveis" not in dados:
            dados = dict(dados)
            unico = dados.pop("verificavel")
            dados["verificaveis"] = [] if unico is None else (
                unico if isinstance(unico, list) else [unico]
            )
        return dados


class Veredicto(str, Enum):
    """Saída do Verificador Simbólico (Seção 4.4.4)."""

    APROVADO = "aprovado"
    REJEITADO = "rejeitado"
    NAO_VERIFICAVEL = "nao_verificavel"
    APROVADO_RESSALVA_NUMERICA = "aprovado_ressalva_numerica"
    # Parte das afirmações foi conferida e o resto não era formalizável. Não é
    # rejeição: para o Orquestrador, segue ao Crítico como qualquer aprovação.
    APROVADO_PARCIAL = "aprovado_parcial"


_GARANTIA_POR_VEREDICTO = {
    Veredicto.APROVADO: Garantia.CONFERIDO,
    Veredicto.APROVADO_RESSALVA_NUMERICA: Garantia.CONFERIDO_EM_PARTE,
    Veredicto.APROVADO_PARCIAL: Garantia.CONFERIDO_EM_PARTE,
    Veredicto.NAO_VERIFICAVEL: Garantia.SEM_CONFERENCIA,
    Veredicto.REJEITADO: Garantia.SEM_CONFERENCIA,
}


def garantia_de(veredicto: Veredicto) -> Garantia:
    """Que conferência a questão **recebeu** de fato.

    Distinta da `verificabilidade_esperada` da habilidade, que diz o que ela
    admitiria. A diferença entre as duas é dado da avaliação empírica: em quais
    habilidades a garantia prometida não se realiza na prática?
    """
    return _GARANTIA_POR_VEREDICTO[veredicto]


class AfirmacaoVerificada(BaseModel):
    """Resultado de **uma** formalização, preservado dentro do veredicto agregado.

    Existe para instrumentação: com ela, o log do ciclo permite medir a taxa de
    `nao_verificavel` **por tipo**. Tipo com taxa alta denuncia descrição malfeita
    no prompt do Gerador, não habilidade difícil --- e o sintoma é invisível de
    outro modo, porque `nao_verificavel` não reprova a questão, só a deixa passar
    sem conferência.
    """

    tipo: str
    consulta: str | None = None
    veredicto: Veredicto


class ResultadoVerificacao(BaseModel):
    veredicto: Veredicto
    justificativa: str
    resultado_calculado: str | None = None
    afirmacoes: list[AfirmacaoVerificada] = Field(default_factory=list)


class NotaCriterio(BaseModel):
    """Parecer do Crítico para um critério da rubrica (Seção 3.4 da dissertação)."""

    criterio: str
    nota: int = Field(ge=1, le=5)
    comentario: str


class ParecerDidatico(BaseModel):
    """Saída estruturada do Agente Crítico Didático (Seção 4.5.3)."""

    notas: list[NotaCriterio]
    aprovado: bool
    sugestoes_revisao: str | None = None

    def nota_minima(self) -> int:
        return min(n.nota for n in self.notas) if self.notas else 0


class DecisaoProfessor(str, Enum):
    """Julgamento humano sobre a questão aprovada pelos agentes."""

    ACEITA = "aceita"
    ACEITA_COM_AJUSTE = "aceita_com_ajuste"
    RECUSADA = "recusada"


class AvaliacaoProfessor(BaseModel):
    """Avaliação do professor sobre uma questão já no banco.

    É o dado que separa "os agentes aprovaram" de "serve para a minha turma" —
    e a matéria-prima da avaliação empírica do Capítulo 6.
    """

    decisao: DecisaoProfessor
    comentario: str | None = Field(
        default=None, description="Por que aceitou, ajustou ou recusou — o dado qualitativo"
    )
    avaliada_em: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class RegistroIteracao(BaseModel):
    """Uma volta completa do ciclo gerar->verificar->criticar (memória de execução, Seção 4.6.3)."""

    numero: int
    questao: Questao
    verificacao: ResultadoVerificacao
    parecer: ParecerDidatico | None = Field(
        default=None, description="None quando a questão foi reprovada pelo Verificador antes do Crítico"
    )
    feedback_para_gerador: str | None = None


class ResultadoCiclo(BaseModel):
    """Resultado final do Orquestrador para uma especificação."""

    aprovada: bool
    questao_final: Questao | None
    iteracoes: list[RegistroIteracao]
    criada_em: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
