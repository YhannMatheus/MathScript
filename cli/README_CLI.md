# MathScript CLI

Sistema de comandos de terminal para a linguagem MathScript.

## Instalação

### Opção 1: Instalação Automática (Recomendada)

```bash
python install.py
```

O script de instalação irá detectar seu sistema operacional e fornecer instruções específicas.

### Opção 2: Instalação via pip

```bash
pip install -e .
```

### Opção 3: Instalação Manual

#### Windows
1. Adicione a pasta do projeto ao PATH do Windows
2. Use o comando `math.bat` ou `python mathscript_cli.py`

#### Linux/macOS
```bash
# Criar symlink (requer sudo)
sudo ln -sf /caminho/completo/para/mathscript_cli.py /usr/local/bin/math

# OU adicionar ao PATH no ~/.bashrc
export PATH="/caminho/para/projeto:$PATH"
```

## Uso

Após a instalação, você pode usar o comando `math` de qualquer lugar:

### Comandos Disponíveis

```bash
# Executar um arquivo MathScript
math run hello.ms

# Execução direta (sem 'run')
math hello.ms

# Modo verbose (mostra tokens, AST, etc.)
math -v hello.ms
math run -v hello.ms

# Mostrar versão
math --version

# Mostrar ajuda
math --help
```

### Exemplos

```bash
# Executar o exemplo
math run example/hello.ms

# Executar com saída detalhada
math -v example/hello.ms

# Verificar se a instalação funcionou
math --version
```

## Estrutura de Arquivos

```
MathScript/
├── mathscript_cli.py    # CLI principal
├── math.bat             # Script batch para Windows
├── setup.py             # Configuração do pip
├── install.py           # Script de instalação
├── main.py              # Script original
└── src/                 # Código fonte do MathScript
    ├── lexer.py
    ├── parser.py
    ├── interpreter.py
    └── ...
```

## Funcionalidades do CLI

- **Execução de arquivos**: Suporte completo a arquivos `.ms`
- **Modo verbose**: Debug detalhado mostrando tokens e AST
- **Tratamento de erros**: Mensagens claras de erro
- **Multiplataforma**: Funciona no Windows, Linux e macOS
- **Flexibilidade**: Múltiplas formas de executar arquivos

## Solução de Problemas

### Comando 'math' não encontrado

1. Verifique se a instalação foi bem-sucedida
2. No Windows, verifique se a pasta está no PATH
3. Tente usar `python mathscript_cli.py` diretamente

### Erro de importação

Certifique-se de estar executando no diretório correto do projeto MathScript, que contém a pasta `src/`.

### Erro de permissão (Linux/macOS)

Use `sudo` para criar symlinks em `/usr/local/bin/`:
```bash
sudo ln -sf $(pwd)/mathscript_cli.py /usr/local/bin/math
```

## Desenvolvimento

Para modificar o CLI, edite o arquivo `mathscript_cli.py`. As principais seções são:

- `run_file()`: Execução de arquivos MathScript
- `main()`: Parse de argumentos da linha de comando
- `show_help()`: Texto de ajuda

## Licença

MIT License - Veja o arquivo LICENSE para detalhes.
