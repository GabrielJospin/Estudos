#maximo2
def  maximo2(a,b):
	if a >= b:
		return a
	else:
		return b

def  maximo(a,b,c):
	return maximo2 (maximo2(a,b), maximo2(b,c))


def teste():
	if maximo(1,2,3) == 3:
		print ('funcionou')
	else:
		print (maximo(1,2,3))
	if maximo(4,5,3) == 5:
		print ('funcionou')
	else:
		print (maximo(4,5,3))
	if maximo(12,5,6) == 12:
		print ('funcionou')
	else:
		print (maximo(12,5,6))
