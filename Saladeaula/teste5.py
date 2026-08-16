'''5) Um ano é considerado bissexto se cumprir a regra matemática:
1. É divisível por 4 E não é divisível por 100; OU
2. É divisível por 400.
Crie uma expressão booleana em Python armazenada na variável eh_bissexto que valide
um ano inteiro ano.'''
ano = int(input("Digite o ano atual: "))
eh_bissexto = (ano % 4 == 0) and (ano % 100 != 0 ) or (ano % 400 == 0)
print("É um ano bissexto? ", eh_bissexto)