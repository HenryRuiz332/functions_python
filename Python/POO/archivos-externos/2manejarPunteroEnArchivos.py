#Editar un archivo en determinada posicion
from io import open

archivotexto = open("files/ejemplo.txt", "r"); 
archivotexto.seek(10)
read = archivotexto.read()
print(read)

archivotexto.close()


#Situar el cursor en la mitad de un archivo

archivotextoMitad = open("files/ejemplo.txt", "r"); #r+: Lectura y escritura
archivotextoMitad.seek(len(archivotextoMitad.read())/2);#Devuelve la longitud de caracteres y luego lo divide entre 2. Se obtiene la mitad de caracteres que tien el archivo

print(archivotextoMitad.read());#Ubica el cursor en el centro de la cantidad de palabras que existe en el archivo

archivotextoMitad.close();