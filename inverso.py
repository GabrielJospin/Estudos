#inverso

num = 1
lista=[]
while num != 0:
	num = int (input('insira um numero: '))
	lista.append(num)
	
i = len (lista)
j = 0

while j < i :
	x = lista[j]
	lista [j] = lista [i-1]
	lista [i-1] = x
	j += 1
	i += - 1

for i in range(1, len(lista)): 
	print (lista[i], end = '\t')

