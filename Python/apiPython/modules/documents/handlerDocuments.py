# Python program to explain os.scandir() method

# importing os module
import os


# Directory to be scanned
path = 'folder'



with os.scandir(path) as ficheros:
	ficheros = [fichero.name for fichero in ficheros if fichero.is_file()] #ichero.is_dir() //para recorrer directorios
print(ficheros)