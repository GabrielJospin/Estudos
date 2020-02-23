#funções
def chamar(string):
	try:
		a = int (input(string))
	except:
		print ('valor inválido, ', end = '')
		a = chamar(string)
	return a

def apresentação():
	print ('')
	print ('Bem-vindo ao jogo do NIM! Escolha:')
	print ('')
	print ('1 - jogo único')
	print ('2 - campeonato')
	option = chamar ('escolha o modo de jogo: ')
	return option

def teste(a):
	if a == '2':
		return True
	elif a == '1':
		return False
	else:
		print ('opção inválida')

def vez_jogador(m,n):
	a = chamar('quantas peças você irá retirar: ')
	if a <= n:
		m = m - a
		print (' restam apenas', m, 'peças')
		return m
	else:
		print (' jogada inválida')
		return vez_jogador (m,n)

def vez_computador (m,n):
	if m <= n:
		m = 0
		print ('o computador ganhou o jogo')
	elif m == n+1:
		m = m
		print (' o computador retirou', 0 , 'peças' )
		print ('restam apenas', m , 'peças')
	elif m <= 2*n + 1:
		print ('o computador retirou', m - n - 1, 'peças')
		m = n + 1
		print (' restam apenas', m , 'peças')
	else:
		m = m - n
		print (' o computador retirou', n, 'peças')
		print (' restam apenas', m, 'peças')
	return m

def jogada(m,n):
	tip = 0
	while m > 0:
		m = vez_computador(m,n)
		if m == 0:
			tip = 1
			break
		else :
			m = vez_jogador(m,n)

	if tip == 1:
		return True
	else:
		print ('vc ganhou')
		return False

def campeonato():
	comp = 0
	vc = 0
	while comp + vc < 3 :
		print ('***partida', comp+vc+1 , '***')
		m = chamar('quantas peças:')
		n = chamar('limite:')
		if m <= n :
			print (' n tem que ser menor que m')
		elif jogada(m,n):
			comp+=1	
		else:
			vc +=1
		print ('computador', comp, 'x', vc , 'você')
	if comp > vc :
		print (' o computador ganhou o jogo!')
	else:
		print ('vc ganhou o jogo')
	
def partida_unica():
	m = chamar('quantas peças:')
	n = chamar('limite:')
	if m <= n :
		print (' n tem que ser menor que m')
	elif jogada(m,n):
		print ('FIM DE JOGO')
	else:
		print ('vc ganhou')
		print ('FIM DE JOGO')

#jogo

boole =teste(apresentação()) 
if boole :
	campeonato()
elif boole==False :
	partida_unica()
else:
	print ('digite uma opção válida')
