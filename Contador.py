Num = int(input('Digite o Numero a ser somado: '))
a = 0

while Num != 0:
	a = a + Num%10
	Num = Num//10

print (a)