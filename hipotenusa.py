#Hipotenusas

def hip_test (c):
	a = 1
	b = 1
	while c > a:
		a += 1
		b = 1
		while c > a and c > b:
			b +=1
			if c**2 == a**2 + b**2:
				return True
				break
	return False

def hip_sum(c):
	i = 0
	sum = 0
	while i<= c:
		if hip_test(i):
			sum += i
		i += 1
	return sum

lin = int(input('valor máximo'))
print (hip_sum(lin))



