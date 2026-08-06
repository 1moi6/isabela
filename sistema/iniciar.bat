@echo off
rem ============================================================================
rem  Abre o Gerador de Questoes de Matematica (Windows)
rem  Duplo clique neste arquivo sempre que quiser usar o programa.
rem ============================================================================
setlocal
cd /d "%~dp0"
title Gerador de Questoes - NAO FECHE esta janela

if not exist ".venv\Scripts\activate.bat" (
    echo.
    echo O programa ainda nao foi instalado neste computador.
    echo.
    echo De duplo clique primeiro no arquivo:   instalar.bat
    echo.
    pause
    exit /b 1
)

call ".venv\Scripts\activate.bat"

python executar.py

echo.
echo O programa foi encerrado.
pause
