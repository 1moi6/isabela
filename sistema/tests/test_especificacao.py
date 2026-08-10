import pytest
from pydantic import ValidationError

from questoes.especificacao import carregar_habilidades

from questoes.especificacao import (
    Dificuldade,
    Especificacao,
    Formato,
    Garantia,
    Natureza,
    NivelBloom,
    Tema,
    carregar_habilidades,
)


def _spec(**kw):
    base = dict(
        tema=Tema.FUNCAO_QUADRATICA,
        habilidade_bncc="EM13MAT302",
        nivel_bloom=NivelBloom.APLICAR,
        dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.APLICADA,
        formato=Formato.MULTIPLA_ESCOLHA,
    )
    base.update(kw)
    return Especificacao(**base)


def test_especificacao_valida():
    spec = _spec()
    assert spec.descricao_habilidade().startswith("Resolver e elaborar problemas")


def test_codigo_bncc_invalido_rejeitado():
    with pytest.raises(ValidationError, match="Habilidade BNCC desconhecida"):
        _spec(habilidade_bncc="EM13MAT999")


def test_catalogo_tem_recorte_completo():
    catalogo = carregar_habilidades()
    assert {"EM13MAT302", "EM13MAT507", "EM13MAT508"} <= set(catalogo)


def test_unidade_da_bncc_esta_completa():
    """A BNCC agrupa estas sete habilidades numa unidade (seção 5.2.1.1).

    O catálogo trazia só quatro delas: faltavam 501, 502 e 503 --- lacuna
    dentro do próprio recorte, não do recorte para fora. Se alguém remover
    uma, a unidade citada no texto deixa de corresponder ao catálogo.
    """
    catalogo = carregar_habilidades()
    unidade = {
        c for c, h in catalogo.items() if h["unidade"] == "funcoes_polinomiais_1_2_graus"
    }
    assert unidade == {
        "EM13MAT501",
        "EM13MAT401",
        "EM13MAT507",
        "EM13MAT502",
        "EM13MAT402",
        "EM13MAT503",
        "EM13MAT302",
    }


def test_tema_incompativel_com_a_habilidade_e_recusado():
    """Pedido incoerente falha em milissegundos, não depois de três iterações.

    PG com uma habilidade de PA passava pela validação e só era barrado pelo
    Crítico Didático — ao custo de ~5 minutos e seis chamadas ao LLM.
    """
    with pytest.raises(ValidationError) as erro:
        Especificacao(
            tema=Tema.PROGRESSAO_GEOMETRICA, habilidade_bncc="EM13MAT507",
            nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
            natureza=Natureza.TEORICA, formato=Formato.DISCURSIVA,
        )
    mensagem = str(erro.value)
    assert "EM13MAT507" in mensagem
    assert "EM13MAT508" in mensagem  # sugere a habilidade certa para o tema


def test_todo_tema_tem_ao_menos_uma_habilidade():
    """Senão a validação nova tornaria um tema inteiro inalcançável."""
    habilidades = carregar_habilidades()
    for tema in Tema:
        assert any(tema.value in h["temas"] for h in habilidades.values()), tema


def _spec_multi(**kw):
    base = {
        "habilidade_bncc": "EM13MAT302",
        "temas": [Tema.FUNCAO_AFIM, Tema.FUNCAO_QUADRATICA],
        "nivel_bloom": NivelBloom.APLICAR,
        "dificuldade": Dificuldade.MEDIA,
        "natureza": Natureza.APLICADA,
        "formato": Formato.DISCURSIVA,
    }
    base.update(kw)
    return Especificacao(**base)


def test_habilidade_enumerativa_aceita_um_ou_varios_temas():
    """EM13MAT302 enumera o repertório coberto: combinar é opção, não obrigação."""
    assert len(_spec_multi().temas) == 2
    assert len(_spec_multi(temas=[Tema.FUNCAO_AFIM]).temas) == 1


def test_habilidade_conjuntiva_exige_todos_os_temas():
    """EM13MAT507 *é* a associação entre PA e função afim: pedir só a PA não a realiza."""
    with pytest.raises(ValidationError, match="descaracteriza"):
        _spec_multi(habilidade_bncc="EM13MAT507", temas=[Tema.PROGRESSAO_ARITMETICA])

    completa = _spec_multi(
        habilidade_bncc="EM13MAT507",
        temas=[Tema.PROGRESSAO_ARITMETICA, Tema.FUNCAO_AFIM],
    )
    assert len(completa.temas) == 2


def test_tema_no_singular_ainda_e_aceito():
    """As questões já gravadas no banco guardam `tema`, não `temas`.

    Sem esta ponte, uma mudança de nome de campo tornaria ilegível o histórico
    inteiro de quem já usou o sistema.
    """
    antiga = Especificacao(
        tema="funcao_quadratica", habilidade_bncc="EM13MAT302",
        nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.TEORICA, formato=Formato.DISCURSIVA,
    )
    assert antiga.temas == [Tema.FUNCAO_QUADRATICA]


def test_tema_repetido_e_recusado():
    with pytest.raises(ValidationError, match="repetido"):
        _spec_multi(temas=[Tema.FUNCAO_AFIM, Tema.FUNCAO_AFIM])


