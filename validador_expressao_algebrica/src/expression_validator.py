class ExpressionValidator:
    def __init__(self):
        # Define os pares de símbolos de abertura e fechamento
        self.opening = "({["
        self.closing = ")}]"
        self.pairs = {")": "(", "}": "{", "]": "["}

    def validate(self, expression):
        """
        Valida se a expressão algébrica tem parênteses, colchetes e chaves balanceados.
        """
        stack = []

        for char in expression:
            if char in self.opening:
                stack.append(char)
            elif char in self.closing:
                if not stack or stack[-1] != self.pairs[char]:
                    return False
                stack.pop()

        # Se a pilha estiver vazia, a expressão é válida
        return len(stack) == 0
