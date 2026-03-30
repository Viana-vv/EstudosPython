import os 
'''Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. 
Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).'''

def definir_peso():
    while True: 
          try:
            peso = float(input("Digite seu peso em kg: "))
            if peso <= 0:
              print("Valor invalido por favor digite novamente.")
              return definir_peso()
            else:
              return peso
            break
          except ValueError:
            print("Valor invalido por favor digite novamente.")
            return definir_peso()
          
def definir_altura():
        while True: 
          try:
             altura = float(input("Digite sua altura em metros: "))
             if altura <= 0:
                print("Digite um valor valido!")
                return definir_altura()
             else:
               return altura
               break
          except ValueError:
            print("Valor invalido por favor digite novamente.")
            return definir_altura()

def definir_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
       print(f"Você está abaixo do peso, seu imc é: {imc:.2f}")
    elif 18.5 <= imc < 25 :
      print (f"Você está com um peso normal, seu imc é: {imc:.2f}")
    else:   
      print(f"Você está acima do peso, seu imc é:{imc:.2f}")

def main():
   os.system('cls')
   peso =  definir_peso()
   altura = definir_altura()
   definir_imc(peso, altura)


if __name__ == "__main__":
    main()