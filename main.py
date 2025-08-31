#!/usr/bin/env python3
import sys
from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
from src.errors import MathScriptError

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.ms>")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            code = file.read()
        
        # Tokenização
        lexer = Lexer(code)
        tokens = lexer.generate_tokens()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Execução
        interpreter = Interpreter()
        interpreter.interpret(ast)
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{sys.argv[1]}' não encontrado.")
        sys.exit(1)
    except MathScriptError as e:
        print(f"Erro MathScript: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()