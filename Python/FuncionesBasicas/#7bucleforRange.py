# for i in range(5,51,3): #Cuenta desde un punto a otro : 5-6-7-8-9
# 	print(f"Valor de variable {i}");
# 	print();
# 	print();

valido = False;
email = input("Introduce tu email: ");

for i in range(len(email)):
	if email[i]=="@":
		valido = True;

if valido:
	print("email Correcto")
else:
	print("Email incorrecto")