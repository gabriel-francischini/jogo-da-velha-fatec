
def entrada_do_usuario():      # Esta função representa a entrada do usuário.
	return [0, 0]

def fazer_jogada(posicao):     # Esta função representa a jogada do usuário.
	return None

def checar_se_ganhou():        # Esta função analisa a condição de vitória do jogo atual.
	return True

# Esta etapa determina as jogadas que serão feitas ao longo do jogo atual.
fim_de_jogo = False
while fim_de_jogo != True:
	jogada = entrada_do_usuario()
	fazer_jogada(jogada)
	fim_de_jogo = checar_se_ganhou()