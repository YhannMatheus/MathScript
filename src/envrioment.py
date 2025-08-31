class Environment:
    def __init__(self, parent=None):
        self.variables = {}
        self.functions = {}
        self.parent = parent
    
    def define_variable(self, name, value):
        self.variables[name] = value
    
    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get_variable(name)
        else:
            raise NameError(f"Variável '{name}' não definida")
    
    def set_variable(self, name, value):
        if name in self.variables:
            self.variables[name] = value
        elif self.parent:
            self.parent.set_variable(name, value)
        else:
            raise NameError(f"Variável '{name}' não definida")
    
    def define_function(self, name, function_node):
        self.functions[name] = function_node
    
    def get_function(self, name):
        if name in self.functions:
            return self.functions[name]
        elif self.parent:
            return self.parent.get_function(name)
        else:
            raise NameError(f"Função '{name}' não definida")
    
    def child_scope(self):
        return Environment(parent=self)