
#Abrir archivo en Modo Escritura
from io import open

archivotexto = open("files/ejemplo.txt", "w"); #Recibe dos parametros. El nombre de Archivo y el modo en que lo vamos a abrir(Lectura, Escritura, Append)
text = "Esta es la información que se va a guardar en el archivo ejemlo \n siguiente linea";

archivotexto.write(text); #Escribimos en el archivo
archivotexto.close();#cerramos el archivo


#Abrir archivo en modo Lectura

archivoLectura  =  open("files/ejemplo.txt", "r");

textRead = archivoLectura.read();#leemos lo que hay en el archivo y lo almacenamos en una variable.
print(textRead);
archivotexto.close();#cerramos el archivo


#Abrir archivo en modo Lectura linea a linea
archivoLecturaLinea  =  open("files/ejemplo.txt", "r");
textLine = archivoLecturaLinea.readlines();#Almacena la información en una lista

archivotexto.close();
#print(textLine[0]); #Accediendo a indices de la listas
print(textLine);


#Abrir archivo para agregar información

archivoAppend  =  open("files/ejemplo.txt", "a");
addText = archivoAppend.write("\n Esta es nueva información agregada");

archivoAppend.close();