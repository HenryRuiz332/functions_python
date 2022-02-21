i = 1;

while i <= 10:
	print(f"Valor {i}")
	i=i+1;#importante. Incrementa el valor de  i hasta 10. i comienza siendo 1 hasta 10. En la siguiente ejecución teminará.

print("Fin");
print();


edad = int(input("Introduce tu edad : "));

#Indeterminar bucle.
while edad<0 or edad>100: #Mientras que la edad sea menor que 0 o edad seam mayor que 100, entrará al loop.
	print(f"La edad {edad} es incorrecta");
	edad = int(input("Introduce tu edad : "));

print(f"Tu edad es {edad}");



