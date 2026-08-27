'''Aprendendo e treinando leetcode

Crie um JSON com informações de um filme (ex: nome, gênero, nota).

Converta para dicionário em Python.

Acesse os valores e imprima frases como:
"O filme X é do gênero Y e tem nota Z."
'''
import json
textJsonJogo = '{"Nome": "X-MAN", "GENERO": "Ação", "NOTA": 9.00}'
dicionario = json.loads(textJsonJogo)
nome = dicionario["Nome"]
genero = dicionario["GENERO"]
nota = dicionario["NOTA"]

print(f'O filme escolhido é {nome} do genero {genero} com a nota {nota}')


'''Exercício 1 - Escreva um programa que imprima todos os números inteiros de 1 a 15
utilizando o laço while.'''
n = 1
while n != 15:
    if n == 1:
        print(n)
    n += 1
    print (n)
print ("Fim")

'''Exercício 2 - Solicite ao usuário um número inteiro e exiba a tabuada desse número de 1 a
10 utilizando while.'''

inteiro = int(input("Digite um número inteiro: "))
m = 1 
while m <= 10:
    result= m*inteiro
    print(result)
    m += 1

print ('fim')

'''
Exercício 3 - Crie um programa que mantenha uma senha cadastrada python123. Peça ao
usuário para digitar a senha e continue solicitando até que a senha digitada seja igual à
cadastrada.
'''
senhaCadastrada = "python123"
senhaDigitada = input("Digite a senha: ")
while senhaDigitada != senhaCadastrada:
    senhaDigitada = input("Digite a senha: ")
print("Senha correta!")

'''Exercício 4 - Exiba todos os números pares de 2 até 20 na tela utilizando o laço while.'''
numerosPares = 20
while numerosPares != 1:
    if numerosPares % 2 == 0:
        print(numerosPares)
    numerosPares-=1
print('fim numeros pares')

