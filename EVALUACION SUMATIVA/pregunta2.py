class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_expression_tree(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  # Es un número
            stack.append(Node(int(token)))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Expresión inválida: faltan operandos.")
            right = stack.pop()
            left = stack.pop()
            new_node = Node(token)
            new_node.left = left
            new_node.right = right
            stack.append(new_node)
        else:
            raise ValueError(f"Operador desconocido: {token}")

    if len(stack) != 1:
        raise ValueError("Expresión inválida: demasiados operandos.")

    return stack[0]  # Raíz del árbol

def evaluate_tree(node):
    if node.left is None and node.right is None:
        return node.value

    left_value = evaluate_tree(node.left)
    right_value = evaluate_tree(node.right)

    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        if right_value == 0:
            raise ZeroDivisionError("Error: División por cero.")
        return left_value / right_value

# Función para imprimir el árbol (para depuración)
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        print_tree(node.left, level + 1, "L--> ")
        print_tree(node.right, level + 1, "R--> ")

# Expresión en notación postfija (RPN)
expression = "3 5 2 8 - * +"  # Equivalente a "3 + 5 * (2 - 8)"
tree = construct_expression_tree(expression)

# Imprimir el árbol para verificar su estructura
print("Árbol de expresión:")
print_tree(tree)

# Evaluar la expresión
print("Resultado:", evaluate_tree(tree))
