Num = int ( input ( 'digite um numero: '))

AdjIguais = False

while Num !=0 and not AdjIguais:
	ant1 = Num % 10
	Num = Num//10
	ant2 = Num %10
	if ant2 == ant1:
		AdjIguais = True

if AdjIguais:
	print ('sim')
else:
	print ('não')
