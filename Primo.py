#primos

Num = int(input('Digite um número: '))
div = 2
NPrimo = False

while Num != div  and not NPrimo:
	if Num % div == 0:
		NPrimo = True
	div = div + 1

if NPrimo :
	print ('não primo')
else:
	print ('primo')
