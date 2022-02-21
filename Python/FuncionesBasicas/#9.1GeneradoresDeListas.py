#Generadores: Extructuras que extraen valores de una función, que se pueden almacenar en objetos iterables. 
#Esos objetos se pueden recorrer a tráves de un bucle.

#Los generadores hacen el mismo trabajo que una función estandar, sin embargo, al ser invocado un generador,
#devuelve un primer objeto y queda en estado de pausa y reanuda el códgo desde donde fue llamado. Al llamar a otro objeto del generador,
#solo va a devolver ese otro objeto y queda en estado de pausa.

def generador(limite):
	
	numero = 1;

	while numero < limite:
		yield numero*2;
		numero=numero+1;


devuelvePare = generador(10);

# for i in devuelvePare:
# 	print(i)

print(next(devuelvePare));

print("Agua con jabon")

print(next(devuelvePare));

print("Ayuda en contra del corona virus")

print(next(devuelvePare));