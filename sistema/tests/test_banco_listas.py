import threading

import pytest

from questoes.banco import BancoQuestoes
from questoes.especificacao import (
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, Tema,
)
from questoes.listas import para_latex, para_markdown
from questoes.modelos import (
    Alternativa, Questao, RegistroIteracao, ResultadoCiclo,
    ResultadoVerificacao, Veredicto,
)


def _resultado(tema=Tema.FUNCAO_QUADRATICA, dificuldade=Dificuldade.MEDIA):
    spec = Especificacao(
        tema=tema, habilidade_bncc="EM13MAT302", nivel_bloom=NivelBloom.APLICAR,
        dificuldade=dificuldade, natureza=Natureza.TEORICA, formato=Formato.MULTIPLA_ESCOLHA,
    )
    q = Questao(
        enunciado="Determine as raízes de x² - 5x + 6 = 0.",
        resolucao="Fatorando: $(x-2)(x-3)=0$.",
        gabarito="x = 2 ou x = 3",
        alternativas=[
            Alternativa(texto="2 e 3", correta=True),
            Alternativa(texto="-2 e -3", erro_representado="troca de sinal"),
            Alternativa(texto="1 e 6", erro_representado="fatoração do termo independente"),
            Alternativa(texto="5 e 6", erro_representado="uso direto dos coeficientes"),
        ],
        verificavel=None,
        especificacao=spec,
    )
    it = RegistroIteracao(
        numero=1, questao=q,
        verificacao=ResultadoVerificacao(veredicto=Veredicto.APROVADO, justificativa="ok"),
    )
    return ResultadoCiclo(aprovada=True, questao_final=q, iteracoes=[it])


def test_salvar_e_buscar(tmp_path):
    banco = BancoQuestoes(tmp_path / "t.db")
    banco.salvar(_resultado())
    banco.salvar(_resultado(dificuldade=Dificuldade.FACIL))
    assert banco.total() == 2
    achadas = banco.buscar(dificuldade="facil")
    assert len(achadas) == 1


def test_banco_atravessa_threads(tmp_path):
    """A interface Streamlit reaproveita o banco entre threads diferentes."""
    banco = BancoQuestoes(tmp_path / "t.db")
    banco.salvar(_resultado())

    erros = []

    def em_outra_thread():
        try:
            banco.salvar(_resultado(dificuldade=Dificuldade.FACIL))
            banco.buscar()
            banco.total()
        except Exception as exc:  # pragma: no cover - só falha se a conexão prender
            erros.append(exc)

    t = threading.Thread(target=em_outra_thread)
    t.start()
    t.join()

    assert not erros, erros
    assert banco.total() == 2


def test_ciclo_reprovado_nao_entra_no_banco(tmp_path):
    banco = BancoQuestoes(tmp_path / "t.db")
    ruim = _resultado()
    ruim.aprovada, ruim.questao_final = False, None
    with pytest.raises(ValueError):
        banco.salvar(ruim)


def test_lista_markdown_aluno_sem_gabarito():
    q = _resultado().questao_final
    md = para_markdown("Lista 1", [q], com_gabarito=False)
    assert "Questão 1." in md and "- (a)" in md  # enunciado e alternativas presentes
    assert "Gabarito" not in md and "Fatorando" not in md  # sem resolução na versão do aluno


def test_lista_markdown_professor_com_resolucao():
    q = _resultado().questao_final
    md = para_markdown("Lista 1", [q], com_gabarito=True)
    assert "Gabarito e resoluções" in md and "Fatorando" in md


def test_lista_latex_compilavel_na_estrutura():
    q = _resultado().questao_final
    tex = para_latex("Lista 1", [q, q], com_gabarito=True)
    assert tex.count(r"\item") >= 2
    assert tex.strip().endswith(r"\end{document}")
    assert r"\begin{document}" in tex
