#!/usr/bin/env python3
"""
Setup script para instalar o MathScript CLI
"""

from setuptools import setup, find_packages
import os
import sys

# Lê o README se existir
README = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        README = f.read()

setup(
    name="mathscript",
    version="1.0.0",
    description="MathScript - Linguagem de Programação Matemática",
    long_description=README,
    long_description_content_type="text/markdown",
    author="YhannMatheus  |  Kaleo Nabor",
    author_email="yhannmatheus@icloud.com   |   kaleo.nabor@gmail.com",
    url="https://github.com/YhannMatheus/MathScript",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "math=mathscript_cli:main",
            "mathscript=mathscript_cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Education",
    ],
    keywords="mathscript programming language interpreter math",
)
