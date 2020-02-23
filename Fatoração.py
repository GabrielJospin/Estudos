#Fatoração

def EPrimo (Num):
	div = 2
	NPrimo = False

	while Num != div  and not NPrimo:
		if Num % div == 0:
			NPrimo = True
		div = div + 1

	return not NPrimo


def multiplicidade(num, div):
	i = 0
	while num >= 1 : 
		if num %div == 0:
			i += 1
			num = num / div
		else:
			break
	return i

num = int (input ('qual é o numero? '))
div = 2

while num >= div:
	if EPrimo(div):
		mult = multiplicidade(num, div)
		if mult != 0 :
			print (div, "^", mult, end = '\t')
	div += 1
