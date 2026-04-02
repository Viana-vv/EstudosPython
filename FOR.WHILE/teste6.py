'''Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
'''

for i in range(10,0,-1):
 if  i % 2 == 0:
     print (f"Faltam apenas {i} segundos - Não perca essa oportunidade!")
 else: 
    print ( f"A contagem continua: {i} segundos restantes.")
print("A contagem acabou!")