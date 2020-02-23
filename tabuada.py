#Tabuada

linha = 1
coluna = 1

def tabuada_linha(linha,coluna):
	while coluna <= 10:
		print( linha * coluna, end = '\t' )
		coluna += 1


def tabuada_completa(linha,coluna):
	while linha <= 10 :
		tabuada_linha(linha,coluna)
		print ('')
		linha += 1


tabuada_completa(linha,coluna)