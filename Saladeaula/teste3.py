'''3)Dada uma variável booleana chovendo e uma variável numérica temperatura (em °C),
construa a variável pode_passear que deve ser True quando NÃO estiver chovendo E a
temperatura for maior que 20 °C.'''
chovendo = False
temperatura = int(input("Digite a temperatura atual em graus °C: "))

pode_passear = (temperatura > 20) and (not chovendo)
print("Pode passear? ",pode_passear) 