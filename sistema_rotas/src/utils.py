def validate_input(prompt, expected_type):
    """
    Valida a entrada do usuário de acordo com o tipo esperado.

    :param prompt: Mensagem para o input do usuário.
    :param expected_type: Tipo de dado esperado (por exemplo, float).
    :return: A entrada validada do tipo esperado.
    """
    while True:
        try:
            return expected_type(input(prompt))
        except ValueError:
            print(
                f"Entrada inválida. Por favor, insira um valor do tipo {expected_type.__name__}.")
