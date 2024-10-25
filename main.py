import random

numero_secreto = random.randint(1, 10)
tentativas = 1

print('Bem-vindo ao jogo do número secreto')
print('LEMBRETE: Você tem apenas 3 chances para acertar um número de 1 a 10')

while True:
    chute = int(input('Digite um número de 1 a 10: '))

    if chute == numero_secreto:
        tentativa_str = "tentativa" if tentativas == 1 else "tentativas"
        print(f'Acertou! O número secreto é {numero_secreto}')
        print(f'Você acertou em {tentativas} {tentativa_str}')
        break
    elif chute > numero_secreto:
        print('O número secreto é menor')
    else:
        print('O número secreto é maior')
    
    tentativas += 1

    if tentativas > 3:
        print('GAME OVER. Você não tem mais chances')
        decisao = input('Você deseja continuar o jogo? (Sim/Não) ').strip().lower()

        if decisao == 'não':
            print('Encerrando o jogo... até a próxima')
            break
        else:
            numero_secreto = random.randint(1, 10)
            tentativas = 1
            print('Um novo número secreto foi sorteado. Vamos jogar novamente!')