#Encontre a duplicato


def FindNumber(Array):
	comp = len(Array)
	i = 0
	NewArray = []
	while i < comp:
		j = 1
		while j < comp :
			if Array [i] == Array [j] and i < j:
				print(Array [i])
			j +=1

		i+=1