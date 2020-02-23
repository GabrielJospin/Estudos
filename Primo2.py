def EPrimo (Num):
	div = 2
	Primo = True

	while Num != div  and Primo:
		if Num == 0 or Num == 1:
			return	False	
			break
		elif Num % div == 0:
			Primo = False
		div = div + 1

	return Primo
def chamar():
	try:
		a = int (input('digite um numero: '))
	except:
		print ('valor inválido, ', end = '')
		a = chamar()
	return a

n = 1

while n > 0:
	n = chamar()
	if EPrimo(n):
		print (n, 'é primo')
	else:
		print (n, 'n é primo')
