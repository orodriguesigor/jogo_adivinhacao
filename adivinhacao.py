import random #importando o random para que ele me gere números aleatórios

def jogar_adivinhacao(): #difinindo a função que vai fazer o jogo rodar

    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Bem vindo ao jogo de Adivinhação")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    #Gerando um número aleatório com range de 1 a 100

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) fácil  (2) Médio (3) Difícil")

    #Trouxe uma condição e um input para que o jogador possa escolher seu nível o jogo dar um nº de tentativas

    nivel = int(input("Defina um nível:  "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

        # Adicionando uma estrutura de repetição / laço


    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute = input("Digite o seu chute"  )
        print("você digitou", chute)
        chute = int(chute)

        if(chute < 1 or chute >=100):
            print("Chute um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("ACERTOU, MISERAVI! Você fez {} pontos" .format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute) #Pega o numero secreto e diminui pelo chute para dar uma pontuação ao jogador
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            if(rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

    print("FIM DO JOGO")

if __name__: #Adiciono um if para caso eu queira rodar esse jogo sozinho, sem ser dentro do meu códio com menu de jogos
    jogar_adivinhacao()