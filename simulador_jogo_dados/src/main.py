from dice_simulator import DiceSimulator
from utils import validate_input

# Resumo do Desafio 09:
# Este script oferece um simulador de jogo de dados onde os jogadores podem lançar um dado de 6 faces
# e ver as estatísticas dos lançamentos.


def main():
    simulator = DiceSimulator()

    while True:
        print("\nSimulador de Jogo de Dados")
        print("1. Lançar dado")
        print("2. Exibir estatísticas")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            rolls = validate_input("Quantas vezes deseja lançar o dado? ", int)
            simulator.roll_dice(rolls)
            print(f"{rolls} lançamentos realizados.")
        elif choice == '2':
            stats = simulator.get_statistics()
            print("\nEstatísticas de Lançamentos:")
            for face, count in stats.items():
                print(f"Face {face}: {count} vezes")
        elif choice == '3':
            print("Saindo do simulador de dados.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script principal oferece uma interface para o usuário lançar os dados várias vezes e ver as estatísticas.
# Ele utiliza o módulo dice_simulator para realizar a simulação dos lançamentos.
