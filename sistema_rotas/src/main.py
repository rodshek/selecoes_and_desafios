from route_calculator import RouteCalculator
from utils import validate_input

# Resumo do Desafio 10:
# Este script oferece um sistema que calcula a rota mais curta entre cidades utilizando o algoritmo de Dijkstra.


def main():
    calculator = RouteCalculator()

    while True:
        print("\nSistema de Rotas")
        print("1. Adicionar rota entre duas cidades")
        print("2. Calcular rota mais curta")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            city1 = input("Nome da primeira cidade: ")
            city2 = input("Nome da segunda cidade: ")
            distance = validate_input(
                "Distância entre as cidades (em km): ", float)
            calculator.add_route(city1, city2, distance)
            print(f"Rota adicionada: {city1} <-> {city2} ({distance} km)")
        elif choice == '2':
            start = input("Cidade de partida: ")
            end = input("Cidade de destino: ")
            route, total_distance = calculator.calculate_shortest_route(
                start, end)
            if route:
                print(
                    f"Rota mais curta de {start} até {end}: {' -> '.join(route)} ({total_distance} km)")
            else:
                print(
                    f"Não foi possível encontrar uma rota entre {start} e {end}.")
        elif choice == '3':
            print("Saindo do sistema de rotas.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script principal oferece uma interface para o usuário adicionar rotas entre cidades e calcular a rota
# mais curta entre duas cidades utilizando o algoritmo de Dijkstra.
