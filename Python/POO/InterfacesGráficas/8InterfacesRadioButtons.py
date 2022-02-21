from tkinter import *

#Radio buttons para seleccionado 
root = Tk(); 
varOptions=IntVar()

def imprimir():
	#print(varOptions.get())
	if varOptions.get() == 1:
		etiqueta.config(text="Has elegido masculino")
	elif varOptions.get() == 3:
		etiqueta.config(text="Has elegido otros")
	else:
		etiqueta.config(text="Has elegido femenino")

Label(root, text="Seleccion simple").pack()

radio =Radiobutton(root,text="Selecciona 1", variable=varOptions, value=1, comman=imprimir)
radio.pack()

radio2 =Radiobutton(root,text="Selecciona 2", variable=varOptions, value=2, comman=imprimir)#Imprimir en consola llamanado a la funcion
radio2.pack()

radio3 =Radiobutton(root,text="Selecciona 3", variable=varOptions, value=3, comman=imprimir)
radio3.pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()