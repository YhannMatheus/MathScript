# Arquivo do interpretador MathScript
from src.ast_nodes import *
from src.envrioment import Environment
from src.errors import RuntimeError

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
    
    def interpret(self, node):
        if isinstance(node, PrintNode):
            return self.visit_print(node)
        elif isinstance(node, ProgramNode):
            return self.visit_program(node)
        elif isinstance(node, VariableDeclarationNode):
            return self.visit_variable_declaration(node)
        elif isinstance(node, AssignmentNode):
            return self.visit_assignment(node)
        elif isinstance(node, FunctionNode):
            return self.visit_function_definition(node)
        elif isinstance(node, FunctionCallNode):
            return self.visit_function_call(node)
        elif isinstance(node, BlockNode):
            return self.visit_block(node)
        elif isinstance(node, IfNode):
            return self.visit_if(node)
        elif isinstance(node, BinaryOpNode):
            return self.visit_binary_op(node)
        elif isinstance(node, UnaryOpNode):
            return self.visit_unary_op(node)
        elif isinstance(node, VariableNode):
            return self.visit_variable(node)
        elif isinstance(node, NumberNode):
            return self.visit_number(node)
        elif isinstance(node, StringNode):
            return self.visit_string(node)
        elif isinstance(node, BooleanNode):
            return self.visit_boolean(node)
        elif isinstance(node, SetNode):
            return self.visit_set(node)
        else:
            raise RuntimeError(f"Tipo de nó desconhecido: {type(node)}")
    
    def visit_print(self, node):
        output = ""
        for arg in node.args:
            value = self.interpret(arg)
            output += str(value) + " "
    
        # Remove o último espaço e imprime
        print(output.strip())
        return None
    
    def visit_program(self, node):
        result = None
        for statement in node.statements:
            result = self.interpret(statement)
        return result
    
    def visit_variable_declaration(self, node):
        value = self.interpret(node.value)
        self.global_env.define_variable(node.var_name, value)
        return value
    
    def visit_assignment(self, node):
        value = self.interpret(node.value)
        current_value = self.global_env.get_variable(node.var_name)
        
        if node.op == ":=":
            result = value
        elif node.op == "+=":
            result = current_value + value
        elif node.op == "-=":
            result = current_value - value
        elif node.op == "*=":
            result = current_value * value
        elif node.op == "/=":
            result = current_value / value
        elif node.op == "**=":
            result = current_value ** value
        elif node.op == "//=":
            result = current_value // value
        elif node.op == "%=":
            result = current_value % value
        else:
            raise RuntimeError(f"Operador de atribuição inválido: {node.op}")
        
        self.global_env.set_variable(node.var_name, result)
        return result
    
    def visit_function_definition(self, node):
        self.global_env.define_function(node.name, node)
        return None
    
    def visit_function_call(self, node):
        function_node = self.global_env.get_function(node.name)
        if not function_node:
            raise RuntimeError(f"Função '{node.name}' não definida")
        
        # Avaliar argumentos
        args = [self.interpret(arg) for arg in node.args]
        
        # Criar novo escopo para a função
        old_env = self.global_env
        self.global_env = Environment(parent=old_env)
        
        # Definir parâmetros no novo escopo
        for param_name, arg_value in zip(function_node.params, args):
            self.global_env.define_variable(param_name, arg_value)
        
        # Executar corpo da função
        result = self.interpret(function_node.body)
        
        # Restaurar escopo anterior
        self.global_env = old_env
        
        return result
    
    def visit_block(self, node):
        result = None
        for statement in node.statements:
            result = self.interpret(statement)
        return result
    
    def visit_if(self, node):
        condition = self.interpret(node.condition)
        if condition:
            return self.interpret(node.then_block)
        return None
    
    def visit_binary_op(self, node):
        left = self.interpret(node.left)
        right = self.interpret(node.right)
        
        if node.op == "+":
            return left + right
        elif node.op == "-":
            return left - right
        elif node.op == "*":
            return left * right
        elif node.op == "/":
            return left / right
        elif node.op == "**":
            return left ** right
        elif node.op == "//":
            return left // right
        elif node.op == "%":
            return left % right
        elif node.op == "==":
            return left == right
        elif node.op == "!=":
            return left != right
        elif node.op == "<":
            return left < right
        elif node.op == ">":
            return left > right
        elif node.op == "<=":
            return left <= right
        elif node.op == ">=":
            return left >= right
        elif node.op == "and":
            return left and right
        elif node.op == "or":
            return left or right
        elif node.op == "xor":
            return left != right
        elif node.op == "xand":
            return left == right
        elif node.op == "xnot":
            return not (left == right)
        else:
            raise RuntimeError(f"Operador binário desconhecido: {node.op}")
    
    def visit_unary_op(self, node):
        expr = self.interpret(node.expr)
        
        if node.op == "not":
            return not expr
        elif node.op == "-":
            return -expr
        elif node.op == "+":
            return +expr
        else:
            raise RuntimeError(f"Operador unário desconhecido: {node.op}")
    
    def visit_variable(self, node):
        return self.global_env.get_variable(node.name)
    
    def visit_number(self, node):
        return node.value
    
    def visit_string(self, node):
        return node.value
    
    def visit_boolean(self, node):
        return node.value
    
    def visit_set(self, node):
        return [self.interpret(elem) for elem in node.elements]