'''2)Dados dois números inteiros a e b, crie uma expressão booleana soma_par_e_maior que
retorne True apenas se a soma de a + b for um número par E o valor de a for estritamente
maior do que b.'''
a = int(input("Digite um núnero inteiro: "))
b = int(input("Digite outro número inteiro: "))
resultado = a + b

soma_par_e_maior = (resultado % 2 == 0) and a > b
print("É par? e é a>b?  ", soma_par_e_maior) 