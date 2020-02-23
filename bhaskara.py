import math

def apresentar ():
		print ('bhaskara calculator')
		print ('')
		print ('A fórmula de bhaskara pode ser definida da seguinte maneira:')
		print('ax²+bx+c=0')
		print('baseado nisso de o valor de')

def main ():
	a = transf(input('a? '))
	b = transf(input('b? '))
	c = transf(input('c? '))
	calcula_raiz(a,b,c)

def transf(a):
	if a == '':
		return(0)
	else:
		return( int (a))

def delta(a,b,c):
	return (b**2) - (4 * a * c)

def coeficientes_nulos(a,b,c):
	if a==0 and b==0 and c==0:
		print ('0=0, portanto x pertence aos reais')
		return False
	elif a==0 and b==0:
		print ('não há raiz')
		print (c, 'é diferente de 0')
		return False
	elif a == 0:
		X = -c/b
		print ('há apenas uma raiz real')
		print (X)
		return False
	else:
		return True

def calcula_raiz(a,b,c):
	if coeficientes_nulos(a,b,c):
		d = delta (a,b,c)
		if d <0:
			print('não há raiz reais')
			D = math.fabs(delta(a,b,c))
			b = -b/2
			D = math.sqrt(D)/2 * 100
			D = int (D)
			D = D / 100
			print ('z=',b,'+', D, 'i')
		elif d ==0:
			print ('há apenas uma raiz real')
			X = -b/2
			print (X)
		else:
			print ('há duas raiz real')
			X1 = (-b + math.sqrt(d))/2
			X2 = (-b - math.sqrt(d))/2
			print (X1, ',' , X2)

apresentar()
main()


	

