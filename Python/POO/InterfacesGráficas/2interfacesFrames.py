from tkinter import *

#Archivos con extencion pyw ejecuta el archivo

#Crear Ventana Raíz
raiz = Tk(); #Instancia de la clase.

#Titulo de la Ventana
raiz.title("Creando Frames");

#Evitar Redimencionar interfaz
raiz.resizable(1,1) #Funcion que permite dos parametros boolean, true or false. #width-height 
#En esta sintaxis, le decimos al programa que el tamaño de la ventana no pueda modificarse, ni ancho ni alto.

raiz.iconbitmap("favicon.png");

raiz.geometry("800x600")

miframe = Frame()#Instanciar la clase, para crear un lienzo -frame

#empaquetar frame
#miframe.pack(side="right")#empaquetar #side=right->mueve el frame a la derecha
#miframe.pack(side="bottom")#side=bottom->mueve el frame a la derecha
#miframe.pack(side="left")#side=left->mueve el frame a la derecha

#manejar dos parametros izquierda derecha o  derecha arriba
#miframe.pack(side="right", anchor="s" )#side=left->mueve el frame a la derecha + un segundo parametro anchor: maneja puntos cardinales
#n,s,w,e

#Rellenar en redimencion
miframe.pack(fill="y", expand=True) #Expandir Verticlamente

#Expandir junto con raiz
#miframe.pack(fill="both", expand=True)

#Configurar border
miframe.config(bd=10)
#miframe.config(relief="groove")
miframe.config(relief="sunken")

#Cambiar icono del cursor 
miframe.config(cursor="hand2");
miframe.config(cursor="pirate");

miframe.config(bg="red")#Dar color al frame
miframe.config(width="400", height="300")#Especificar dimenciones para notar el frame. 


raiz.mainloop();#Para que la ventana pueda estar abierta. mainloop.
#Es necesario que el método mainloop este en la parte final de ejecución del programa. Para que la ventana se mantenga abierta


#IMPORTNTE: LOS METODOS QUE SE UTILIZAN PARA CONFIGURAR EL FRAME, SE PUEDEN USAR EN RAIZ.

