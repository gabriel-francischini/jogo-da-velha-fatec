tabuleiro = [' ',  ' ',  ' ',
             ' ',  ' ',  ' ',
             ' ',  ' ',  ' '
            ]

def coordenada_esta_no_limite(c, texto):
	while (c < 0) or (c > 2):
		c = int(input('Digite o valor da '+ str(texto) + ': ' ))
	return c

def entrada_do_usuario():      # Esta função representa a entrada do usuário.

	i = int(input('Digite o valor da linha: '))
	i = coordenada_esta_no_limite(i, 'linha')
		

	j = int(input('Digite o valor da coluna: '))
	j =	coordenada_esta_no_limite(j, 'coluna')

	return [i, j]

def fazer_jogada(posicao, tabuleiro):     # Esta função representa a jogada do usuário.
	
	if posicao == [0,0]:
		posicao = 0
	if posicao == [0,1]:
		posicao = 1
	if posicao == [0,2]:
		posicao = 2
	if posicao == [1,0]:
		posicao = 3
	if posicao == [1,1]:
		posicao = 4
	if posicao == [1,2]:
		posicao = 5
	if posicao == [2,0]:
		posicao = 6
	if posicao == [2,1]:
		posicao = 7
	if posicao == [2,2]:
		posicao = 8
	tabuleiro[posicao] = "X"

	return tabuleiro	

def mostrar_gui(tabuleiro):      # Essa função mostra o tabuleiro para o usuário realizar as jogadas

	print(' ' + ' | '.join(tabuleiro[0:3]))

	print('+'.join(['---', '---', '---']))

	print(' ' + ' | '.join(tabuleiro[3:6]))

	print('+'.join(['---', '---', '---']))

	print(' ' + ' | '.join(tabuleiro[6:9]))


def detectar_resultado (tabuleiro):   # Essa função representa a detecção responsável por determinar o resultado da partida.
	
	#Linhas Verticais
	for marcador in range(0,3,1):
		if tabuleiro[marcador] == tabuleiro[marcador+3]==tabuleiro[marcador+6]:
			if tabuleiro[marcador] == 'X' or tabuleiro[marcador] == 'O':
				return tabuleiro[marcador]

	#Linhas Horizontais
	for horizontal in range(0,9,3):
		if tabuleiro[horizontal] == tabuleiro[horizontal+1]==tabuleiro[horizontal+2]:
			if tabuleiro[horizontal] == 'X' or tabuleiro[horizontal] == 'O':
				return tabuleiro[horizontal]

	#Linhas Diagonais
	if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
		if tabuleiro[0] == 'X' or tabuleiro[0] == 'O':
			return tabuleiro[0]

	if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
		if tabuleiro[2] == 'X' or tabuleiro[2] == 'O':
			return tabuleiro[2]
	return False

# Esta etapa determina as jogadas que serão feitas ao longo do jogo atual.
fim_de_jogo = False
while fim_de_jogo == False:
	jogada = entrada_do_usuario()
	tabuleiro = fazer_jogada(jogada, tabuleiro)
	fim_de_jogo = detectar_resultado (tabuleiro)
	mostrar_gui(tabuleiro)
print("Jogador " + fim_de_jogo + " ganhou.")