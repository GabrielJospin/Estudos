#vogais

def vogal(letra):
	if letra == 'a':
		return True
	elif letra == 'e':
		return True
	elif letra == 'i':
		return True
	elif letra == 'o':
		return True
	elif letra == 'u':
		return True
	elif letra == 'A':
		return True
	elif letra == 'E':
		return True
	elif letra == 'I':
		return True
	elif letra == 'O':
		return True
	elif letra == 'U':
		return True
	else:
		return False

def teste ():
	if vogal('a'):
		print( 'funciona pra a')
	if not vogal ('b'):
		print ('funciona pra b')
	if vogal ('E'):
		print (' funciona pra E')

