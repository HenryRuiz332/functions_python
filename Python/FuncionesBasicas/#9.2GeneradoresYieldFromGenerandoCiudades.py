def generadorCiudades(*ciudades): #* Recibe un número indeterminado de elementos. Recibe elemento en furma de tupla

	for i in ciudades:
		# for j in i:
		# 	print(f"{j} tiene {len(j)} letras");
		yield from i 


ciudadesReturn = generadorCiudades("Caracas", "Madrid", "Berlin", "Montevideo");


print(next(ciudadesReturn))
print(next(ciudadesReturn))