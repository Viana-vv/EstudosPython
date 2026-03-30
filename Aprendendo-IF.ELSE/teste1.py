import os
'''Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.'''




# Recebe o número de vendas dos dois produtos
def numero_de_maca(): 
    while True:         
        try:
              macas_vendidas = int(input("Digite o numero de maçãs vendidas: "))
              print("Valor das maçãs foram salvos! ")
              return macas_vendidas
              break
        except ValueError:
                print("Você digitou uma letra por favor digite apenas números ")
                return numero_de_maca()
                break

def numero_de_bananas():
    while True:
         try:
             bananas_vendidas = int(input("Digite o numero de bananas vendidas: "))
             print("Valor das bananas foram salvos! ")
             return bananas_vendidas
             break
         except ValueError:
            print("Você digitou ma letra por favor digite apenas números ")
            return numero_de_bananas()
            break

def menu():
      print("Olá Bruno aqui você pode ver qual produto teve mais saidas:  ")
      maca = numero_de_maca()
      banana = numero_de_bananas()
      if maca < banana:
           print("O número de maçãs é menor! ") 
      elif maca > banana:
           print("O número de bananas é menor! ") 
      else:
            print("Os numeros são exatos, houve um empate!")


def main():
      os.system('cls')
      menu()


if __name__ == "__main__":
    main()