"""Testes do nível "básico" e da blindagem do plano do acervo contra ele.

O nível veio do painel docente: quatro dos cinco professores julgaram as
questões mais difíceis do que a especificação declarava. O risco de acrescentá-lo
é silencioso: o plano do acervo percorria o enum inteiro, e um nível a mais
mudaria as 90 especificações que a comparação entre modelos exige idênticas.
"""

import gerar_acervo
from questoes.agentes import Gerador
from questoes.especificacao import (
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, Tema,
)

from test_api import cliente  # noqa: F401  (fixture)


def test_basico_e_o_primeiro_nivel_oferecido_ao_professor(cliente):  # noqa: F811
    niveis = cliente.get("/api/opcoes").json()["dificuldades"]
    assert [n["valor"] for n in niveis] == ["basico", "facil", "media", "dificil"]
    assert niveis[0]["rotulo"] == "Básico"


def test_gerador_recebe_a_descricao_do_basico_e_nao_so_o_nome():
    """Sem a descrição, "básico" seria só um sinônimo de "fácil" para o modelo."""
    spec = Especificacao(
        tema=Tema.FUNCAO_AFIM, habilidade_bncc="EM13MAT302",
        nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.BASICO,
        natureza=Natureza.APLICADA, formato=Formato.DISCURSIVA,
    )
    pedido = Gerador._montar_pedido(spec, None)
    assert "básico — um passo só" in pedido
    assert "sem itens encadeados" in pedido


def test_plano_do_acervo_continua_com_as_90_especificacoes_de_tres_niveis():
    plano = gerar_acervo.plano()
    assert len(plano) == 90
    assert {e["dificuldade"] for e in plano} == {
        Dificuldade.FACIL, Dificuldade.MEDIA, Dificuldade.DIFICIL,
    }
