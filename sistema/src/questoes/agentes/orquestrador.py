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
from collections.abc import Callable
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
        ao_progredir: Callable[[dict], None] | None = None,
    ):
        self._gerador = gerador
        self._verificador = verificador
        self._critico = critico
        self._max = max_iteracoes
        self._log_dir = log_dir
        # Aviso de progresso para quem estiver acompanhando de fora (a interface).
        # É observação, não decisão: a política do ciclo continua inteira aqui.
        self._ao_progredir = ao_progredir or (lambda _: None)

    def produzir(self, spec: Especificacao) -> ResultadoCiclo:
        iteracoes: list[RegistroIteracao] = []
        feedback: str | None = None

        for numero in range(1, self._max + 1):
            self._ao_progredir({"iteracao": numero, "etapa": "gerando"})
            questao = self._gerar_com_folga(spec, feedback)

            self._ao_progredir({"iteracao": numero, "etapa": "verificando"})
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

            self._ao_progredir({
                "iteracao": numero, "etapa": "criticando",
                "veredicto": verificacao.veredicto.value,
            })
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
            self._logar(resultado, spec)
            return resultado

        resultado = ResultadoCiclo(aprovada=False, questao_final=None, iteracoes=iteracoes)
        self._logar(resultado, spec)
        return resultado

    def _gerar_com_folga(self, spec: Especificacao, feedback: str | None):
        """Gera, e tenta uma segunda vez pedindo concisão se a primeira não vier.

        Na geração do acervo de 8 de agosto, um ciclo morreu porque o modelo
        esgotou o limite de saída antes de fechar o JSON: `max_tokens`. A exceção
        subia e derrubava o ciclo inteiro. Pedir concisão resolve o caso
        observado sem mexer no contrato --- e uma segunda falha continua subindo,
        porque aí não é limite de tamanho, é outra coisa.
        """
        try:
            return self._gerador.gerar(spec, feedback=feedback)
        except Exception as exc:
            aviso = (
                "A resposta anterior não pôde ser lida por inteiro "
                f"({type(exc).__name__}). Produza a MESMA questão de forma mais "
                "econômica: resolução mais curta e apenas as afirmações "
                "verificáveis essenciais."
            )
            return self._gerador.gerar(spec, feedback=f"{feedback}\n{aviso}" if feedback else aviso)

    def _logar(self, resultado: ResultadoCiclo, spec: Especificacao) -> None:
        """Registro completo do ciclo em JSONL (reprodutibilidade, Seção 5.5 do projeto).

        Junto do ciclo vai a divergência entre o nível cognitivo pedido e os
        verbos da habilidade. Não é erro nem impede a geração --- é o dado que
        permite, na avaliação empírica, perguntar se pedidos fora do nível
        sugerido custam mais iterações ou terminam mais em descarte.
        """
        if self._log_dir is None:
            return
        self._log_dir.mkdir(parents=True, exist_ok=True)
        arquivo = self._log_dir / "ciclos.jsonl"
        registro = {
            **resultado.model_dump(mode="json"),
            "bloom_divergente": spec.bloom_diverge(),
            "bloom_sugerido": spec.bloom_sugerido(),
        }
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(json.dumps(registro, ensure_ascii=False) + "\n")
