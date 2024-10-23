def validate_input(prompt, expected_type):
    """
    Valida a entrada do usuário com base no tipo esperado.

    :param prompt: A mensagem exibida ao solicitar a entrada do usuário.
    :param expected_type: O tipo esperado da entrada (por exemplo, int).
    :return: O valor validado.
    """
    while True:
        try:
            user_input = input(prompt)
            return expected_type(user_input)
        except ValueError:
            print(
                f"Por favor, insira um valor válido do tipo {expected_type.__name__}.")
