"""Especificação de entrada: o que o professor fornece ao sistema.

Corresponde à Seção 4.2 da dissertação. Cada campo é um parâmetro didático
que o Agente Gerador recebe como instrução explícita.

A ordem dos campos não é decorativa: a **habilidade vem antes do tema**. A
habilidade da BNCC é a unidade normativa do planejamento do professor, e é ela
que delimita quais temas podem ser pedidos --- não o contrário. Escolher o tema
primeiro permitia montar pedidos incoerentes que só um validador conseguia
barrar; escolhendo a habilidade primeiro, a incoerência deixa de existir por
construção.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field, field_validator, model_validator

_DADOS = Path(__file__).resolve().parents[2] / "dados" / "bncc_em_matematica.json"


class Tema(str, Enum):
    """Tópicos do recorte da dissertação (expansível)."""

    FUNCAO_AFIM = "funcao_afim"
    FUNCAO_QUADRATICA = "funcao_quadratica"
    FUNCAO_EXPONENCIAL = "funcao_exponencial"
    PROGRESSAO_ARITMETICA = "progressao_aritmetica"
    PROGRESSAO_GEOMETRICA = "progressao_geometrica"
    FUNCAO_LOGARITMICA = "funcao_logaritmica"
    FUNCAO_TRIGONOMETRICA = "funcao_trigonometrica"
    FUNCAO_POR_PARTES = "funcao_por_partes"


class RelacaoTemas(str, Enum):
    """Como os temas de uma habilidade se combinam numa questão (ver o catálogo).

    A distinção importa: em `EM13MAT507` ("identificar e associar sequências
    numéricas (PA) a funções afins de domínios discretos") a articulação entre
    os dois temas *é* a habilidade --- pedir só a PA não a realiza. Já em
    `EM13MAT302` o texto enumera o repertório coberto, e um problema modelado
    apenas por função afim realiza a habilidade tanto quanto um que combine as
    duas.
    """

    UNICA = "unica"
    ENUMERATIVA = "enumerativa"
    CONJUNTIVA = "conjuntiva"


class Garantia(str, Enum):
    """Grau de conferência automática — declarado por habilidade, obtido por questão.

    São dois níveis distintos e a diferença é essencial. `verificabilidade_esperada`
    diz o que a habilidade *admite* em princípio; `garantia_obtida` (em `modelos.py`)
    diz o que a questão *recebeu* de fato, porque o Gerador nem sempre consegue
    formalizar o que a habilidade permitiria. Confundir os dois faria "esta
    habilidade é verificável" ser lido como "esta questão foi verificada" --- o erro
    silencioso outra vez, agora nos metadados.

    Os rótulos são lidos por professores: ver ROTULO_GARANTIA na API.
    """

    CONFERIDO = "conferido"
    CONFERIDO_EM_PARTE = "conferido_em_parte"
    SEM_CONFERENCIA = "sem_conferencia"


class NivelBloom(str, Enum):
    """Processos cognitivos da Taxonomia de Bloom Revisada (Seção 3.2.1)."""

    LEMBRAR = "lembrar"
    ENTENDER = "entender"
    APLICAR = "aplicar"
    ANALISAR = "analisar"
    AVALIAR = "avaliar"
    CRIAR = "criar"


class Dificuldade(str, Enum):
    FACIL = "facil"
    MEDIA = "media"
    DIFICIL = "dificil"


class Natureza(str, Enum):
    """Questão teórica (manipulação/conceito) ou aplicada (contexto real)."""

    TEORICA = "teorica"
    APLICADA = "aplicada"


class Formato(str, Enum):
    DISCURSIVA = "discursiva"
    MULTIPLA_ESCOLHA = "multipla_escolha"  # 4 alternativas, conforme o projeto


def carregar_habilidades() -> dict[str, dict]:
    """Carrega o catálogo de habilidades BNCC do recorte (dados/bncc_em_matematica.json)."""
    with open(_DADOS, encoding="utf-8") as f:
        return {h["codigo"]: h for h in json.load(f)["habilidades"]}


class Especificacao(BaseModel):
    """Parâmetros do professor para a geração de uma questão."""

    habilidade_bncc: str = Field(description="Código EM13MATxxx, validado contra o catálogo")
    temas: list[Tema] = Field(
        min_length=1,
        description="Um ou mais temas da habilidade escolhida. Com mais de um, a questão deve "
        "articulá-los num único problema — não justapor itens independentes.",
    )
    nivel_bloom: NivelBloom
    dificuldade: Dificuldade
    natureza: Natureza
    formato: Formato
    contexto: str | None = Field(
        default=None, description="Contexto temático opcional (ex.: 'esportes', 'finanças pessoais')"
    )
    restricoes: str | None = Field(
        default=None, description="Restrições adicionais (ex.: 'apenas coeficientes inteiros')"
    )

    @model_validator(mode="before")
    @classmethod
    def _aceitar_tema_no_singular(cls, dados):
        """Aceita o campo `tema` das versões anteriores.

        As questões já gravadas no banco guardam a especificação serializada com
        `"tema": "funcao_afim"`. Sem esta ponte, `Questao.model_validate_json`
        falharia ao reler o banco de quem já usou o sistema --- o histórico
        inteiro do professor ficaria ilegível por uma mudança de nome de campo.
        """
        if isinstance(dados, dict) and "tema" in dados and "temas" not in dados:
            dados = dict(dados)
            tema = dados.pop("tema")
            dados["temas"] = tema if isinstance(tema, list) else [tema]
        return dados

    @field_validator("habilidade_bncc")
    @classmethod
    def _validar_codigo_bncc(cls, v: str) -> str:
        catalogo = carregar_habilidades()
        if v not in catalogo:
            conhecidos = ", ".join(sorted(catalogo))
            raise ValueError(f"Habilidade BNCC desconhecida: {v}. Disponíveis: {conhecidos}")
        return v

    @field_validator("temas")
    @classmethod
    def _sem_temas_repetidos(cls, v: list[Tema]) -> list[Tema]:
        if len(set(v)) != len(v):
            raise ValueError("Tema repetido na especificação.")
        return v

    @model_validator(mode="after")
    def _validar_temas_compativeis(self):
        """Os temas pedidos precisam pertencer à habilidade --- e, se ela for
        conjuntiva, precisam estar todos presentes.

        A interface deriva os temas da habilidade escolhida, então este validador
        protege quem chama a API diretamente. Sem ele, um pedido incoerente (PG
        com uma habilidade de PA) só seria descoberto pelo Crítico Didático ---
        depois de três iterações, cerca de cinco minutos e o custo de seis
        chamadas ao LLM.
        """
        habilidade = carregar_habilidades()[self.habilidade_bncc]
        da_habilidade = set(habilidade["temas"])
        pedidos = {t.value for t in self.temas}

        if fora := pedidos - da_habilidade:
            catalogo = carregar_habilidades()
            alvo = sorted(fora)[0]
            compativeis = ", ".join(c for c, h in catalogo.items() if alvo in h["temas"])
            raise ValueError(
                f"A habilidade {self.habilidade_bncc} não cobre o(s) tema(s) "
                f"{', '.join(sorted(fora))} (ela trata de: {', '.join(habilidade['temas'])}). "
                f"Para o tema '{alvo}', use: {compativeis}."
            )

        if habilidade["relacao_temas"] == RelacaoTemas.CONJUNTIVA and pedidos != da_habilidade:
            raise ValueError(
                f"A habilidade {self.habilidade_bncc} é a articulação entre "
                f"{' e '.join(habilidade['temas'])}: pedir apenas "
                f"{', '.join(sorted(pedidos))} a descaracteriza. Inclua todos os temas."
            )
        return self

    # ------------------------------------------------ leitura do catálogo
    def _habilidade(self) -> dict:
        return carregar_habilidades()[self.habilidade_bncc]

    def descricao_habilidade(self) -> str:
        return self._habilidade()["descricao"]

    def exigencias_habilidade(self) -> list[str]:
        """O que a questão precisa exibir para realizar a habilidade (Seção 4.2).

        Sem isto, a habilidade entrava no *prompt* como mais uma linha de texto e
        o único guardião do alinhamento curricular era o julgamento em prosa do
        Crítico. Estas exigências viram requisito para o Gerador e âncora para o
        Crítico.
        """
        return list(self._habilidade()["exigencias"])

    def relacao_temas(self) -> RelacaoTemas:
        return RelacaoTemas(self._habilidade()["relacao_temas"])

    def verificabilidade_esperada(self) -> Garantia:
        """Que garantia esta habilidade admite, em princípio (leitura nossa, não da BNCC).

        Não é o que a questão obteve: para isso, `garantia_de` em `modelos.py`.
        """
        return Garantia(self._habilidade()["verificabilidade_esperada"])

    def bloom_sugerido(self) -> list[str]:
        """Níveis cognitivos compatíveis com os verbos da habilidade."""
        return list(self._habilidade()["bloom_sugerido"])

    def bloom_diverge(self) -> bool:
        """O nível pedido destoa dos verbos da habilidade?

        Não é erro --- o professor pode ter boas razões para pedir um nível fora
        do que o verbo sugere. É informação: a interface avisa e o registro do
        ciclo guarda a divergência, que é dado da avaliação empírica.
        """
        return self.nivel_bloom.value not in self.bloom_sugerido()
