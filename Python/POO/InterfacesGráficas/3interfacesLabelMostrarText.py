from tkinter import *

#Archivos con extencion pyw ejecuta el archivo

#Crear Ventana Raíz
root = Tk(); #Instancia de la clase.

root.iconbitmap("favicon.png");

root.geometry("800x600")

miFrame = Frame(root, width="150", height="150")#Instanciar la clase, para crear un lienzo -frame
miFrame.pack(side="left", anchor="n")#empaquetar #side=right->mueve el frame a la derecha
miFrame.config(bg="yellow")

miImagen = PhotoImage(file="favicon.png")#Instancia para manipular imagenes

#Label
miLabel = Label(miFrame, text="Mi primera  \n Imagen en Python")#Instanciar clase para colocar texto estatico. Especificar variable del contenedor padre
#recibe como parametro property text, para colocar el texto que mostrará ese label
miLabel.place(x=10, y=10)#Ubicar texto en cualquier lugar x o y
miLabel.config(fg="red", font=("Comic Sans MS",12))#Configurar color texto, tipo de letra y tamaño

#utilizar imagenes en Label. Tkinter trabaja con formatos png y gif
Label(miFrame, image=miImagen).place(x=40, y=100)

#Abreviar codigo anterior si no vamos a utilizar otrave la variable miLabel
#Label(miFrame, text="Hola mundo").place(x=10, y=10)

root.mainloop()
