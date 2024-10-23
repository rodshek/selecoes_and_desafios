import random


class DiceSimulator:
    def __init__(self):
        """
        Inicializa o simulador com um dicionário para armazenar o número de vezes
        que cada face do dado foi lançada.
        """
        self.results = {i: 0 for i in range(1, 7)}

    def roll_dice(self, rolls):
        """
        Realiza os lançamentos do dado e atualiza os resultados.

        :param rolls: Número de lançamentos a serem realizados.
        """
        for _ in range(rolls):
            result = random.randint(1, 6)
            self.results[result] += 1

    def get_statistics(self):
        """
        Retorna as estatísticas dos lançamentos, mostrando quantas vezes cada face foi lançada.
        """
        return self.results
