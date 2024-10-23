def validate_input(prompt, expected_type):
    """
    Valida a entrada do usuário de acordo com o tipo esperado.
    """
    while True:
        try:
            return expected_type(input(prompt))
        except ValueError:
            print(
                f"Entrada inválida. Por favor, insira um valor do tipo {expected_type.__name__}.")
