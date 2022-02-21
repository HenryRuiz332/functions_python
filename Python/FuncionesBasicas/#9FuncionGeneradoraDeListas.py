#Generadores: Extructuras que extraen valores de una función, que se pueden almacenar en objetos iterables. 
#Esos objetos se pueden recorrer a tráves de un bucle.

#Los generadores hacen el mismo trabajo que una función estandar, sin embargo, al ser invocado un generador,
#devuelve un primer objeto y queda en estado de pausa y reanuda el códgo desde donde fue llamado. Al llamar a otro objeto del generador,
#solo va a devolver ese otro objeto y queda en estado de pausa.

def generador(limite):
	
	numero = 1;
	array = [];

	while numero < limite:
		array.append(numero*2);#En este array se irra almacenando, los nuemros pares.
		numero=numero+1;

	return array;



print (generador(20));