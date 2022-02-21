import pickle


class Person:
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print(f"Se ha creado a la persona {self.nombre}")


	def __str__(self):#Convierte en cadena de texto
		return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersona:
	"""docstring for listaPersona"""
	personas = [];

	def __init__(self):
		listaDePersonas = open("ficheroPermnente.txt", "ab+");
		listaDePersonas.seek(0);#Se desplaza el cursor al principio para que se pueda ller toda la info del archivo

		try:
			self.personas = pickle.load(listaDePersonas);
			print("Se actualizo el archivo".format(len(self.personas)));
		except:
			print("El fichero está vacío")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def AddPerson(self, p):
		self.personas.append(p)
		self.savePersonsInFile()

	def showPerson(self):
		for i in self.personas:
			print(i)

	def savePersonsInFile(self):#Guarda la data en un fichero. Fichero externo
		listaDePersonas.open("ficheroPermnente.txt", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroe(self):
		print(f"Info")
		for x in self.personas:
			print(x)
		

listperson = ListaPersona()#Instancia

persona = Person("Henry", "Masculino", 28);
# # listperson.AddPerson(p)
# persona = Person("Antonio", "Masculino", 27);
# # listperson.AddPerson(p)
# persona = Person("Ana", "Femenino", 18);
# listperson.AddPerson(p)

listperson.AddPerson(persona)
listperson.mostrarInfoFicheroe()



