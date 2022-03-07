def jogo():
    x = 0
    while x != 1 and x != 2:
        print('1 - para jogar uma partida isolada')
        x = int(input('2 - para jogar um campeonato '))
    print()
    if x == 1:
        print('Você escolheu uma partida!')
        print()
        partida()
    else:
        print('Você escolheu um campeonato!')
        print()
        campeonato()

def partida():
    n = int(input('Quantas peças? '))
    if n <=0:
        print('Quantidade de peças deve ser maior do que zero!')
        n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if m == 0:
        print('Limite de peças por jogada não pode ser zero!')
        m = int(input('Limite de peças por jogada? '))
    if m > n:
        print('Limite de peças por jogada não pode ser maior que quantidade de peças!')
        m = int(input('Limite de peças por jogada? '))
    multiplo = n % (m + 1)
    qtde_usuario = 0
    qtde_computador = 0
    print()
    if multiplo == 0:
        print('Você começa!')
        n = n - usuario_escolhe_jogada(n, m)
        jogador = True
        computador = False
    else:
        print('Computador começa!')
        n = n - computador_escolhe_jogada(n, m)
        jogador = False
        computador = True
    while n >= 1:
        if jogador == False:
            n = n - usuario_escolhe_jogada(n, m)
            jogador = True
            computador = False
        if computador == False:
            n = n - computador_escolhe_jogada(n, m)
            jogador = False
            computador = True
    if jogador == True:
        print('Fim do jogo! Você ganhou!')
    if computador == True:
        print('Fim do jogo! O computador ganhou!')

def computador_escolhe_jogada(n, m):
    print()
    i = 1
    mult = False
    while i <= m and mult == False:
        k = n - i
        if k % (m + 1) == 0:
            mult = True
            qtde_computador = i
        i = i + 1
    if mult == False:
        qtde_computador = m
    if qtde_computador > 1:
        print('O computador tirou', qtde_computador, 'peças.')
    if qtde_computador == 1:
        print('O computador tirou uma peça.')
    restantes = n - qtde_computador
    if restantes > 1:
        print('Agora restam', restantes, 'peças no tabuleiro.')
    if restantes == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
    return qtde_computador

def usuario_escolhe_jogada(n, m):
    print()
    qtde_usuario = int(input('Quantas peças você vai tirar? '))
    while qtde_usuario > m or qtde_usuario <= 0 or qtde_usuario > n:
        print()
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        qtde_usuario = int(input('Quantas peças você vai tirar? '))
        print()
    if qtde_usuario > 1:
        print('Você tirou', qtde_usuario, 'peças.')
    if qtde_usuario == 1:
        print('Você tirou uma peça.')
    restantes = n - qtde_usuario
    if restantes > 1:
        print('Agora restam', restantes, 'peças no tabuleiro.')
    if restantes == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
    return qtde_usuario

def campeonato():
    j = 1
    while j <= 3:
        print()
        print('**** Rodada', j, '****')
        print()
        partida()
        j = j + 1
    print()
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você 0 X 3 Computador')


print('Bem-vindo ao jogo do NIM! Escolha:')
print()
jogo()
