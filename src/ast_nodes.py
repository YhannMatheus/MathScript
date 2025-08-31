# Arquivo de definição dos nós da AST
# Arquivo de definição dos nós da AST
from dataclasses import dataclass
from typing import List, Optional

# Nós da AST

@dataclass
class ASTNode:
    pass

@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode]

@dataclass
class VariableDeclarationNode(ASTNode):
    var_type: str
    var_name: str
    value: ASTNode

@dataclass
class AssignmentNode(ASTNode):
    var_name: str
    op: str
    value: ASTNode

@dataclass
class FunctionNode(ASTNode):
    name: str
    params: List[str]
    body: ASTNode

@dataclass
class FunctionCallNode(ASTNode):
    name: str
    args: List[ASTNode]

@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode]

@dataclass
class IfNode(ASTNode):
    condition: ASTNode
    then_block: ASTNode

@dataclass
class BinaryOpNode(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

@dataclass
class UnaryOpNode(ASTNode):
    op: str
    expr: ASTNode

@dataclass
class VariableNode(ASTNode):
    name: str

@dataclass
class NumberNode(ASTNode):
    value: float

@dataclass
class StringNode(ASTNode):
    value: str

@dataclass
class BooleanNode(ASTNode):
    value: bool

@dataclass
class SetNode(ASTNode):
    elements: List[ASTNode]

@dataclass
class PrintNode(ASTNode):
    args: List[ASTNode]