#!/bin/bash
# ============================================================================
#  Instalação do Gerador de Questões de Matemática (macOS)
#  Duplo clique neste arquivo. Roda uma única vez, na primeira utilização.
# ============================================================================
cd "$(dirname "$0")" || exit 1

echo
echo "============================================================"
echo "   GERADOR DE QUESTÕES DE MATEMÁTICA — INSTALAÇÃO"
echo "============================================================"
echo
echo "Esta janela vai baixar da internet o que o programa precisa."
echo "Pode demorar de 2 a 10 minutos, dependendo da conexão."
echo

PY=""
for candidato in python3.13 python3.12 python3.11 python3; do
    if command -v "$candidato" >/dev/null 2>&1 &&
       "$candidato" -c 'import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)' 2>/dev/null; then
        PY="$candidato"
        break
    fi
done

if [ -z "$PY" ]; then
    echo "------------------------------------------------------------"
    echo "   FALTA INSTALAR O PYTHON"
    echo "------------------------------------------------------------"
    echo
    echo "Este computador não tem o Python 3.11 (ou mais novo)."
    echo "Baixe em https://www.python.org/downloads/ e rode este arquivo de novo."
    echo
    read -r -p "Pressione Enter para fechar..."
    exit 1
fi

echo "[1/3] Python encontrado: $($PY --version)"

if [ -x ".venv/bin/python" ]; then
    echo "[2/3] Ambiente já existe, reaproveitando."
else
    echo "[2/3] Preparando o ambiente do programa..."
    "$PY" -m venv .venv || { echo "ERRO ao preparar o ambiente."; read -r; exit 1; }
fi

echo "[3/3] Baixando os componentes. Esta é a parte demorada..."
.venv/bin/python -m pip install --upgrade pip --quiet
if ! .venv/bin/python -m pip install -r requirements.txt; then
    echo
    echo "ERRO ao baixar os componentes. Verifique a conexão e tente de novo."
    read -r -p "Pressione Enter para fechar..."
    exit 1
fi

chmod +x iniciar.command 2>/dev/null

echo
echo "============================================================"
echo "   INSTALAÇÃO CONCLUÍDA COM SUCESSO"
echo "============================================================"
echo
echo "Para usar o programa, dê duplo clique em:  iniciar.command"
echo
read -r -p "Pressione Enter para fechar..."
