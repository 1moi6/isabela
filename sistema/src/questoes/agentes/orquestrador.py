"""Agente Orquestrador (Seção 4.6 da dissertação).

Coordena o ciclo gerar -> verificar -> criticar -> decidir. Não gera, não
verifica, não avalia: decide. Política de decisão explícita:

  - Verificador REJEITADO ................ revisão (não passa pelo Crítico)
  - Verificador NAO_VERIFICAVEL .......... segue ao Crítico; aprovação final
                                           fica marcada para revisão prioritária
                                           do professor (a questão não é descartada)
  - Crítico reprovado .................... revisão com as sugestões do parecer
  - Ambos aprovados ...................... questão aprovada
  - 3 iterações sem aprovação ............ descarte

Toda iteração é registrada (memória de execução, Seção 4.6.3) e logada em
JSONL para rastreabilidade.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..especificacao import Especificacao
from ..modelos import RegistroIteracao, ResultadoCiclo, Veredicto
from .critico import CriticoDidatico
from .gerador import Gerador
from .verificador import VerificadorSimbolico

MAX_ITERACOES = 3


class Orquestrador:
    def __init__(
        self,
        gerador: Gerador,
        verificador: VerificadorSimbolico,
        critico: CriticoDidatico,
        max_iteracoes: int = MAX_ITERACOES,
        log_dir: Path | None = None,
    ):
        self._gerador = gerador
        self._verificador = verificador
        self._critico = critico
        self._max = max_iteracoes
        self._log_dir = log_dir

    def produzir(self, spec: Especificacao) -> ResultadoCiclo:
        iteracoes: list[RegistroIteracao] = []
        feedback: str | None = None

        for numero in range(1, self._max + 1):
            questao = self._gerador.gerar(spec, feedback=feedback)
            verificacao = self._verificador.verificar(questao)

            if verificacao.veredicto == Veredicto.REJEITADO:
                feedback = (
                    "O verificador simbólico REPROVOU o gabarito. "
                    f"Motivo: {verificacao.justificativa} "
                    f"Resultado calculado independentemente: {verificacao.resultado_calculado}. "
                    "Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes)."
                )
                iteracoes.append(
                    RegistroIteracao(
                        numero=numero, questao=questao, verificacao=verificacao,
                        parecer=None, feedback_para_gerador=feedback,
                    )
                )
                continue

            parecer = self._critico.avaliar(questao)
            if not parecer.aprovado:
                feedback = (
                    "O avaliador didático REPROVOU a questão. Sugestões de revisão: "
                    f"{parecer.sugestoes_revisao or 'ver notas por critério.'}"
                )
                iteracoes.append(
                    RegistroIteracao(
                        numero=numero, questao=questao, verificacao=verificacao,
                        parecer=parecer, feedback_para_gerador=feedback,
                    )
                )
                continue

            # aprovada pelos dois avaliadores
            iteracoes.append(
                RegistroIteracao(numero=numero, questao=questao, verificacao=verificacao, parecer=parecer)
            )
            resultado = ResultadoCiclo(aprovada=True, questao_final=questao, iteracoes=iteracoes)
            self._logar(resultado)
            return resultado

        resultado = ResultadoCiclo(aprovada=False, questao_final=None, iteracoes=iteracoes)
        self._logar(resultado)
        return resultado

    def _logar(self, resultado: ResultadoCiclo) -> None:
        """Registro completo do ciclo em JSONL (reprodutibilidade, Seção 5.5 do projeto)."""
        if self._log_dir is None:
            return
        self._log_dir.mkdir(parents=True, exist_ok=True)
        arquivo = self._log_dir / "ciclos.jsonl"
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(json.dumps(resultado.model_dump(mode="json"), ensure_ascii=False) + "\n")
