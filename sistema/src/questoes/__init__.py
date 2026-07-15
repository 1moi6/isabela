"""Sistema multiagente para geração assistida de questões de Matemática do EM.

Produto educacional da dissertação PROFMAT/UFMT de Isabella Dias Ribeiro dos Santos.
Arquitetura: Gerador (LLM) -> Verificador Simbólico (SymPy) + Crítico Didático (LLM)
-> Orquestrador (política de decisão com ciclos de revisão).
"""

__version__ = "0.1.0"
