from expression_validator import ExpressionValidator

# Resumo do Desafio 05:
# Este script permite a validação de expressões algébricas com parênteses, colchetes e chaves.
# O usuário insere uma expressão, e o sistema verifica se ela é válida.


def main():
    validator = ExpressionValidator()

    while True:
        expression = input(
            "Insira uma expressão algébrica (ou 'sair' para finalizar): ")

        if expression.lower() == 'sair':
            print("Encerrando o programa.")
            break

        if validator.validate(expression):
            print("A expressão é válida.")
        else:
            print("A expressão é inválida.")


if __name__ == "__main__":
    main()

# Explicação:
# O script principal permite que o usuário insira expressões e utiliza a classe ExpressionValidator para verificar se a sintaxe
# está correta, garantindo que os parênteses, colchetes e chaves estão balanceados e na ordem correta.
