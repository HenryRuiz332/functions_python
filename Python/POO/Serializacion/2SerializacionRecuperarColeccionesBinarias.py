import pickle #Importar biblioteca para poder serializar

path = "files/ficheroBinario.txt";
fichero = open(path, "rb");#Read binary. parametro para leer archivos binaros

lista=pickle.load(fichero);#Cargar información desde un archivo binario

print(lista);