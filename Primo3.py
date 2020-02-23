def chamar (string):
	try:
		a = int (input (string))
	except:
		print ('valor inválido,', end = ' ')
		a  = chamar(string)
	return a

def EPrimo (Num):
	div = 2
	NPrimo = False

	while Num != div  and not NPrimo:
		if Num % div == 0:
			NPrimo = True
		div = div + 1

	return not NPrimo

def lista_primo(maior):
	i = 2
	Primo = 1
	while i <= maior:
		if EPrimo (i):
			print (i , end = '\t')
		i += 1

a = chamar('digite um valor inteiro:')

lista_primo(a)