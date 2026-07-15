"""Agente Verificador Simbólico (Seção 4.4 da dissertação).

Camada fina sobre o pacote `verificacao`: resolve a questão de forma
independente via SymPy e compara com o gabarito do Gerador. Nenhum LLM.
"""

from __future__ import annotations

from ..modelos import Questao, ResultadoVerificacao, Veredicto
from ..verificacao import verificar


class VerificadorSimbolico:
    def verificar(self, questao: Questao) -> ResultadoVerificacao:
        if questao.verificavel is None:
            return ResultadoVerificacao(
                veredicto=Veredicto.NAO_VERIFICAVEL,
                justificativa="O Gerador não forneceu formalização verificável. "
                "Validação matemática fica a cargo do professor.",
            )
        return verificar(questao.verificavel)
