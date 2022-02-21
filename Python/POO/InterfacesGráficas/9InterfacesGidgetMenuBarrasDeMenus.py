from tkinter import *

root = Tk()
root.geometry("600x600")

barMenu = Menu(root)
root.config(menu=barMenu)

#Nombre menu
archivoMenu = Menu(barMenu, tearoff=0)
#Submenu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Salir")

archivoMenu.add_separator()#Separar grupos de opciones
archivoMenu.add_command(label="FTP")


archivoEdicion = Menu(barMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barMenu, tearoff=0)
archivoHerramientas.add_command(label="Colores")
archivoHerramientas.add_command(label="Teclado en pantalla")
archivoHerramientas.add_command(label="Copia color")

archivoAyuda = Menu(barMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")


#texto de estos elementos de menu
barMenu.add_cascade(label="Archivo", menu=archivoMenu)

barMenu.add_cascade(label="Edición", menu=archivoEdicion)

barMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()