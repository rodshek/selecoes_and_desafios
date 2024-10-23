from password_generator import PasswordGenerator
from utils import validate_input

# Resumo do Desafio 12:
# Este script permite ao usuário gerar senhas seguras, personalizando critérios como comprimento,
# e a inclusão de letras maiúsculas, minúsculas, números e caracteres especiais.


def main():
    generator = PasswordGenerator()

    print("Bem-vindo ao Gerador de Senhas!")

    while True:
        try:
            length = validate_input("Digite o comprimento da senha: ", int)
            include_uppercase = validate_input(
                "Incluir letras maiúsculas? (s/n): ", str).lower() == 's'
            include_numbers = validate_input(
                "Incluir números? (s/n): ", str).lower() == 's'
            include_special = validate_input(
                "Incluir caracteres especiais? (s/n): ", str).lower() == 's'

            password = generator.generate_password(
                length, include_uppercase, include_numbers, include_special)
            print(f"Senha gerada: {password}")

            another = validate_input("Gerar outra senha? (s/n): ", str).lower()
            if another != 's':
                break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script principal oferece uma interface para gerar senhas seguras personalizadas de acordo com os
# critérios do usuário. A função validate_input é usada para garantir a entrada correta, enquanto o
# PasswordGenerator lida com a lógica da criação da senha.
