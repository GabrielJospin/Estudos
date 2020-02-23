#444
#Desenhar Retângulo

def chamar (string):
	try:
		a = int (input (string))
	except:
		print ('valor inválido,', end = ' ')
		a  = chamar(string)
	return a

def desenharbase(b):
	x = 0
	while x < b:
		print ('#', end = '')
		x += 1




b = chamar ('Qual é a base: ')
h = chamar ('Qual é a altura: ')

y = 0
while y < h:
	desenharbase(b)
	print()
	y += 1
