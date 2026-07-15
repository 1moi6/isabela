"""Estratégias de verificação simbólica por tipo de questão (Seção 4.4.2 da dissertação).

Cada módulo implementa `verificar(ExpressaoVerificavel) -> ResultadoVerificacao`
usando exclusivamente SymPy — nenhum LLM participa desta camada.
"""

from ..modelos import ExpressaoVerificavel, ResultadoVerificacao, Veredicto
from . import equacoes, funcoes, numerica, progressoes

_ESTRATEGIAS = {
    "equacao": equacoes.verificar,
    "funcao": funcoes.verificar,
    "progressao": progressoes.verificar,
}


def verificar(ev: ExpressaoVerificavel) -> ResultadoVerificacao:
    """Roteia a expressão verificável para a estratégia do seu tipo.

    Tipos desconhecidos retornam NAO_VERIFICAVEL (nunca exceção): a decisão
    sobre o que fazer com a questão é do Orquestrador, não desta camada.
    """
    estrategia = _ESTRATEGIAS.get(ev.tipo)
    if estrategia is None:
        return ResultadoVerificacao(
            veredicto=Veredicto.NAO_VERIFICAVEL,
            justificativa=f"Tipo de verificação desconhecido: '{ev.tipo}'. "
            f"Tipos suportados: {sorted(_ESTRATEGIAS)}.",
        )
    try:
        return estrategia(ev)
    except Exception as exc:  # expressão malformada vinda do LLM não pode derrubar o ciclo
        return ResultadoVerificacao(
            veredicto=Veredicto.NAO_VERIFICAVEL,
            justificativa=f"Falha ao processar a expressão ({type(exc).__name__}: {exc}). "
            "Revisar a formalização produzida pelo Gerador.",
        )
