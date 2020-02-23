#444
#Desenhar Retângulo

def chamar (string):
	try:
		a = int (input (string))
	except:
		print ('valor inválido,', end = ' ')
		a  = chamar(string)
	return a

def desenharbase(b,y,h):
	x = 0
	if y == 0 or y == h-1:
		while x < b:
			print ('#', end = '')
			x += 1
	else:
		print ('#', end = '')
		while x < b - 2:
			print (' ', end = '')
			x += 1
		print ('#', end = '')

b = chamar ('Qual é a base: ')
h = chamar ('Qual é a atura: ')

y = 0
while y < h:
	desenharbase(b,y,h)
	print()
	y += 1
