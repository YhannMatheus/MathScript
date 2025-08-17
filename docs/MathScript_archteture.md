MathScript/
├── main.py                  # Ponto de entrada
├── src/
│   ├── lexer.py             # Analisador léxico (tokenização)
│   ├── parser.py            # Analisador sintático (AST)
│   ├── ast_nodes.py         # Definição de nós da árvore sintática
│   ├── interpreter.py       # Executor da AST
│   ├── environment.py       # Armazena variáveis e conjuntos (escopo)
│   └── errors.py            # Tratamento de erros (lexical, sintático, runtime)
├── examples/                # Scripts MathScript de exemplo
├── tests/                   # Testes unitários e de integração
└── docs/                    # Documentação da linguagem

## Fluxo de execução

- main.py lê o arquivo MathScript.

- Lexer converte em tokens.

- Parser cria a AST.

- Interpreter percorre a AST:

- Avalia expressões e blocos < >.

- Executa funções.

- Atualiza o Environment.

### Resultados impressos no console.

[ Código fonte (.ms) ]
           |
           v
         Lexer
           |
           v
         Parser
           |
           v
          AST
           |
           v
       Interpreter
           |
           v
   Environment & Saída