import os

def produto():
    lista_de_valores = []
    while True:
        try:
            valor = float(input("Digite o valor da despesa: "))
            if valor < 0:
                print("Valor inválido. Por favor, digite novamente.")
                continue
            lista_de_valores.append(valor)
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")
            continue

        continuar = input("Digite 'Sim' para continuar ou 'Nao' para parar: ").lower()
        if continuar == "nao":
            break
    return lista_de_valores

def somar_produtos(produtos):
    total = sum(produtos)
    if total > 3000:
        print(f"Você ultrapassou o limite, seu total é: R$ {total:.2f}")
    else:
        print(f"Você está dentro do orçamento, seu total é: R$ {total:.2f}")

def main():
    os.system('cls') 
    produtos = produto()
    somar_produtos(produtos)

if __name__ == "__main__":
    main()
