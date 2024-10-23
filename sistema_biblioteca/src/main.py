from library_management import LibraryManagement
from utils import validate_input

# Resumo do Desafio 06:
# Este script fornece uma interface para gerenciar o sistema de biblioteca, permitindo
# a adição de livros, a realização de empréstimos e a devolução de livros.


def main():
    library = LibraryManagement()

    while True:
        print("\nSistema de Biblioteca")
        print("1. Adicionar livro ao catálogo")
        print("2. Listar livros")
        print("3. Realizar empréstimo")
        print("4. Devolver livro")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            title = input("Título do livro: ")
            author = input("Autor do livro: ")
            library.add_book(title, author)
            print(f"Livro '{title}' adicionado ao catálogo.")
        elif choice == '2':
            books = library.list_books()
            print("\nCatálogo de Livros:")
            for book in books:
                print(
                    f"{book['id']}: {book['title']} - {book['author']} (Disponível: {book['available']})")
        elif choice == '3':
            book_id = validate_input("ID do livro para empréstimo: ", int)
            borrower = input("Nome do usuário: ")
            if library.borrow_book(book_id, borrower):
                print("Empréstimo realizado com sucesso.")
            else:
                print(
                    "Erro ao realizar empréstimo. Verifique se o livro está disponível.")
        elif choice == '4':
            book_id = validate_input("ID do livro para devolução: ", int)
            if library.return_book(book_id):
                print("Livro devolvido com sucesso.")
            else:
                print("Erro ao realizar devolução. Verifique o ID do livro.")
        elif choice == '5':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script oferece uma interface interativa para o usuário, permitindo o gerenciamento de um catálogo de livros.
# Ele interage com o módulo library_management para gerenciar empréstimos, devoluções e adições ao catálogo.
