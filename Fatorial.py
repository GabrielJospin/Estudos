#Fatorial
Num = int(input('Numero que se quer fatoriar: '))
Resp = 1
while Num != 0:
	Resp = Resp * Num
	Num += -1

print (Resp)
