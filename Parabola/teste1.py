#Paraola

import matplotlib.pyplot as plt
import numpy as np


def apresentação():
	print ("\nsimulador de parabolas\n")

def transforma (k):
	if k == '':
		k = 0
	else:
		k = int(float (k))
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
	tab =v[0] - r1[0]
else:
	tab = 1

ex1 = v[0] - 5 * tab
ex2 = v[0] + 5 * tab

x=[]
y=[]
i = ex1

while (i<= ex2 and a != 0):
	x.append(i)
	y.append(a*i**2+b*i+c)
	i += 0.1


plt.plot(x,y)


plt.title("Parabola")

plt.legend()

plt.show()
