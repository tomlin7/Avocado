from nodes import *
from values import Number


class Interpreter:
    @staticmethod
    def to_method_name(classname):
        return ''.join(['_' + i.lower() if i.isupper() else i for i in classname]).lstrip('_')

    def visit(self, node):
        # print(self.to_method_name(type(node).__name__))
        method_name = f"visit_{self.to_method_name(type(node).__name__)}"
        method = getattr(self, method_name)
        return method(node)

    def visit_number_node(self, node):
        return Number(node.value)

    def visit_add_node(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_subtract_node(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_multiply_node(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_divide_node(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_floor_divide_node(self, node):
        try:
            return Number(self.visit(node.node_a).value // self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_exponent_node(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_modulus_node(self, node):
        return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)

    def visit_plus_node(self, node):
        return self.visit(node.node)

    def visit_minus_node(self, node):
        return Number(-self.visit(node.node).value)
