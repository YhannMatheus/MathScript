# parser.py
from src.ast_nodes import *
from src.errors import ParserError
from src.token import Token


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def advance(self):
        self.pos += 1
        self.current_token = (
            self.tokens[self.pos] if self.pos < len(self.tokens) else None
        )

    def expect(self, token_type, error_msg):
        if self.current_token and self.current_token.tipo == token_type:
            token = self.current_token
            self.advance()
            return token
        else:
            raise ParserError(error_msg, self.current_token)

    def parse(self):
        statements = []
        while self.current_token:
            if self.current_token.tipo in ["KW_NUM", "KW_TEXT", "KW_BOOL", "KW_CONJ"]:
                statements.append(self.parse_variable_declaration())
            elif self.current_token.tipo == "IDENT" and self.check_next_token_type(
                [":=", "+=", "-=", "*=", "/=", "**=", "//=", "%="]
            ):
                statements.append(self.parse_assignment())
            elif self.current_token.tipo == "IDENT" and self.check_next_token_is(
                "LPAREN"
            ):
                statements.append(self.parse_function_call())
            elif self.current_token.tipo == "KW_FUN":
                statements.append(self.parse_function_definition())
            elif self.current_token.tipo == "KW_IF":
                statements.append(self.parse_if_statement())
            elif self.current_token.tipo == "KW_PRINT":
                statements.append(self.parse_print_statement())
            else:
                raise ParserError(f"Token inesperado: {self.current_token}")

        return ProgramNode(statements)

    def peek_next(self):
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return None

    def check_next_token_type(self, expected_types):
        """Verifica se o próximo token tem um dos tipos esperados"""
        next_token = self.peek_next()
        return next_token is not None and next_token.tipo in expected_types

    def check_next_token_is(self, expected_type):
        """Verifica se o próximo token é de um tipo específico"""
        next_token = self.peek_next()
        return next_token is not None and next_token.tipo == expected_type

    def parse_variable_declaration(self):
        if not self.current_token:
            raise ParserError(
                "Fim inesperado dos tokens ao parsear declaração de variável"
            )

        var_type = self.current_token.valor
        self.advance()

        var_name = self.expect("IDENT", "Esperado nome de variável").valor

        self.expect("ASSIGN", "Esperado operador de atribuição :=")

        value = self.parse_expression()

        return VariableDeclarationNode(var_type, var_name, value)

    def parse_assignment(self):
        if not self.current_token:
            raise ParserError("Fim inesperado dos tokens ao parsear atribuição")

        var_name = self.current_token.valor
        self.advance()

        if not self.current_token:
            raise ParserError(
                "Fim inesperado dos tokens ao parsear operador de atribuição"
            )

        op = self.current_token.valor
        self.advance()

        value = self.parse_expression()

        return AssignmentNode(var_name, op, value)

    def parse_function_definition(self):
        self.expect("KW_FUN", "Esperado 'fun'")

        name = self.expect("IDENT", "Esperado nome de função").valor

        self.expect("LPAREN", "Esperado '('")

        params = []
        if self.current_token and self.current_token.tipo != "RPAREN":
            params.append(self.expect("IDENT", "Esperado nome de parâmetro").valor)
            while self.current_token and self.current_token.tipo == "COMMA":
                self.advance()
                params.append(self.expect("IDENT", "Esperado nome de parâmetro").valor)

        self.expect("RPAREN", "Esperado ')'")

        self.expect("LBRACE", "Esperado '{' para abrir o corpo da função")

        body = self.parse_block(end_token="RBRACE")  # Pass RBRACE as the end token

        self.expect("RBRACE", "Esperado '}' para fechar o corpo da função")

        return FunctionNode(name, params, body)

    def parse_function_call(self):
        if not self.current_token:
            raise ParserError("Fim inesperado dos tokens ao parsear chamada de função")

        name = self.current_token.valor
        self.advance()

        self.expect("LPAREN", "Esperado '('")

        args = []
        if self.current_token and self.current_token.tipo != "RPAREN":
            args.append(self.parse_expression())
            while self.current_token and self.current_token.tipo == "COMMA":
                self.advance()
                args.append(self.parse_expression())

        self.expect("RPAREN", "Esperado ')'")

        return FunctionCallNode(name, args)

    def parse_if_statement(self):
        self.expect("KW_IF", "Esperado 'if'")

        self.expect("LPAREN", "Esperado '('")

        condition = self.parse_expression()

        self.expect("RPAREN", "Esperado ')'")

        self.expect("ARROW", "Esperado '->'")

        self.expect("LBRACE", "Esperado '{'")  # Change from BLOCK_START to LBRACE

        then_block = self.parse_block(
            end_token="RBRACE"
        )  # Pass RBRACE as the end token

        self.expect("RBRACE", "Esperado '}'")  # Change from BLOCK_END to RBRACE

        return IfNode(condition, then_block)

    def parse_block(self, end_token=None):
        statements = []
        # The while loop condition needs to be adjusted to handle the different end tokens
        while self.current_token and self.current_token.tipo != end_token:
            # Tenta parsear como statement primeiro
            try:
                if self.current_token and self.current_token.tipo in [
                    "KW_NUM",
                    "KW_TEXT",
                    "KW_BOOL",
                    "KW_CONJ",
                ]:
                    statements.append(self.parse_variable_declaration())
                elif (
                    self.current_token
                    and self.current_token.tipo == "IDENT"
                    and self.check_next_token_type(
                        [":=", "+=", "-=", "*=", "/=", "**=", "//=", "%="]
                    )
                ):
                    statements.append(self.parse_assignment())
                elif (
                    self.current_token
                    and self.current_token.tipo == "IDENT"
                    and self.check_next_token_is("LPAREN")
                ):
                    statements.append(self.parse_function_call())
                elif self.current_token and self.current_token.tipo == "KW_PRINT":
                    statements.append(self.parse_print_statement())
                elif self.current_token and self.current_token.tipo == "KW_IF":
                    statements.append(self.parse_if_statement())
                else:
                    # Se não for um statement, tenta parsear como expressão
                    statements.append(self.parse_expression())
                    # Consome ponto e vírgula se existir
                    if self.current_token and self.current_token.tipo == "SEMICOLON":
                        self.advance()
            except ParserError as e:
                raise ParserError(f"Erro no bloco: {e}")

        return BlockNode(statements)

    def parse_expression(self):
        return self.parse_logical_or()

    def parse_logical_or(self):
        left = self.parse_logical_and()

        while self.current_token and self.current_token.tipo == "OR":
            op = self.current_token.valor
            self.advance()
            right = self.parse_logical_and()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_logical_and(self):
        left = self.parse_comparison()

        while self.current_token and self.current_token.tipo == "AND":
            op = self.current_token.valor
            self.advance()
            right = self.parse_comparison()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_comparison(self):
        left = self.parse_term()

        while self.current_token and self.current_token.tipo in [
            "EQ",
            "NEQ",
            "LT",
            "GT",
            "LTE",
            "GTE",
        ]:
            op = self.current_token.valor
            self.advance()
            right = self.parse_term()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.current_token and self.current_token.tipo in ["PLUS", "MINUS"]:
            op = self.current_token.valor
            self.advance()
            right = self.parse_factor()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_factor(self):
        left = self.parse_power()

        while self.current_token and self.current_token.tipo in ["MUL", "DIV", "MOD"]:
            op = self.current_token.valor
            self.advance()
            right = self.parse_power()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_power(self):
        left = self.parse_unary()

        while self.current_token and self.current_token.tipo == "POW":
            op = self.current_token.valor
            self.advance()
            right = self.parse_unary()
            left = BinaryOpNode(left, op, right)

        return left

    def parse_unary(self):
        if self.current_token and self.current_token.tipo in ["NOT", "MINUS", "PLUS"]:
            op = self.current_token.valor
            self.advance()
            expr = self.parse_unary()
            return UnaryOpNode(op, expr)

        return self.parse_primary()

    def parse_primary(self):
        if self.current_token is None:
            raise ParserError("Fim inesperado dos tokens")

        if self.current_token.tipo == "NUMBER":
            value = self.current_token.valor
            self.advance()
            return NumberNode(value)

        elif self.current_token.tipo == "STRING":
            value = self.current_token.valor
            self.advance()
            return StringNode(value)

        elif self.current_token.tipo == "BOOL":
            value = self.current_token.valor == "true"
            self.advance()
            return BooleanNode(value)

        elif self.current_token.tipo == "IDENT":
            name = self.current_token.valor
            self.advance()
            return VariableNode(name)

        elif self.current_token.tipo == "LPAREN":
            self.advance()
            expr = self.parse_expression()
            self.expect("RPAREN", "Esperado ')'")
            return expr

        elif self.current_token.tipo == "LBRACE":
            self.advance()
            block = self.parse_block(end_token="RBRACE")
            self.expect("RBRACE", "Esperado '}'")
            return block

        else:
            raise ParserError(f"Token inesperado: {self.current_token}")

    def parse_print_statement(self):
        self.expect("KW_PRINT", "Esperado 'print'")
        self.expect("LPAREN", "Esperado '(' após print")

        args = []
        if self.current_token and self.current_token.tipo != "RPAREN":
            args.append(self.parse_expression())
            while self.current_token and self.current_token.tipo == "COMMA":
                self.advance()
                args.append(self.parse_expression())

        self.expect("RPAREN", "Esperado ')' após argumentos do print")
        return PrintNode(args)

    def safe_current_token_access(self, operation_name="operação"):
        """Verifica se current_token não é None antes de acessar seus atributos"""
        if self.current_token is None:
            raise ParserError(f"Fim inesperado dos tokens durante {operation_name}")
        return self.current_token
