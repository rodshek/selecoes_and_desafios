import unittest

from src.voting_system import VotingSystem


class TestVotingSystem(unittest.TestCase):

    def setUp(self):
        self.system = VotingSystem()

    def test_vote(self):
        self.system.vote("Candidato A")
        self.system.vote("Candidato A")
        self.system.vote("Candidato B")
        results = self.system.get_results()
        self.assertEqual(results["Candidato A"], 2)
        self.assertEqual(results["Candidato B"], 1)

    def test_get_results_empty(self):
        results = self.system.get_results()
        self.assertEqual(results, {})

    def test_get_results(self):
        self.system.vote("Candidato A")
        self.system.vote("Candidato B")
        results = self.system.get_results()
        self.assertEqual(results["Candidato A"], 1)
        self.assertEqual(results["Candidato B"], 1)


if __name__ == '__main__':
    unittest.main()
