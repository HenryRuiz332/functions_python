#La serializacion consiste en guardar en un fichero externo, objetos, colecciones, en formato de código binario
#Usar Biblioteca Pickle
#dump():Volcado de datos al fichero binario
#load():Carga de datos del fichero binario

import pickle #Importar biblioteca para poder serializar

listaNombre = ["Pedro", "Ana", "María", "Luis"];
path = "files/ficheroBinario.txt";
ficheroBin = open(path, "wb");#Escritura binaria. Write Binary

pickle.dump(listaNombre, ficheroBin)#Recibe 2 argumentas: Informacion que queromos volcar - Fichero al que qeremos volcar la coleccion

ficheroBin.close();
print(ficheroBin)
del(ficheroBin);#Borrarlo de la memoria