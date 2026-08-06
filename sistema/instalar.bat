@echo off
rem ============================================================================
rem  Instalacao do Gerador de Questoes de Matematica (Windows)
rem  Duplo clique neste arquivo. Roda uma unica vez, na primeira utilizacao.
rem
rem  Mensagens sem acento de proposito: o console do Windows embaralha
rem  acentuacao dependendo da configuracao regional da maquina.
rem ============================================================================
setlocal
cd /d "%~dp0"
title Instalacao - Gerador de Questoes

echo.
echo ============================================================
echo    GERADOR DE QUESTOES DE MATEMATICA - INSTALACAO
echo ============================================================
echo.
echo Esta janela vai baixar da internet o que o programa precisa.
echo Pode demorar de 2 a 10 minutos, dependendo da conexao.
echo NAO feche a janela ate aparecer a mensagem de conclusao.
echo.

rem --- Procura um Python 3.11 ou mais novo -----------------------------------
set "PY="
py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)" >nul 2>nul
if not errorlevel 1 set "PY=py -3"

if not defined PY (
    python -c "import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)" >nul 2>nul
    if not errorlevel 1 set "PY=python"
)

if not defined PY goto sem_python

echo [1/3] Python encontrado.
%PY% --version
echo.

rem --- Cria o ambiente isolado ----------------------------------------------
if exist ".venv\Scripts\python.exe" (
    echo [2/3] Ambiente ja existe, reaproveitando.
) else (
    echo [2/3] Preparando o ambiente do programa...
    %PY% -m venv ".venv"
    if errorlevel 1 goto erro_venv
)
echo.

rem --- Instala as dependencias ----------------------------------------------
echo [3/3] Baixando os componentes. Isso e a parte demorada...
echo.
call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt
if errorlevel 1 goto erro_pip

echo.
echo ============================================================
echo    INSTALACAO CONCLUIDA COM SUCESSO
echo ============================================================
echo.
echo Para usar o programa, de duplo clique no arquivo:
echo.
echo        iniciar.bat
echo.
echo Este arquivo (instalar.bat) nao precisa ser executado de novo.
echo.
pause
exit /b 0

rem ============================================================================
:sem_python
echo.
echo ------------------------------------------------------------
echo    FALTA INSTALAR O PYTHON
echo ------------------------------------------------------------
echo.
echo Este computador nao tem o Python 3.11 (ou mais novo) instalado.
echo.
echo O QUE FAZER:
echo   1) Abra o site   https://www.python.org/downloads/
echo   2) Clique no botao amarelo "Download Python" e execute o arquivo.
echo   3) IMPORTANTE: na primeira tela do instalador, MARQUE a caixinha
echo      "Add python.exe to PATH", que fica embaixo. Sem ela nao funciona.
echo   4) Clique em "Install Now" e espere terminar.
echo   5) Volte aqui e de duplo clique em instalar.bat novamente.
echo.
pause
exit /b 1

rem ============================================================================
:erro_venv
echo.
echo ------------------------------------------------------------
echo    ERRO ao preparar o ambiente
echo ------------------------------------------------------------
echo.
echo Isso costuma acontecer quando a pasta esta em um lugar protegido
echo (por exemplo, dentro de "Arquivos de Programas").
echo.
echo Tente mover a pasta inteira para a Area de Trabalho e rodar de novo.
echo.
pause
exit /b 1

rem ============================================================================
:erro_pip
echo.
echo ------------------------------------------------------------
echo    ERRO ao baixar os componentes
echo ------------------------------------------------------------
echo.
echo Verifique se o computador esta conectado a internet e rode
echo instalar.bat novamente.
echo.
echo Se estiver em uma rede de escola/universidade, o antivirus ou o
echo firewall podem estar bloqueando o download.
echo.
pause
exit /b 1
