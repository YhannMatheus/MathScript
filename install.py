#!/usr/bin/env python3
"""
Script de instalação para o MathScript CLI
Este script configura o comando 'math' no sistema
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def is_windows():
    return sys.platform.startswith("win")


def is_unix():
    return sys.platform.startswith(("linux", "darwin"))


def install_windows():
    """Instalação para Windows"""
    print("Configurando MathScript para Windows...")

    # Diretório atual do projeto
    project_dir = Path(__file__).parent.absolute()

    # Verifica se os arquivos necessários existem
    cli_script = project_dir / "mathscript_cli.py"
    batch_file = project_dir / "math.bat"

    if not cli_script.exists():
        print(f"Erro: Arquivo {cli_script} não encontrado!")
        return False

    if not batch_file.exists():
        print(f"Erro: Arquivo {batch_file} não encontrado!")
        return False

    print(f"Projeto MathScript localizado em: {project_dir}")

    # Opção 1: Instalar via pip (recomendado)
    print("\n=== INSTALAÇÃO VIA PIP (Recomendado) ===")
    print("1. Instalação global via pip:")
    print(f'   cd "{project_dir}"')
    print("   pip install -e .")
    print("   (Isso criará o comando 'math' globalmente)")

    # Opção 2: Adicionar ao PATH
    print("\n=== INSTALAÇÃO MANUAL ===")
    print("2. Adicionar ao PATH do Windows:")
    print(f"   - Adicione esta pasta ao PATH: {project_dir}")
    print("   - Após isso, você poderá usar 'math' de qualquer lugar")

    print("\n=== TESTE ===")
    print("Após a instalação, teste com:")
    print("   math --help")
    print("   math run example/hello.ms")

    return True


def install_unix():
    """Instalação para Unix/Linux/macOS"""
    print("Configurando MathScript para Unix/Linux/macOS...")

    project_dir = Path(__file__).parent.absolute()
    cli_script = project_dir / "mathscript_cli.py"

    if not cli_script.exists():
        print(f"Erro: Arquivo {cli_script} não encontrado!")
        return False

    # Torna o script executável
    os.chmod(cli_script, 0o755)

    print(f"Projeto MathScript localizado em: {project_dir}")

    # Opção 1: Instalar via pip
    print("\n=== INSTALAÇÃO VIA PIP (Recomendado) ===")
    print("1. Instalação global via pip:")
    print(f'   cd "{project_dir}"')
    print("   pip install -e .")
    print("   (Isso criará o comando 'math' globalmente)")

    # Opção 2: Symlink manual
    print("\n=== INSTALAÇÃO MANUAL ===")
    print("2. Criar symlink manual:")
    print(f"   sudo ln -sf {cli_script} /usr/local/bin/math")
    print("   (Requer privilégios de administrador)")

    # Opção 3: Adicionar ao PATH
    print("\n=== ADICIONAR AO PATH ===")
    print("3. Adicionar ao ~/.bashrc ou ~/.zshrc:")
    print(f'   export PATH="{project_dir}:$PATH"')
    print("   source ~/.bashrc  # ou source ~/.zshrc")

    print("\n=== TESTE ===")
    print("Após a instalação, teste com:")
    print("   math --help")
    print("   math run example/hello.ms")

    return True


def auto_install():
    """Tentativa de instalação automática via pip"""
    print("Tentando instalação automática...")

    try:
        # Tenta instalar via pip
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            check=True,
            cwd=Path(__file__).parent,
        )
        print("\n✅ Instalação via pip concluída com sucesso!")
        print("O comando 'math' agora deve estar disponível globalmente.")
        print("\nTeste com: math --help")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Falha na instalação automática: {e}")
        print("Tente a instalação manual mostrada acima.")
        return False
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        return False


def main():
    print("=== INSTALADOR DO MATHSCRIPT CLI ===\n")

    # Verifica se estamos no diretório correto
    if not Path("mathscript_cli.py").exists():
        print("Erro: Execute este script no diretório do projeto MathScript")
        print("Deve conter o arquivo 'mathscript_cli.py'")
        return 1

    # Detecta o sistema operacional
    if is_windows():
        success = install_windows()
    elif is_unix():
        success = install_unix()
    else:
        print(f"Sistema operacional não suportado: {sys.platform}")
        return 1

    if not success:
        return 1

    # Pergunta se quer tentar instalação automática
    print(f"\n{'='*50}")
    response = input("Deseja tentar a instalação automática via pip? (s/N): ").lower()

    if response in ("s", "sim", "y", "yes"):
        auto_install()
    else:
        print("Instalação manual escolhida. Siga as instruções acima.")

    print(f"\n{'='*50}")
    print("Instalação do MathScript CLI concluída!")
    print("Documentação: https://github.com/YhannMatheus/MathScript")

    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
