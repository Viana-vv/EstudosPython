import os

def cpf():
    cpf_digitado = input("Digite seu CPF: ")
    try:
        if not cpf_digitado.isdigit():
            print("CPF deve conter apenas números, tente novamente!")
            return cpf()
        elif len(cpf_digitado) != 11:
            print("CPF deve conter 11 dígitos, tente novamente!")
            return cpf()
        elif int(cpf_digitado) < 0:
            print("CPF não pode ser negativo, tente novamente!")
            return cpf()
        else:
            print("CPF válido!")
    except ValueError:
        print("Você não pode digitar letras, tente novamente!")
        return cpf()

def menu():
    cpf()

def main():
    os.system('cls')  # no Windows; em Linux/Mac seria 'clear'
    menu()

if __name__ == "__main__":
    main()
