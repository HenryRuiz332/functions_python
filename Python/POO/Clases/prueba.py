
def tableSum():
	numero=0
	array=[]

	while numero < 10:
		array.append(numero*2)#En este array se irra almacenando, los nuemros pares.
		numero=numero+1

	return array

print(tableSum())