#Combinação
def arranjo(n,k):
	Resp = 1
	while n > k:
		Resp = Resp * n
		n += -1
	return Resp

def fatorial (n):
	Resp = 1
	while n != 0:
		Resp = Resp * n
		n += -1
	return Resp
def combinação(n,k):
	return arranjo(n,k)/fatorial(n-k)

def main ():
	n = int( input (' dê o valor de n: '))
	k = int(input (' dê o calor de k: '))
	if n < k:
		print (' n deve ser maior que k')
		main()
	else:
		print (combinação(n,k))
main()