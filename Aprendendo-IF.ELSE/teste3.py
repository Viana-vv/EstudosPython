import os 
'''Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.'''
def temperatura():
    while True:   
        try:
            temp = int(input('Defina a temperatura atual: '))    
            if temp > 25:
             print("ALERTA!! Temperatura acima do limite esperado!")     
             break
            else:
             print("Temperatura aceitavel.") 
             break
        except ValueError:
         print("Digite um valor valido para fazer a analise.") 
        return temperatura()  

def menu():
   print("OLa aqui você pode saber se está correta a temperatura: ")
   temperatura()

def main ():
    os.system('cls')
    menu()

if __name__ == "__main__":
    main()