import os
'''Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.'''

# Recebe o número de dias das três atividades
def primeiro_numero():
    while True:
       try:
            num1 = int(input("Digite os dias da primeira atividade: "))
            if(num1 < 0 ):
                    print("Digite um valor valido por favor!")
                    return primeiro_numero() 
            else:
                print("Dias salvos")
                return num1
            break
       except ValueError:
           print("Digite um valor valido por favor!")
           return primeiro_numero()
         
def segundo_numero():
    while True:
       try:
            num2 = int(input("Digite os dias da segunda atividade: "))
            if(num2 < 0 ):
                    print("Digite um valor valido por favor!")
                    return segundo_numero() 
            else:
                print("Dias salvos")
                return num2
            break 
       except ValueError:
           print("Digite um valor valido por favor!")
           return segundo_numero()                     

def terceiro_numero():
    while True:
       try:
            num3 = int(input("Digite os dias da terceira atividade: "))
            if (num3 < 0 ):
                    print("Digite um valor valido por favor!")
                    return terceiro_numero() 
            else:
                print("Dias salvos")
                return num3
            break 
       except ValueError:
           print("Digite um valor valido por favor!")
           return terceiro_numero()  

def somar():   
    primeiro = primeiro_numero()
    segundo = segundo_numero()
    terceiro = terceiro_numero()                
    somando = primeiro + segundo + terceiro 
    return somando

def menu():
    print("Olá Camila estou aqui para te ajudar.. ")
    soma = somar()
    print(f"Os dias totais são {soma} de atividades.")



def main ():
    os.system('cls')
    menu()


if __name__ == "__main__":
    main()
