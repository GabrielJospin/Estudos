#Fizzbuzz

def fizzbuzz(a):
	if a%15 == 0:
		return ('FizzBuzz')
	elif a%5 == 0:
		return ('Buzz')
	elif a%3 == 0:
		return ('Fizz')
	else:
		return (a)

def teste():
	i = 1
	while i<=30:
		fizzbuzz(i)
		i += 1

