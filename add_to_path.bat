@echo off
REM Script para adicionar MathScript ao PATH permanentemente
echo Adicionando MathScript ao PATH do Windows...

REM Obtem o diretorio atual
set MATHSCRIPT_DIR=%~dp0
set MATHSCRIPT_DIR=%MATHSCRIPT_DIR:~0,-1%

echo Diretorio do MathScript: %MATHSCRIPT_DIR%

REM Adiciona ao PATH do usuario (mais seguro que PATH do sistema)
for /f "usebackq tokens=2,*" %%A in (`reg query HKCU\Environment /v PATH`) do set user_path=%%B

REM Verifica se ja esta no PATH
echo %user_path% | find /i "%MATHSCRIPT_DIR%" > nul
if %errorlevel%==0 (
    echo MathScript ja esta no PATH!
) else (
    echo Adicionando ao PATH...
    if defined user_path (
        reg add HKCU\Environment /v PATH /t REG_EXPAND_SZ /d "%user_path%;%MATHSCRIPT_DIR%" /f
    ) else (
        reg add HKCU\Environment /v PATH /t REG_EXPAND_SZ /d "%MATHSCRIPT_DIR%" /f
    )
    
    echo MathScript adicionado ao PATH com sucesso!
    echo.
    echo IMPORTANTE: Reinicie o PowerShell/CMD para usar o comando 'math'
    echo.
    echo Teste com: math --help
)

pause
