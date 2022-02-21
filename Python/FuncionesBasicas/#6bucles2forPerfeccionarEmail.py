#Validar correo electrónico 
contador = 0;
emailInput = input("Introducir Email : ");


#La variable contador comienza en 0, a cada vuelta de bucle la variable contador ira aumentando, dependiendo del tipo
#de comparación que vayamos haciendo.
for i in emailInput:
	if (i=="@" or i=="."):
		contador = contador+1
		print(contador);
#Luego se iguala a contador con el nuemro de validaciones que hagamos. En el siguiente caso devolvera una respuesta u otra
#dependiendo de nuestra validación.
if contador == 2 :
	print("Email Correcto");
else :
	print("La dirección de email no es correcta");