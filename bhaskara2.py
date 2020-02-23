import math

a = input('a? ')
b = input('b? ')
c = input('c? ')

if a == '' :
	a = 0
if b == '':
	b = 0
if c == '':
	c = 0

a = int (a)
b = int (b)
c = int (c)


D = (b**2) - (4 * a * c)
if a==0 and b==0 and c==0:
	print ('0=0, portanto x pertence aos reais')
elif a==0 and b==0:
	print ('não há raiz')
	print (c, 'é diferente de 0')
elif a == 0:
	X = -c/b
	print ('há apenas uma raiz real')
	print (X)
elif D<0:
	print('esta equação não possui raízes reais')
	D = math.fabs(D)
	b = -b/2
	D = math.sqrt(D)/2 * 100
	D = int (D)
	D = D / 100
elif D==0:
	X = -b/2
	print ('a raiz desta equação é',X)
else:
	X1 = (-b - math.sqrt(D))/2
	X2 = (-b + math.sqrt(D))/2
	print ('as raízes da equação são', X1, 'e' , X2)




	

