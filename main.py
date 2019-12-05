#sei laaaaaaaaaaaaaaaaaa
def entrada_do_usuario():
	return [0, 0]

def fazer_jogada(posicao):
	return None

def checar_se_ganhou():
	return True


fim_de_jogo = False
while fim_de_jogo != True:
	jogada = entrada_do_usuario()
	fazer_jogada(jogada)
	fim_de_jogo = checar_se_ganhou()