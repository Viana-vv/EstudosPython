idade = 20
saida="Maior de idade" if idade >= 18 else "Menor de idade"
print(saida)

status_conta = "ativo"
pontos = 120
nivel="VIP"if pontos >= 100 else "Padrão"
print(nivel)

produtos=float(input("Digite o valor dos produtos R$ "))
tipocli=input("Digite o  tipo de cliente (VIP/Comum): ")

if produtos > 500:
    if tipocli == 'VIP':
        desconto=produtos*0.2
    else:
        desconto=produtos*0.1

elif produtos >=200 :
    if tipocli == 'VIP':
        desconto=produtos*0.1
    else:
        desconto=produtos*0.5
else:
    desconto= 0

print("O valor do desconto é: ", desconto)