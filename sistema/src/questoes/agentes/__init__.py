"""Os quatro agentes do sistema (Cap. 4 da dissertação):

Gerador (LLM) — produz a questão a partir da especificação.
Verificador Simbólico (SymPy, sem LLM) — confirma ou refuta o gabarito.
Crítico Didático (LLM + rubrica) — avalia a qualidade pedagógica.
Orquestrador (código puro) — coordena o ciclo e aplica a política de decisão.
"""

from .critico import CriticoDidatico
from .gerador import Gerador
from .orquestrador import Orquestrador
from .verificador import VerificadorSimbolico

__all__ = ["Gerador", "VerificadorSimbolico", "CriticoDidatico", "Orquestrador"]
