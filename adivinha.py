from random import randint
pc = randint(0,10)
print('Sou seu PC... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual é? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...')
        if jogador > pc:
            print('Menos...')
print(f'\nAcertou com {palpites} tentativas!')