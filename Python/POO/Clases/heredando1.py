from clases.herencia import *

#Carro Chevrolet
class Chevrolet(Car): #Chevrolet hereda de Car
	pass
#Sintaxis para heredar de otra clase
	
class Moto(Car): #Chevrolet hereda de Car
	
	hcaballito = ""

	def caballito(self):
		self.hcaballito = "Voy haciendo caballito"
	

	#Sobresecribe el metodo de la superclase
	def statusObj(self):
		print(f"Marca : {self.marca} \n modelo: {self.modelo} \n Encendido: {self.onOff} \n Frenando: {self.frenar} \n Acelerando: {self.acelerar} \n Caballito: {self.hcaballito}")


class Furgoneta(Car):
	
	def carga(self, cargar):
		self.cargado = cargar

		if self.cargado == True:
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"




class vElectricos(Car):
	
	def __init__(self, marca, modelo):#Utilizar parametros del metodo construtor de la clase Padre
		super().__init__(marca, modelo)#Variables que van a ir a la Instancia
		self.autonomia = 100

	def cargado(self):
		
		self.cargando = True


class bicicletaElectrica(vElectricos, Car): #Herencia Multiple. Se da preferencia a la primera clase a la izq

	pass
		

obj = Chevrolet("Chevrolet", "350")
obj.onOff = True
obj.acelerar = True
obj.statusObj()


moto = Moto("Susuky", "200")
moto.caballito()
moto.statusObj()



furgoneta = Furgoneta("Ban", "350")
furgoneta.statusObj()
print(furgoneta.carga(True))



#super() - isinstance()
bici = bicicletaElectrica("Bici electrica", "3PO")
bici.statusObj()


#isintance: Comprobamos si un objeto pertenece a una clase

print(f"El objeto pertenece a la clase Car: {isinstance(bici, vElectricos)}")

#isinstance verifica si el objeto bici pertenece a la clase Car