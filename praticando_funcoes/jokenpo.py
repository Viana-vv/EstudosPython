'''Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.'''

import random

def escolha_usuario():
        escolha = input("Escolha entre pedra, papel ou tesoura: ").lower()
        try:
            if escolha in ["pedra", "papel", "tesoura"]:
                return escolha
            else:
                print("Escolha inválida. Tente novamente.")
                return escolha_usuario()
        except ValueError:
              print("Escolha inválida. Tente novamente.")
              return escolha_usuario()
        
def obter_escolha_usuario():
    escolha_usuario_result  = escolha_usuario()
    return escolha_usuario_result


def obter_escolha_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra"):
        return "Usuário"
    else:
        return "Computador"

def main():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    while True:
        escolha_usuario = obter_escolha_usuario()
        escolha_computador = obter_escolha_computador()
        vencedor = determinar_vencedor(escolha_usuario, escolha_computador)
        print(f"Você escolheu: {escolha_usuario}")
        print(f"O computador escolheu: {escolha_computador}")
        if vencedor == "Empate":
            print("A partida terminou em empate!")
        else:
            print(f"O {vencedor} venceu a partida!")
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            break

if __name__ == "__main__":
    main()