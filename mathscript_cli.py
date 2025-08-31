#!/usr/bin/env python3
"""
MathScript Command Line Interface
Permite executar arquivos MathScript via comando 'math'
"""
import sys
import os
import argparse
from pathlib import Path

# Adiciona o diretório atual ao path para imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from src.lexer import Lexer
    from src.parser import Parser
    from src.interpreter import Interpreter
    from src.errors import MathScriptError
except ImportError as e:
    print(f"Erro ao importar módulos MathScript: {e}")
    print("Certifique-se de que você está no diretório correto do MathScript")
    sys.exit(1)


def run_file(filename, verbose=False):
    """Executa um arquivo MathScript"""
    try:
        if not os.path.exists(filename):
            print(f"Erro: Arquivo '{filename}' não encontrado.")
            return 1

        with open(filename, "r", encoding="utf-8") as file:
            code = file.read()

        if verbose:
            print(f"Executando: {filename}")
            print(f"Código:\n{code}\n" + "=" * 50)

        # Tokenização
        lexer = Lexer(code)
        tokens = lexer.generate_tokens()

        if verbose:
            print("Tokens gerados:")
            for token in tokens:
                print(f"  {token}")
            print("=" * 50)

        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()

        if verbose:
            print(f"AST gerada: {ast}")
            print("=" * 50)

        # Execução
        interpreter = Interpreter()
        interpreter.interpret(ast)

        if verbose:
            print("\nExecução concluída com sucesso!")

        return 0

    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
        return 1
    except MathScriptError as e:
        print(f"Erro MathScript: {e}")
        return 1
    except Exception as e:
        print(f"Erro inesperado: {e}")
        if verbose:
            import traceback

            traceback.print_exc()
        return 1


def show_version():
    """Mostra a versão do MathScript"""
    print("MathScript v1.0.0")
    print("Linguagem de programação matemática")


def show_help():
    """Mostra ajuda sobre os comandos"""
    help_text = """
MathScript - Linguagem de Programação Matemática

Uso:
  math run <arquivo.ms>     Executa um arquivo MathScript
  math --version           Mostra a versão
  math --help             Mostra esta ajuda
  math -v <arquivo.ms>    Executa em modo verbose (detalhado)

Exemplos:
  math run hello.ms        Executa o arquivo hello.ms
  math -v hello.ms         Executa hello.ms com saída detalhada
  
Arquivos MathScript devem ter a extensão .ms
"""
    print(help_text)


def main():
    """Função principal do CLI"""
    parser = argparse.ArgumentParser(
        prog="math",
        description="MathScript Command Line Interface",
        add_help=False,  # Desabilita ajuda padrão para usar nossa própria
    )

    parser.add_argument(
        "command", nargs="?", help="Comando a executar (run, --version, --help)"
    )
    parser.add_argument("file", nargs="?", help="Arquivo MathScript para executar")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo verbose")
    parser.add_argument("--version", action="store_true", help="Mostra versão")
    parser.add_argument("--help", action="store_true", help="Mostra ajuda")

    args = parser.parse_args()

    # Tratamento de argumentos especiais
    if args.version:
        show_version()
        return 0

    if args.help or (not args.command and not args.file):
        show_help()
        return 0

    # Modo verbose simples (math -v arquivo.ms)
    if args.verbose and args.command and not args.file:
        return run_file(args.command, verbose=True)

    # Comando run
    if args.command == "run":
        if not args.file:
            print("Erro: Especifique um arquivo para executar")
            print("Uso: math run <arquivo.ms>")
            return 1
        return run_file(args.file, args.verbose)

    # Execução direta (math arquivo.ms)
    if args.command and not args.file:
        # Verifica se é um arquivo .ms
        if args.command.endswith(".ms"):
            return run_file(args.command, args.verbose)
        else:
            print(f"Comando desconhecido: {args.command}")
            show_help()
            return 1

    # Se chegou até aqui, há erro na sintaxe
    print("Uso incorreto dos argumentos")
    show_help()
    return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
