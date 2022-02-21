print("Asignaturas optativas año 2017");

print("Lista de asignaturas : Informatica grafica - Pruebas de Software - Accebilidad y usabilidad");

asignatura = input("Escribe la asignatura escogida: ");

opcion = asignatura.lower(); #Definir todos los caracteres en minusculas

if opcion in ("informatica grafica" , "pruebas de software", "accebilidad y usabilidad"): #Comparacion de estring
	print("Has elegido " + opcion);
else : 
	print("Error, o existe en la lista");