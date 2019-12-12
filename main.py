import ai
from detect import detectar_resultado


tabuleiro = [' ',  ' ',  ' ',
             ' ',  ' ',  ' ',
             ' ',  ' ',  ' '
            ]

class JogadaInvalida(RuntimeError):
	pass

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

def humano_jogar(posicao, tabuleiro, simbolo):     # Esta função representa a jogada do usuário.
	
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
	if tabuleiro[posicao] != " " :
		raise JogadaInvalida("Jogada já feita.") #trata objeto como exceção
												 #("Jogada já feita") é o objeto da classe JogadaInvalida	
	tabuleiro[posicao] = simbolo


	return tabuleiro	

def mostrar_gui(tabuleiro):      # Essa função mostra o tabuleiro para o usuário realizar as jogadas

	print(' ' + ' | '.join(tabuleiro[0:3]))

	print('+'.join(['---', '---', '---']))

	print(' ' + ' | '.join(tabuleiro[3:6]))

	print('+'.join(['---', '---', '---']))

	print(' ' + ' | '.join(tabuleiro[6:9]))


	print("="*12)
# Esta etapa determina as jogadas que serão feitas ao longo do jogo atual.
fim_de_jogo = False

simbolo = "X"
while fim_de_jogo == False:

	try :
		if simbolo == "X" :
			jogada = entrada_do_usuario()
			tabuleiro = humano_jogar(jogada, tabuleiro, simbolo)
		else:
			tabuleiro = ai.fazer_jogada(tabuleiro, simbolo) 
		fim_de_jogo = detectar_resultado (tabuleiro)
		mostrar_gui(tabuleiro)
		if simbolo == "X" :
			simbolo = "O"
		else: 
			simbolo = "X"
	except JogadaInvalida as e:
		print(str(e))


print("Jogador " + fim_de_jogo + " ganhou.")