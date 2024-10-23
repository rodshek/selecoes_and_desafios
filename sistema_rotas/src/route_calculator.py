import networkx as nx


class RouteCalculator:
    def __init__(self):
        """
        Inicializa o sistema de rotas com um grafo vazio.
        """
        self.graph = nx.Graph()

    def add_route(self, city1, city2, distance):
        """
        Adiciona uma rota entre duas cidades no grafo.

        :param city1: Nome da primeira cidade.
        :param city2: Nome da segunda cidade.
        :param distance: Distância entre as cidades.
        """
        self.graph.add_edge(city1, city2, weight=distance)

    def calculate_shortest_route(self, start, end):
        """
        Calcula a rota mais curta entre duas cidades usando o algoritmo de Dijkstra.

        :param start: Cidade de partida.
        :param end: Cidade de destino.
        :return: Rota mais curta e a distância total.
        """
        try:
            shortest_path = nx.dijkstra_path(
                self.graph, start, end, weight='weight')
            total_distance = nx.dijkstra_path_length(
                self.graph, start, end, weight='weight')
            return shortest_path, total_distance
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None, None
