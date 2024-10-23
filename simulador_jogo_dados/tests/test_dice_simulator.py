import unittest

from src.dice_simulator import DiceSimulator


class TestDiceSimulator(unittest.TestCase):

    def setUp(self):
        self.simulator = DiceSimulator()

    def test_initial_statistics(self):
        # Verifica se as estatísticas iniciais são todas zero
        stats = self.simulator.get_statistics()
        for value in stats.values():
            self.assertEqual(value, 0)

    def test_roll_dice(self):
        # Simula 100 lançamentos de dados
        self.simulator.roll_dice(100)
        stats = self.simulator.get_statistics()
        total_rolls = sum(stats.values())
        self.assertEqual(total_rolls, 100)


if __name__ == '__main__':
    unittest.main()
