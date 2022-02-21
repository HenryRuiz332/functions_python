from clases.PrimeraClase import *

#Instancia
objCar = Car()

#Viendo y cambiando propiedades
chasis = objCar.largoChasis
chasis = 100
print(f"Se ha cambiado el largo del chasis a {chasis}")

#Encender Carro
print(objCar.run(False))#Esperando parametro

#Comprobando status
print(objCar.status())


#Creamos un segundo objeto

objCar2 = Car()
objCar2.__ruedas=2 #__ruedas no es accesible desde aqui

print(f"Objeto 2 : {objCar2.status()}")
print(objCar.run(True))
