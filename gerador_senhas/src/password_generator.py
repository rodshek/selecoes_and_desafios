import random
import string


class PasswordGenerator:
    def __init__(self):
        """
        Inicializa o gerador de senhas com os conjuntos de caracteres disponíveis.
        """
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = "!@#$%^&*()"

    def generate_password(self, length, include_uppercase=False, include_numbers=False, include_special=False):
        """
        Gera uma senha com base nos critérios fornecidos.

        :param length: Comprimento da senha.
        :param include_uppercase: Se deve incluir letras maiúsculas.
        :param include_numbers: Se deve incluir números.
        :param include_special: Se deve incluir caracteres especiais.
        :return: A senha gerada.
        """
        if length < 1:
            raise ValueError("O comprimento da senha deve ser pelo menos 1.")

        characters = self.lowercase
        if include_uppercase:
            characters += self.uppercase
        if include_numbers:
            characters += self.digits
        if include_special:
            characters += self.special

        if not characters:
            raise ValueError(
                "Nenhum conjunto de caracteres selecionado para gerar a senha.")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password
