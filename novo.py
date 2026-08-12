import random 
print('testando como gerar senhas: ')
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTYVWXYZ'
number = '123456789'
caracter = '(){}[]*&%$#@!'

sort = lower + upper + number + caracter

password = ''.join(random.sample(sort, 8))
if len(password) < 8:
            password += random.choice(sort)
            

print(password)

