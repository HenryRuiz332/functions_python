for letra in "Python":
	#print(letra);
	if letra == 'h': #Salta a la siguiente linea sin leer la h
		continue
	print(f"la letra es {letra}");

print("#############salto de linea");
print();



print("Contar numeros de caracteres");
nombre = "Pildoras Informaticas";
contador = 0;
print(f"La palabra Pildoras informaticas tiene  {len(nombre)} con la funcion len():Longitud")

for i in nombre:
	if i == " ":
		continue
	contador+=1;#Incrmenta la variable contador en 1

print(f"Si aplicamos un bucle for usando continue, entonces la palabra Pildoras Informaticas, verdaderamente tiene {contador} caracteres ")
