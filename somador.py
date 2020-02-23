print ('')
print ('somador')
print ('')

soma = int(input('Quantos numeros iremos somar: '))


i = 0
a = 0
while i < soma:
	b = input()
	if (b ==''):
		b = 0
	else:
		b = int (b)
	a = a+b
	i = i+1
print ('')
print (a)