# MathScript CLI - Documentação de Comandos

## 📋 **Visão Geral**

O MathScript possui um sistema completo de Interface de Linha de Comando (CLI) que permite executar programas MathScript de diversas formas, desde a execução simples até debugging avançado com modo verbose.

## 🚀 **Métodos de Execução**

### 1. **Método Original (Sempre Funciona)**
```powershell
python main.py <arquivo.ms>
```
**Exemplo:**
```powershell
python main.py hello.ms
python main.py example/calculadora.ms
```

### 2. **CLI via PowerShell (Recomendado para Windows)**
```powershell
.\math.ps1 [opções] <arquivo.ms>
```

**Comandos Disponíveis:**
```powershell
.\math.ps1 hello.ms              # Execução direta
.\math.ps1 run hello.ms          # Execução com comando explícito
.\math.ps1 -v hello.ms           # Modo verbose (debug detalhado)
.\math.ps1 --help               # Mostra ajuda completa
.\math.ps1 --version            # Mostra versão do MathScript
```

### 3. **CLI via Batch (Windows CMD)**
```cmd
.\math.bat [opções] <arquivo.ms>
```

**Comandos Disponíveis:**
```cmd
.\math.bat hello.ms
.\math.bat run hello.ms  
.\math.bat -v hello.ms
.\math.bat --help
.\math.bat --version
```

### 4. **CLI via Python Direto**
```powershell
python mathscript_cli.py [opções] <arquivo.ms>
```

**Comandos Disponíveis:**
```powershell
python mathscript_cli.py hello.ms
python mathscript_cli.py run hello.ms
python mathscript_cli.py -v hello.ms
python mathscript_cli.py --help
python mathscript_cli.py --version
```

### 5. **Comando Global (Após Instalação)**
```powershell
# Primeiro instale:
pip install -e .

# Depois use globalmente:
math <arquivo.ms>
math run <arquivo.ms>
mathscript <arquivo.ms>
```

## 🔧 **Opções e Flags**

| Flag/Opção | Descrição | Exemplo |
|------------|-----------|---------|
| `run` | Executa arquivo explicitamente | `math run hello.ms` |
| `-v, --verbose` | Modo debug detalhado | `math -v hello.ms` |
| `--help` | Mostra ajuda completa | `math --help` |
| `--version` | Mostra versão | `math --version` |

## 📊 **Modo Verbose (-v)**

O modo verbose é especialmente útil para debugging e aprendizado, mostrando:

```powershell
.\math.ps1 -v hello.ms
```

**Saída inclui:**
- Código fonte completo
- Tokens gerados pelo lexer
- Árvore Sintática Abstrata (AST)
- Processo de execução passo a passo
- Mensagens de sucesso/erro detalhadas

## 📁 **Estrutura de Arquivos CLI**

```
MathScript/
├── mathscript_cli.py    # CLI principal (Python)
├── math.ps1             # Script PowerShell
├── math.bat             # Script Batch (CMD)
├── setup.py             # Configuração pip
├── install.py           # Instalador automático
└── docs/
    └── CLI_commands_documentation.md  # Este documento
```

## 🎯 **Exemplos Práticos**

### Execução Básica
```powershell
# Executar programa simples
.\math.ps1 hello.ms

# Resultado:
# Soma:  18
# Multiplicação:  45
```

### Debugging com Verbose
```powershell
.\math.ps1 -v hello.ms

# Resultado inclui:
# Executando: hello.ms
# Código:
# num a := 15
# num b := 3
# print("Soma: ", a + b)
# ==================================================
# Tokens gerados:
#   Token(KW_NUM, 'num')
#   Token(IDENT, 'a')
#   Token(ASSIGN, ':=')
#   ...
# ==================================================
# AST gerada: ProgramNode(...)
# ==================================================
# Soma:  18
# Execução concluída com sucesso!
```

### Verificação de Sistema
```powershell
.\math.ps1 --version
# MathScript v1.0.0
# Linguagem de programação matemática

.\math.ps1 --help
# [Mostra ajuda completa com todos os comandos]
```

## ⚙️ **Instalação Global**

### Método 1: Instalador Automático
```powershell
python install.py
```

### Método 2: Pip Manual
```powershell
pip install -e .
```

### Método 3: PATH Manual
Adicione o diretório do MathScript ao PATH do sistema.

## 🐛 **Solução de Problemas**

### Erro: "Comando não encontrado"
- **Solução**: Use `.\math.ps1` em vez de `math.ps1`
- **Alternativa**: Adicione ao PATH ou instale globalmente

### Erro: "Python não encontrado"
- **Solução**: Instale Python e adicione ao PATH
- **Verificação**: `python --version`

### Erro: "Módulos não encontrados"
- **Solução**: Execute no diretório correto do MathScript
- **Verificação**: Confirme que existe a pasta `src/`

### Erro de Importação
- **Solução**: Use `python mathscript_cli.py` diretamente
- **Diagnóstico**: Verifique se todos os arquivos `src/` existem

## 🔄 **Comparação de Métodos**

| Método | Facilidade | Velocidade | Recursos | Recomendação |
|--------|------------|------------|----------|--------------|
| `python main.py` | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Básico |
| `.\math.ps1` | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | **Recomendado** |
| `.\math.bat` | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Alternativa |
| `python mathscript_cli.py` | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Debug |
| `math` (global) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Profissional |

## 📚 **Recursos Avançados**

### Execução de Múltiplos Arquivos
```powershell
# Execute vários programas sequencialmente
.\math.ps1 programa1.ms
.\math.ps1 programa2.ms
.\math.ps1 programa3.ms
```

### Debugging Completo
```powershell
# Para análise profunda do código
.\math.ps1 -v programa_complexo.ms > debug_output.txt
```

### Integração com Scripts
```powershell
# Em um script PowerShell
$resultado = & .\math.ps1 calculo.ms
if ($LASTEXITCODE -eq 0) {
    Write-Host "Programa executado com sucesso"
} else {
    Write-Host "Erro na execução"
}
```

## 🎨 **Personalização**

Os scripts CLI podem ser modificados para:
- Adicionar novos comandos
- Alterar comportamento padrão
- Integrar com outras ferramentas
- Personalizar mensagens de saída

## 📞 **Suporte**

Para problemas com o CLI:
1. Verifique este documento
2. Use modo verbose (`-v`) para diagnóstico
3. Teste o método básico (`python main.py`)
4. Consulte os logs de erro detalhados

---

**Versão da Documentação:** 1.0.0  
**Compatibilidade:** Windows, Linux, macOS  
**Requisitos:** Python 3.7+
