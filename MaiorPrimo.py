#Maior Primo

def EPrimo (Num):
	div = 2
	NPrimo = False

	while Num != div  and not NPrimo:
		if Num % div == 0:
			NPrimo = True
		div = div + 1

	return not NPrimo

def maior_primo(maior):
	i = 2
	Primo = 1
	while i <= maior:
		if EPrimo (i):
			Primo = i
		i += 1
	return Primo

def test():
	if maior_primo(10)==7 :
		print ('Funciona pra 10')
	if maior_primo(15) == 13 :
		print ('funciona pra 15')
	if maior_primo(50)==47:
		print ('funciona pra 50')
	if maior_primo(100)==97:
		print('funciona pra 100')

