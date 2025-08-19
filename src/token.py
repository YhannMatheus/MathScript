TOKEN_TYPES = [
    "KW_NUM",      # num
    "KW_TEXT",     # text
    "KW_BOOL",     # bool
    "KW_CONJ",     # conjuntos
    "IDENT",       # nome de variável ou função
    "NUMBER",      # números
    "STRING",      # textos entre ""
    "ASSIGN",      # :=
    "PLUS", "MINUS", "MUL", "DIV", "POW", "MOD", "ROOT", # operadores
    "AND", "OR", "NOT", "XOR", "XAND", "XNOT",           # lógicos
    "EQ", "NEQ", "LT", "GT", "LTE", "GTE",               # comparações
    "BLOCK_START", "BLOCK_END",                           # < >
    "LPAREN", "RPAREN",                                   # ( )
    "COMMA", "SEMICOLON"
]

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"{self.tipo}({self.valor})"