tabuleiro = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def entrada_do_usuario():
	return [0, 0]

def fazer_jogada(posicao, tabuleiro):
	
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

	return posicao

def checar_se_ganhou():
	return True


fim_de_jogo = False
while fim_de_jogo != True:
	jogada = entrada_do_usuario()
	fazer_jogada(posicao, tabuleiro)
	fim_de_jogo = checar_se_ganhou()
