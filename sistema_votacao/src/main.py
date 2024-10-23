from utils import validate_input
from voting_system import VotingSystem

# Resumo do Desafio 08:
# Este script oferece um sistema de votação onde os usuários podem votar e visualizar os resultados em tempo real.


def main():
    system = VotingSystem()

    while True:
        print("\nSistema de Votação")
        print("1. Votar em um candidato")
        print("2. Exibir resultado da votação")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            candidate = input("Nome do candidato: ")
            system.vote(candidate)
            print(f"Voto registrado para '{candidate}'.")
        elif choice == '2':
            results = system.get_results()
            print("\nResultado da votação:")
            for candidate, votes in results.items():
                print(f"{candidate}: {votes} votos")
        elif choice == '3':
            print("Saindo do sistema de votação.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script principal oferece uma interface para o sistema de votação. Ele permite que os usuários votem em
# candidatos e vejam o resultado acumulado em tempo real.
