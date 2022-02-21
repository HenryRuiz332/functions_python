from tkinter import *

#Archivos con extencion pyw ejecuta el archivo

#Crear Ventana Raíz
raiz = Tk(); #Instancia de la clase.

#Titulo de la Ventana
raiz.title("Título");

#Evitar Redimencionar interfaz
raiz.resizable(1,1) #Funcion que permite dos parametros boolean, true or false. #width-height 
#En esta sintaxis, le decimos al programa que el tamaño de la ventana no pueda modificarse, ni ancho ni alto.

#Cambiar icono o establecer icono
raiz.iconbitmap("favicon.png");#Colocar archivo con extencion .ico

#cambiar tamaño de ventana widthxheight
raiz.geometry("800x600")

#Cambiar color de fondo
raiz.config(bg="skyblue")

raiz.mainloop();#Para que la ventana pueda estar abierta. mainloop.
#Es necesario que el método mainloop este en la parte final de ejecución del programa. Para que la ventana se mantenga abierta