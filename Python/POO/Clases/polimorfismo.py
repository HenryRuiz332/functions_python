#Polimorfismo: Es cuando un objeto puede tener varias formas, cambia de corpontamiento

class Coche():
	"""docstring for Coche"""
	def desplazamiento(self):
		print("Me desplazo con 4 ruedas")


class Moto():
	"""docstring for Coche"""
	def desplazamiento(self):
		print(f"soy Me desplazo con 2 ruedas")


class Camion():
	"""docstring for Coche"""
	def desplazamiento(self):
		print("Soy camion Me desplazo con 8 ruedas")


# new = Moto()
# new.desplazamiento()


# new2 = Coche()
# new2.desplazamiento()


# new3 = Camion()
# new3.desplazamiento()


#Poliformismo en accion
def desplazamientoVehiculo(vehiculo): #El objeto va cambiando de forma mediante la instancia que usemos
	vehiculo.desplazamiento()


camion = Coche()
desplazamientoVehiculo(camion)