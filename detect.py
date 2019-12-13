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