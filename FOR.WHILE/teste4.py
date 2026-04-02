livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    print(f"Livros: {livro}")

def digite_livro():
    livro_escolhido =input("Digite o nome do livro que deseja encontrar: ")
    return livro_escolhido

for livro in livros:
    if livro == digite_livro():
        print(f"Encontrado: {livro}")
    else:
        print(f"Livro não encontrado: {livro}")