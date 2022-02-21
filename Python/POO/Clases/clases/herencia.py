#La herencia: Se trata de heredar de otras clases las misma funcionalidades
class Car(object):#SuperClase
	
	"""docstring for Car"""
	def __init__(self, marca, modelo):
		self.marca = marca 
		self.modelo = modelo
		self.onOff 	= False
		self.acelerar = False
		self.frenar = False

	#Methods
	def run(self):
		self.onOff = True

	def acelerar(self):
		self.acelerar = True		
		
	def frenar(self):
		self.frenar = True

	def statusObj(self):
		print(f"Marca : {self.marca} \n modelo: {self.modelo} \n Encendido: {self.onOff} \n Frenando: {self.frenar} \n Acelerando: {self.acelerar}")


