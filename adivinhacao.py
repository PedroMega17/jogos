import random
def jogar():

    print('*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************')

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print('Níveis de dificuldade')
    print('(1) Fácil (2) Médio (3) Difícil')

    while True:
        nivel = int(input('Defina o nível: '))

        if (nivel == 1):
            total_de_tentativas = 20
            break
        elif (nivel == 2):
            total_de_tentativas = 10
            break
        elif (nivel == 3):
            total_de_tentativas = 5
            break
        else:
            print('Escolha um nível existente')
            continue

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_str = input('Digite um número entre 1 e 100: ')
        print('Voce digitou', chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100:')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f'Você acertou! Você fez {pontos} pontos!')
            break
        else:
            if (maior):
                print('Você errou! Número maior que o número secreto.')
            elif (menor):
                print('Você errou! Número menor que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('O número secreto é', numero_secreto)
    print('Fim do jogo')

if (__name__ == "__main__"):
    jogar()
