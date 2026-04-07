import os

"""Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";

Entre 12h e 18h, exibir "Boa tarde";

Após 18h, exibir "Boa noite".

"""

def resposta():
    resposta_horas = int(input("Defina o horario atual, digite apenas números "))
    if resposta_horas < 12:
        print("Bom dia!")
    elif resposta_horas > 12 and resposta_horas < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
def menu():
    print("Bem-vindo ao sistema de atendimento!")
    resposta()

def main():
    os.system('cls')
    menu()

if __name__ == "__main__":
    main()
