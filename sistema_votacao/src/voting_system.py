class VotingSystem:
    def __init__(self):
        """
        Inicializa o sistema de votação com um dicionário vazio para armazenar os votos.
        """
        self.votes = {}

    def vote(self, candidate):
        """
        Registra um voto para um candidato. Se o candidato ainda não tiver votos,
        inicializa seu contador com 1. Caso contrário, incrementa seu número de votos.
        """
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            self.votes[candidate] = 1

    def get_results(self):
        """
        Retorna o resultado da votação como um dicionário de candidatos e seus respectivos votos.
        """
        return self.votes
