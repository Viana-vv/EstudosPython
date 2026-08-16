'''1) Escreva um programa em Python que receba um número float x e verifique se ele está
estritamente entre 10 e 100 (sem incluir os extremos 10 e 100). Armazene o resultado em
uma variável booleana esta_no_intervalo e exiba o resultado.'''

numero = float(input("Digite um número ente 10 e 100: "))
expressao_booleana = (numero > 10 and numero < 100)  
print("O resultado é: ", expressao_booleana)