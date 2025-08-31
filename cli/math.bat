@echo off
REM MathScript Command Wrapper for Windows
REM Este script permite usar 'math' como comando no Windows

REM Verifica se Python está disponível
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Erro: Python nao esta instalado ou nao esta no PATH
    exit /b 1
)

REM Obtém o diretório onde este script está localizado
set SCRIPT_DIR=%~dp0

REM Executa o CLI do MathScript
python "%SCRIPT_DIR%mathscript_cli.py" %*
