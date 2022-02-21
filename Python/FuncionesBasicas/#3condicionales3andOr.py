print("Estudiantes aspirantes a becas ")

distanciaKm = int(input("Introduce la distancia en KM : "));
print("Distancia" + str(distanciaKm));

hermanos = int(input("Introduce numero de hermanos : "));
print("Hermanos " + str(hermanos));

salario = int(input("Introduce el salario familiar : "));
print("El salario es " + str(salario));


#if distanciaKm > 40 and hermanos > 2 and salario <= 20000 : #Se deben cumplir todas las condiciones para que tenga becas
if distanciaKm > 40 and hermanos > 2 or salario <= 20000 :
	print("Te has ganado la beca");
else :
	print("No necesitas becas");
