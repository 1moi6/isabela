"""Depósito das questões numa pasta sincronizada com a nuvem.

O professor aponta o aplicativo para uma pasta que o Google Drive para Desktop
(ou OneDrive, ou qualquer cliente equivalente) já sincroniza. A cada questão
salva, gravamos três coisas nessa pasta:

  - um `.md` legível, para ler e revisar fora do aplicativo;
  - um `.json` com o ciclo completo, para reanálise posterior;
  - um `_indice.csv` regravado por inteiro, com uma linha por questão.

Não há autenticação nem chamada de rede aqui — quem sincroniza é o cliente da
nuvem. É o caminho mais robusto: nada quebra quando um token expira.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from .modelos import AvaliacaoProfessor, Questao, ResultadoCiclo, garantia_de

INDICE = "_indice.csv"

COLUNAS_INDICE = [
    "id", "criada_em", "temas", "habilidade_bncc", "nivel_bloom", "dificuldade",
    "natureza", "formato", "veredicto_verificacao", "garantia", "nota_minima_critico",
    "iteracoes", "decisao_professor", "comentario_professor", "arquivo",
]


class PastaSincronizada:
    """Escreve as questões numa pasta local que a nuvem replica."""

    def __init__(self, pasta: Path | str):
        self.pasta = Path(pasta).expanduser()

    @property
    def configurada(self) -> bool:
        return str(self.pasta) not in ("", ".")

    def verificar(self) -> None:
        """Falha cedo e com mensagem útil se a pasta não estiver acessível."""
        if not self.configurada:
            raise ValueError("Nenhuma pasta de sincronização configurada.")
        if not self.pasta.is_dir():
            raise FileNotFoundError(
                f"A pasta '{self.pasta}' não existe. Verifique se o Google Drive "
                "está instalado e sincronizando, e confira o caminho nas configurações."
            )

    def exportar(
        self,
        questao_id: int,
        resultado: ResultadoCiclo,
        avaliacao: AvaliacaoProfessor | None = None,
    ) -> Path:
        """Grava o `.md` e o `.json` de uma questão. Regravar sobrescreve."""
        self.verificar()
        q = resultado.questao_final
        if q is None:
            raise ValueError("Só ciclos aprovados são exportados.")
        base = self.pasta / self._nome(questao_id, q)
        base.with_suffix(".md").write_text(
            _markdown(questao_id, resultado, avaliacao), encoding="utf-8"
        )
        base.with_suffix(".json").write_text(
            json.dumps(resultado.model_dump(mode="json"), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return base.with_suffix(".md")

    def regravar_indice(self, registros: list[dict]) -> Path:
        """Reescreve o índice inteiro a partir do banco.

        Regravar tudo (em vez de acrescentar uma linha) mantém o índice correto
        depois de uma avaliação do professor, que muda uma linha antiga.
        """
        self.verificar()
        caminho = self.pasta / INDICE
        # utf-8-sig: sem o BOM, o Excel em português abre os acentos errados.
        with open(caminho, "w", encoding="utf-8-sig", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=COLUNAS_INDICE)
            escritor.writeheader()
            for reg in registros:
                linha = {c: reg.get(c, "") for c in COLUNAS_INDICE}
                # `temas` chega como lista; o CSV é para o professor ler no Excel.
                linha["temas"] = "; ".join(linha["temas"] or [])
                linha["arquivo"] = self._nome(reg["id"], reg["questao"]) + ".md"
                escritor.writerow(linha)
        return caminho

    def _nome(self, questao_id: int, questao: Questao) -> str:
        spec = questao.especificacao
        return f"questao-{questao_id:04d}_{spec.temas[0].value}_{spec.dificuldade.value}"


def _markdown(
    questao_id: int, resultado: ResultadoCiclo, avaliacao: AvaliacaoProfessor | None = None
) -> str:
    """Versão legível da questão, com a evidência de verificação junto."""
    q = resultado.questao_final
    spec = q.especificacao
    ultima = resultado.iteracoes[-1]

    linhas = [
        f"# Questão #{questao_id:04d}",
        "",
        f"- **Temas:** {', '.join(t.value for t in spec.temas)}",
        f"- **Habilidade BNCC:** {spec.habilidade_bncc}",
        f"- **Nível cognitivo (Bloom):** {spec.nivel_bloom.value}",
        f"- **Dificuldade:** {spec.dificuldade.value}",
        f"- **Natureza:** {spec.natureza.value}",
        f"- **Formato:** {spec.formato.value}",
        f"- **Gerada em:** {resultado.criada_em}",
        f"- **Iterações até a aprovação:** {len(resultado.iteracoes)}",
        "",
        "## Enunciado",
        "",
        q.enunciado,
        "",
    ]

    if q.alternativas:
        linhas.append("## Alternativas")
        linhas.append("")
        for letra, alt in zip("abcd", q.alternativas):
            marca = "  ← correta" if alt.correta else ""
            linhas.append(f"- ({letra}) {alt.texto}{marca}")
            if alt.erro_representado and not alt.correta:
                linhas.append(f"  - *erro representado:* {alt.erro_representado}")
        linhas.append("")

    linhas += [
        "## Gabarito", "", q.gabarito, "",
        "## Resolução", "", q.resolucao, "",
        "## Verificação simbólica", "",
        f"- **Veredicto:** {ultima.verificacao.veredicto.value}",
        f"- **Garantia:** {garantia_de(ultima.verificacao.veredicto).value}",
        f"- **Justificativa:** {ultima.verificacao.justificativa}",
    ]
    if ultima.verificacao.resultado_calculado:
        linhas.append(f"- **Resultado recalculado pelo SymPy:** `{ultima.verificacao.resultado_calculado}`")
    linhas.append("")

    if ultima.parecer:
        linhas += ["## Parecer didático", ""]
        for nota in ultima.parecer.notas:
            linhas.append(f"- **{nota.criterio}:** {nota.nota}/5 — {nota.comentario}")
        linhas.append("")

    if avaliacao is not None:
        linhas += ["## Avaliação do professor", "",
                   f"- **Decisão:** {avaliacao.decisao.value}"]
        if avaliacao.comentario:
            linhas.append(f"- **Comentário:** {avaliacao.comentario}")
        linhas.append("")

    return "\n".join(linhas)
