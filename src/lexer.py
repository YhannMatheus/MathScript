from src.token import Token

class Lexer:
    KEYWORDS = {
        "num": "KW_NUM",
        "text": "KW_TEXT",
        "bool": "KW_BOOL",
        "conjuntos": "KW_CONJ",
        "and": "AND",
        "or": "OR",
        "not": "NOT",
        "xor": "XOR",
        "xand": "XAND",
        "xnot": "XNOT"
    }

    SYMBOLS = {
        ":=": "ASSIGN",
        "+": "PLUS",
        "-": "MINUS",
        "*": "MUL",
        "/": "DIV",
        "**": "POW",
        "//": "ROOT",
        "%": "MOD",
        "==": "EQ",
        "!=": "NEQ",
        "<": "LT",
        ">": "GT",
        "<=": "LTE",
        ">=": "GTE",
        "<": "BLOCK_START",
        ">": "BLOCK_END",
        "(": "LPAREN",
        ")": "RPAREN",
        ",": "COMMA",
        ";": "SEMICOLON"
    }

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def generate_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
                continue

            # Números
            if self.current_char.isdigit():
                tokens.append(self.generate_number())
                continue

            # Identificadores ou keywords
            if self.current_char.isalpha():
                tokens.append(self.generate_identifier())
                continue

            # Símbolos
            matched = False
            for sym, tipo in sorted(self.SYMBOLS.items(), key=lambda x: -len(x[0])):  # verifica símbolos longos primeiro
                if self.text[self.pos:self.pos+len(sym)] == sym:
                    tokens.append(Token(tipo, sym))
                    for _ in range(len(sym)):
                        self.advance()
                    matched = True
                    break
            if matched:
                continue

            raise Exception(f"Caractere inválido: {self.current_char}")

        return tokens

    def generate_number(self):
        num_str = ""
        dot_count = 0
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == "."):
            if self.current_char == ".":
                dot_count += 1
                if dot_count > 1:
                    break
            num_str += self.current_char
            self.advance()
        return Token("NUMBER", float(num_str) if "." in num_str else int(num_str))

    def generate_identifier(self):
        id_str = ""
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == "_"):
            id_str += self.current_char
            self.advance()
        tipo = self.KEYWORDS.get(id_str, "IDENT")
        return Token(tipo, id_str)
