"""Agente Verificador Simbólico (Seção 4.4 da dissertação).

Camada fina sobre o pacote `verificacao`: resolve a questão de forma
independente via SymPy e compara com o gabarito do Gerador. Nenhum LLM.

Uma questão pode trazer várias afirmações verificáveis --- uma por tema, quando
articula dois, ou uma por propriedade que a habilidade cobra. Este módulo
verifica cada uma e agrega os vereditos num só, que é o que o Orquestrador
recebe: a política de decisão continua lá, e continua vendo um veredicto único.
"""

from __future__ import annotations

from ..modelos import Questao, ResultadoVerificacao, Veredicto
from ..verificacao import verificar


class VerificadorSimbolico:
    def verificar(self, questao: Questao) -> ResultadoVerificacao:
        if not questao.verificaveis:
            return ResultadoVerificacao(
                veredicto=Veredicto.NAO_VERIFICAVEL,
                justificativa="O Gerador não forneceu formalização verificável. "
                "Validação matemática fica a cargo do professor.",
            )

        resultados = [verificar(ev) for ev in questao.verificaveis]
        if len(resultados) == 1:
            return resultados[0]
        return _agregar(resultados)


def _agregar(resultados: list[ResultadoVerificacao]) -> ResultadoVerificacao:
    """Conjunção: a questão vale o que vale a sua afirmação mais fraca.

    Uma reprovação basta para reprovar --- não adianta o termo geral da PA estar
    certo se a função afim associada está errada. E uma afirmação não
    formalizável rebaixa o conjunto a parcial, em vez de deixá-lo passar como se
    tudo tivesse sido conferido.
    """
    por_veredicto = {r.veredicto for r in resultados}
    detalhe = " | ".join(
        f"({i}) {r.veredicto.value}: {r.justificativa}" for i, r in enumerate(resultados, 1)
    )
    calculado = " | ".join(r.resultado_calculado or "—" for r in resultados)

    if Veredicto.REJEITADO in por_veredicto:
        reprovadas = sum(r.veredicto == Veredicto.REJEITADO for r in resultados)
        return ResultadoVerificacao(
            veredicto=Veredicto.REJEITADO,
            justificativa=f"{reprovadas} de {len(resultados)} afirmações reprovadas. {detalhe}",
            resultado_calculado=calculado,
        )

    if Veredicto.NAO_VERIFICAVEL in por_veredicto:
        conferidas = sum(r.veredicto != Veredicto.NAO_VERIFICAVEL for r in resultados)
        if conferidas == 0:
            return ResultadoVerificacao(
                veredicto=Veredicto.NAO_VERIFICAVEL,
                justificativa=f"Nenhuma das {len(resultados)} afirmações pôde ser "
                f"verificada. {detalhe}",
            )
        return ResultadoVerificacao(
            veredicto=Veredicto.APROVADO_PARCIAL,
            justificativa=f"{conferidas} de {len(resultados)} afirmações conferidas; "
            f"o restante não é formalizável. {detalhe}",
            resultado_calculado=calculado,
        )

    if Veredicto.APROVADO_RESSALVA_NUMERICA in por_veredicto:
        return ResultadoVerificacao(
            veredicto=Veredicto.APROVADO_RESSALVA_NUMERICA,
            justificativa=f"Todas as {len(resultados)} afirmações conferidas, alguma por "
            f"amostragem numérica. {detalhe}",
            resultado_calculado=calculado,
        )

    return ResultadoVerificacao(
        veredicto=Veredicto.APROVADO,
        justificativa=f"Todas as {len(resultados)} afirmações conferidas. {detalhe}",
        resultado_calculado=calculado,
    )
