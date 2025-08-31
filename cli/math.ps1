# MathScript PowerShell Wrapper
# Este script permite usar 'math' como comando no PowerShell

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Arguments
)

# Obtém o diretório onde este script está localizado
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Verifica se Python está disponível
try {
    python --version | Out-Null
} catch {
    Write-Error "Erro: Python não está instalado ou não está no PATH"
    exit 1
}

# Executa o CLI do MathScript
$CLIScript = Join-Path $ScriptDir "mathscript_cli.py"
& python $CLIScript @Arguments
