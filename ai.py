import detect
import random


def fazer_jogada_burra(tabuleiro, simbolo) :
	for i in range(len(tabuleiro)) :
		if tabuleiro[i] == " " :
			tabuleiro[i] = simbolo
			break	

	return tabuleiro

def fazer_jogada_aleatoria(tabuleiro, simbolo) :
	jogadas_possiveis = []
	for i in range(len(tabuleiro)) :
		if tabuleiro[i] == " " :
			jogadas_possiveis.append(i)
	posicao = random.choice(jogadas_possiveis)
	tabuleiro[posicao] = simbolo
	return tabuleiro 

def fazer_jogada_inteligente(tabuleiro, simbolo) :
	_ = None
	
	for i in range(len(tabuleiro)) : ##análise para ganhar
		if tabuleiro[i] == " " :
			tabuleiro_futuro = tabuleiro.copy()
			tabuleiro_futuro[i] = "O"
			resultado = detect.detectar_resultado(tabuleiro_futuro)
			if resultado == "O" :
				tabuleiro[i] = simbolo
				return tabuleiro

	for i in range(len(tabuleiro)) : #análise para empatar
		if tabuleiro[i] == " " :
			tabuleiro_futuro = tabuleiro.copy()
			tabuleiro_futuro[i] = "X"
			resultado = detect.detectar_resultado(tabuleiro_futuro)
			if resultado == "X" :
				tabuleiro[i] = simbolo
				return tabuleiro

	
	return fazer_jogada_aleatoria(tabuleiro, simbolo)		


fazer_jogada = fazer_jogada_inteligente
				