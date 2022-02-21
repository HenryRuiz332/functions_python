# edad = int(input(" Introduce tu edad : "));

# if 0 < edad < 100:  #Evalua si es menor que 0 y menor que 100
# 	print("Edad Correcta");
# else:
# 	print("Edad Incorrecta. Debe ser menor a 100 y mayor que 0");


salarioPresidente = int(input("Salario del presidente : "));
print("Salario del presidente es :" + str(salarioPresidente) + "$"); #str() : Permite leer un numero como strin. Se utiliza en este caso para poder concatenar.


salarioDirector = int(input("Salario del Director : "));
print("Salario del Director es :" + str(salarioDirector) + "$");


salarioJefeArea = int(input("Salario del Jefe de Area : "));
print("Salario del  Jefe de Area es :" + str(salarioJefeArea) + "$");

salarioAdministrativo = int(input("Salario Administrativo : "));
print("Salario Administrativo es :" + str(salarioAdministrativo) + "$");

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
	print("El salario del presidente es el mayor, todo esta funcionando");

else:
	print("Algo falla");