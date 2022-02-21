#Creaion de Carros
class Car(object):#SuperClase
	
 	#Method Construct

	"""docstring for Car"""
	def __init__(self):
	    #Estado inicial de los objetos
		#Propierty
		self.largoChasis = 250
		self.anchoChasis = 120
		self.__ruedas		= 4#Encapsulacion->Encapsular o proteger una propiedad para que no se pueda modificar fuera de la clase. Se podrá modificar dentro de la clase
		self.onOff 		= False
		

	#Methods	

	#Self, hace referencia a el propio objeto pertenenciente a la clase. Referencia a la intancia pertenecinte a la clase
	#Self equivalente a this, de otro lenguaje de programacion: PHP, Javascript

	#Metodo de arranque
	def run(self,on):
		self.onOff=on
		if self.onOff == True:
			return "El carro está Encendido"
		else:
			return "El carro está apagado"


	#Metodo status
	def status(self):
		print(f"El carro tiene {self.__ruedas} ruedas , un largo de {self.largoChasis}, ancho {self.anchoChasis}")
		
