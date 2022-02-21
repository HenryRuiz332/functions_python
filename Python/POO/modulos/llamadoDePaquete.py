#Importar nombreDePaques, es el nombre de la carpeta, usamos  . y nombre de archivo
from paquetes.calculos import *

var = 0
n = "numero"

while var <= 1:
	
	n = int(input(f"numero{var}: "))
	var+=1



print(f" {sumar(n,n)}")
print(f" {restar(n,n)}")
print(f" {multi(n,n)}")
print(f" {potencia(n,n)}")