def test_toda_habilidade_tem_exigencias_e_bloom_sugerido():
    """São o que torna a habilidade uma restrição de geração, não um rótulo."""
    for codigo, h in carregar_habilidades().items():
        assert h["exigencias"], codigo
        assert h["bloom_sugerido"], codigo
        assert h["relacao_temas"] in {"unica", "enumerativa", "conjuntiva"}, codigo
        # 'unica' com dois temas (ou o contrário) faria a interface travar ou
        # liberar a escolha errada.
        assert (h["relacao_temas"] == "unica") == (len(h["temas"]) == 1), codigo


def test_bloom_divergente_e_sinalizado_sem_ser_barrado():
    """Pedir um nível fora dos verbos da habilidade é permitido — e registrado."""
    assert _spec_multi(nivel_bloom=NivelBloom.LEMBRAR).bloom_diverge()
    assert not _spec_multi(nivel_bloom=NivelBloom.APLICAR).bloom_diverge()


def test_toda_habilidade_declara_verificabilidade_e_razao():
    """Categoria sem razão registrada seria classificação arbitrária."""
    for codigo, h in carregar_habilidades().items():
        assert h["verificabilidade_esperada"] in {
            "conferido", "conferido_em_parte", "sem_conferencia"
        }, codigo
        assert h["grupo_verificabilidade"] in {1, 2, 3, 4}, codigo
        assert h["razao_verificabilidade"], codigo


def test_conversao_de_registro_nao_promete_conferencia_plena():
    """401 e 402 pedem converter álgebra em gráfico — nenhum CAS decide isso.

    Estavam no catálogo aparentando a mesma garantia das demais; agora dizem
    que só parte da questão é conferida.
    """
    catalogo = carregar_habilidades()
    for codigo in ("EM13MAT401", "EM13MAT402"):
        assert catalogo[codigo]["verificabilidade_esperada"] == "conferido_em_parte"
        assert catalogo[codigo]["grupo_verificabilidade"] == 3
    assert _spec_multi(habilidade_bncc="EM13MAT402", temas=[Tema.FUNCAO_QUADRATICA]) \
        .verificabilidade_esperada() == Garantia.CONFERIDO_EM_PARTE


def test_habilidades_de_funcoes_log_e_trigonometricas_entraram():
    """Fase 2a/2b: a unidade de funções deixa de parar na exponencial."""
    catalogo = carregar_habilidades()
    assert {"EM13MAT305", "EM13MAT306", "EM13MAT403", "EM13MAT404", "EM13MAT405"} <= set(catalogo)
    # 403 compara exponencial COM logarítmica: a articulação é a habilidade
    assert catalogo["EM13MAT403"]["relacao_temas"] == "conjuntiva"
    with pytest.raises(ValidationError, match="descaracteriza"):
        _spec_multi(habilidade_bncc="EM13MAT403", temas=[Tema.FUNCAO_EXPONENCIAL])


def test_comparacao_entre_representacoes_declara_conferencia_parcial():
    """403 e 404 pedem comparar representações — nenhum CAS decide isso."""
    catalogo = carregar_habilidades()
    for codigo in ("EM13MAT403", "EM13MAT404"):
        assert catalogo[codigo]["verificabilidade_esperada"] == "conferido_em_parte"
        assert catalogo[codigo]["grupo_verificabilidade"] == 3


def test_catalogo_de_contextos_cobre_todos_os_temas():
    """Tema sem contexto sugerido devolveria o professor ao padrão do modelo.

    No acervo de 8 de agosto, 7 das 9 questões de função afim eram tarifa fixa
    mais valor por unidade e todas as de PG eram cultura de bactérias — o
    Gerador volta ao contexto mais provável do tema quando ninguém indica outro.
    """
    from questoes.especificacao import carregar_contextos, contextos_para

    contextos = carregar_contextos()
    assert len(contextos) >= 20
    for tema in Tema:
        assert len(contextos_para(tema.value)) >= 5, tema

    campos = {c["campo"] for c in contextos}
    # os campos que faltavam por inteiro no acervo
    assert {"ecologia", "clima", "demografia"} <= campos


def test_contexto_declarado_chega_ao_gerador():
    from questoes.agentes.gerador import Gerador

    spec = _spec_multi(contexto="Desmatamento e recuperação de área florestal")
    assert "Desmatamento" in Gerador._montar_pedido(spec, None)


def test_sorteio_de_contexto_nao_repete_dentro_da_habilidade():
    """Sorteio COM reposição pareceria natural e seria pior.

    Com 5 a 9 contextos por tema, a chance de repetir dentro das seis questões
    de uma habilidade iria de 89% a 100% — justamente o que o catálogo veio
    resolver. Embaralhar dá ordem imprevisível e nenhuma repetição.
    """
    import random
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from gerar_acervo import sorteio_de_contexto

    sorteio, filas = random.Random(1), {}
    escolhidos = [
        sorteio_de_contexto("EM13MAT304", "funcao_exponencial", i, sorteio, filas)
        for i in range(6)
    ]
    principais = [c.split(" + ")[0] for c in escolhidos]
    assert len(set(principais)) == 6, principais


def test_habilidades_do_mesmo_tema_nao_compartilham_a_fila():
    """302, 401 e 501 são todas de função afim: fila comum daria a mesma sequência."""
    import random
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from gerar_acervo import sorteio_de_contexto

    sorteio, filas = random.Random(1), {}
    a = [sorteio_de_contexto("EM13MAT302", "funcao_afim", i, sorteio, filas) for i in range(6)]
    b = [sorteio_de_contexto("EM13MAT401", "funcao_afim", i, sorteio, filas) for i in range(6)]
    assert a != b
