import os
'''João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.'''

def nome_salvar():
     nome_user = input("Digite o nome do seu usuario (obs: o nome do usuario deve conter no minimo 5 caracteres):  ")
     if len(nome_user) >= 5:
        print("Usuario salvo com sucesso! ")
        return nome_user
     else: 
         print ("Nome de usuario invalido! Tente novamente. ")
         return nome_salvar()
     
def senha_salvar():
    senha_user = input("Digite a senha do seu suario (obs: a senha do usuario deve conter no minimo 8 caracteres):  ")
    if len(senha_user) >= 8:
          print("Senha salvacom sucesso! ")
          return senha_user
    else: 
          print ("Senha invalida! Tente novamente. ")
          return senha_salvar()
         
def usuario():
    while True:
     nome = nome_salvar()
     senha = senha_salvar()
     break
    print("Usuario cadastrado com sucesso!")

def menu():
    print("Bem-vindo ao sistema de cadastro!")
    usuario()

def main():
    os.system('cls')
    menu()

if __name__ == "__main__":
    main()
