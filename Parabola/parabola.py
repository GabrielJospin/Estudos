import math

def apresentação():
	print ("\nsimulador de parabolas\n")

def transforma (k):
	if k == '':
		k = 0
	else:
		k = float (k)
	return k

def delta(a,b,c):
	return b**2 - 4*a*c

def vertice(a,b,c):
	v = (-b/2*a , 0 - delta (a,b,c) / 4*a )
	return v

def raizes (a,b,c):
	r1 = ((-b - delta(a,b,c))/2*a ,0 )
	r2 = ((-b + delta(a,b,c))/2*a ,0 )
	return (r1,r2)


apresentação()

a = transforma( input ('valor de a: '))
b = transforma( input ('valor de b: '))
c = transforma( input ('valor de c: '))

if a == b == c == 0:
	quit()



v = vertice(a,b,c)

r1 = (raizes(a,b,c)[0])
r2 = (raizes (a,b,c)[1])

if delta(a,b,c) > 0:
	tab = v[0] - r1[0]
else:
	tab = 1

ex1 = v[0] - 5 * tab
ex2 = v[0] + 5 * tab

grafico = []

x = ex1 
while (x<= ex2 and a != 0):
	point = (x, (a*x**2 + b*x+ c) )
	grafico.append(point)
	if point == v and v[1]==0:
		print (point, 'vertice e raiz')		
	elif point[1] == 0 :
		print (point, 'raiz')
	elif point == v:
			print (point, 'vertice')
	else:
		print (point)
	x += tab

print(grafico)

x = -10
point = (-10, -10*b+c)

while(point[1] >= -10 and a==0 ):
	print (point)
	point = (point[0] + 1, (point[0]+1)*b + c)

