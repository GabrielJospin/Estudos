#Fatoriais

lim = int (input ('quantos fatorias serão calculados? '))

def calcularfatorial(n):
	if n >= 0:
		m = 1
	else:
		m = 'número sem fatorial definido'
	while n > 1:
		m =m * n
		n = n - 1
	return m 

i = 1
while i<= lim:
	n = int (input ('numero: '))
	print( calcularfatorial(n))
	i += 1
