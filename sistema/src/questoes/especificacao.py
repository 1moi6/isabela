"""Especificação de entrada: o que o professor fornece ao sistema.

Corresponde à Seção 4.2 da dissertação. Cada campo é um parâmetro didático
que o Agente Gerador recebe como instrução explícita.
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

    tema: Tema
    habilidade_bncc: str = Field(description="Código EM13MATxxx, validado contra o catálogo")
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

    @field_validator("habilidade_bncc")
    @classmethod
    def _validar_codigo_bncc(cls, v: str) -> str:
        catalogo = carregar_habilidades()
        if v not in catalogo:
            conhecidos = ", ".join(sorted(catalogo))
            raise ValueError(f"Habilidade BNCC desconhecida: {v}. Disponíveis: {conhecidos}")
        return v

    @model_validator(mode="after")
    def _validar_tema_compativel(self):
        """O tema pedido precisa ser um dos temas da habilidade escolhida.

        Sem esta checagem, um pedido incoerente (PG com uma habilidade de PA)
        só é descoberto pelo Crítico Didático --- depois de três iterações,
        cerca de cinco minutos e o custo de seis chamadas ao LLM. A interface
        já filtra as habilidades pelo tema; isto protege quem chama a API
        diretamente.
        """
        habilidade = carregar_habilidades()[self.habilidade_bncc]
        if self.tema.value not in habilidade["temas"]:
            compativeis = ", ".join(
                c for c, h in carregar_habilidades().items() if self.tema.value in h["temas"]
            )
            raise ValueError(
                f"A habilidade {self.habilidade_bncc} não cobre o tema '{self.tema.value}' "
                f"(ela trata de: {', '.join(habilidade['temas'])}). "
                f"Para este tema, use: {compativeis}."
            )
        return self

    def descricao_habilidade(self) -> str:
        return carregar_habilidades()[self.habilidade_bncc]["descricao"]
