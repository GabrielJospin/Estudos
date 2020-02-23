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

def n_primo(maior):
	i = 2
	Primo = 1
	j = 0
	while i <= maior:
		if EPrimo (i):
			j += 1
		i += 1
	return j
