class MathScriptError(Exception):
    pass

class LexerError(MathScriptError):
    def __init__(self, message, position):
        super().__init__(f"Erro léxico: {message} (posição {position})")

class ParserError(MathScriptError):
    def __init__(self, message, token=None):
        if token:
            super().__init__(f"Erro sintático: {message} (token: {token})")
        else:
            super().__init__(f"Erro sintático: {message}")

class RuntimeError(MathScriptError):
    def __init__(self, message, context=None):
        if context:
            super().__init__(f"Erro de execução: {message} (contexto: {context})")
        else:
            super().__init__(f"Erro de execução: {message}")