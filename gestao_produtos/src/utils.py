def validate_input(prompt, expected_type, optional=False):
    """
    Valida a entrada do usuário de acordo com o tipo esperado.

    :param prompt: Mensagem para o input do usuário.
    :param expected_type: Tipo de dado esperado (por exemplo, float).
    :param optional: Se o campo é opcional (pode ser deixado em branco).
    :return: A entrada validada do tipo esperado.
    """
    while True:
        user_input = input(prompt)
        if optional and user_input == "":
            return None
        try:
            return expected_type(user_input)
        except ValueError:
            print(
                f"Entrada inválida. Por favor, insira um valor do tipo {expected_type.__name__}.")
