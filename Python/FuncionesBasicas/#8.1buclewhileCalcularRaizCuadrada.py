
#import class

import math;

numero = int(input("Introduce un número : "));

intentos = 0;
while numero<0:
	print(f"No se puede hayar el valor de {numero}");
	
	if intentos==2:
		print("Has intentantos varias veces, espera unos minutos para volver a intentarlo");
		break; #Salir del bucle.
	
	numero = int(input("Introduce un número : "));
	if numero<0:
		intentos=intentos+1;

if intentos<2:
	solucion=math.sqrt(numero);
	print(f"La raiz cuadrada de {numero} es {solucion}");