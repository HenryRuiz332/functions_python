print("Verificar acceso");

ageUser=int(input("Introduce tu edad:\n"));
limitAge = int(100);

if ageUser<18:
	print("No eres mayor de edad");
elif ageUser> limitAge:
	while ageUser>100:
		print ("edad incorrecta");
		ageUser=int(input("Introduce tu edad:\n"));
		pass
else:
	 print("Eres mayor de edad");