import unittest

from src.route_calculator import RouteCalculator


class TestRouteCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = RouteCalculator()

    def test_add_route(self):
        self.calculator.add_route("Cidade A", "Cidade B", 100)
        route, distance = self.calculator.calculate_shortest_route(
            "Cidade A", "Cidade B")
        self.assertEqual(route, ["Cidade A", "Cidade B"])
        self.assertEqual(distance, 100)

    def test_no_route(self):
        route, distance = self.calculator.calculate_shortest_route(
            "Cidade X", "Cidade Y")
        self.assertIsNone(route)
        self.assertIsNone(distance)

    def test_shortest_route(self):
        self.calculator.add_route("Cidade A", "Cidade B", 100)
        self.calculator.add_route("Cidade B", "Cidade C", 50)
        self.calculator.add_route("Cidade A", "Cidade C", 200)
        route, distance = self.calculator.calculate_shortest_route(
            "Cidade A", "Cidade C")
        self.assertEqual(route, ["Cidade A", "Cidade B", "Cidade C"])
        self.assertEqual(distance, 150)


if __name__ == '__main__':
    unittest.main()
