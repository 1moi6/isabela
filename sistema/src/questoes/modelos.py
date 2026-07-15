"""Contratos de dados trocados entre os agentes (Seções 4.3.3, 4.4.4 e 4.5.3 da dissertação).

Todos os agentes se comunicam por objetos estruturados, nunca por texto livre —
decisão de projeto que garante rastreabilidade (Seção 4.8).
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field

from .especificacao import Especificacao


class Alternativa(BaseModel):
    """Alternativa de múltipla escolha, com o erro que o distrator representa."""

    texto: str
    correta: bool = False
    erro_representado: str | None = Field(
        default=None,
        description="Para distratores: qual erro sistemático do estudante esta alternativa captura",
    )


class ExpressaoVerificavel(BaseModel):
    """Formalização SymPy-friendly do problema, preenchida pelo Gerador.

    É esta ponte que permite ao Verificador operar sem interpretar prosa
    (limite discutido na Seção 2.4.3 da dissertação).
    """

    tipo: str = Field(description="Roteia a estratégia de verificação: 'equacao', 'funcao', 'progressao'")
    expressao: str = Field(description="Expressão/equação em sintaxe SymPy, ex.: 'Eq(2*x**2 - 5*x + 3, 0)'")
    incognitas: list[str] = Field(default_factory=lambda: ["x"])
    resposta_esperada: str = Field(description="Gabarito em sintaxe SymPy, ex.: '[1, 3/2]'")
    parametros: dict[str, str] = Field(
        default_factory=dict,
        description="Dados extras por tipo, ex.: {'a1': '2', 'razao': '3', 'n': '10', 'consulta': 'termo_geral'}",
    )


class Questao(BaseModel):
    """Saída estruturada do Agente Gerador (Seção 4.3.3)."""

    enunciado: str
    resolucao: str = Field(description="Resolução passo a passo, em Markdown/LaTeX")
    gabarito: str = Field(description="Resposta final em linguagem natural")
    alternativas: list[Alternativa] | None = Field(
        default=None, description="Presente apenas em múltipla escolha (4 alternativas)"
    )
    verificavel: ExpressaoVerificavel | None = Field(
        default=None, description="None quando o Gerador julga a questão não formalizável"
    )
    especificacao: Especificacao


class Veredicto(str, Enum):
    """Saída do Verificador Simbólico (Seção 4.4.4)."""

    APROVADO = "aprovado"
    REJEITADO = "rejeitado"
    NAO_VERIFICAVEL = "nao_verificavel"
    APROVADO_RESSALVA_NUMERICA = "aprovado_ressalva_numerica"


class ResultadoVerificacao(BaseModel):
    veredicto: Veredicto
    justificativa: str
    resultado_calculado: str | None = None


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
