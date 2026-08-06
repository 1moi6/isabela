#!/bin/bash
# ============================================================================
#  Abre o Gerador de Questões de Matemática (macOS)
#  Duplo clique neste arquivo sempre que quiser usar o programa.
#  Se o macOS recusar na primeira vez: clique com o botão direito > Abrir.
# ============================================================================
cd "$(dirname "$0")" || exit 1

if [ ! -x ".venv/bin/python" ]; then
    echo
    echo "  O programa ainda não foi instalado nesta máquina."
    echo "  Rode primeiro:  ./instalar.command"
    echo
    read -r -p "  Pressione Enter para fechar..."
    exit 1
fi

.venv/bin/python executar.py
