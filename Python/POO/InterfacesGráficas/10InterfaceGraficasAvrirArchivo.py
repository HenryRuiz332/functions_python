from tkinter import *
from tkinter import filedialog #Importar para realizar aperturas de ventanas de dialogo

root = Tk()
root.geometry("600x600")

#Abrir ventana en un sitio especifico  initialdir="ruta"
#visuaizar tipos de archivos filetypes. Acepta como valor de atribito, una tupla. En la tupla especificamos un titulo de
#acuerdo al tipo de archivo que queremos que se muestre, y como segundo parametro, la extención

def openWindow():
	file = filedialog.askopenfilename(title="Abriendo", initialdir="C:", 
									filetypes=(
											("Ficheros Docs", "*docx"),
											("Fiheros texto", ".txt") 
										) 
					  ) #Se ejecuta, y abre una ventana emergente para abrir archivo	
	print(file)


frame = Frame()
frame.pack()
frame.config(bg="skyblue", width=300, height=300)

button = Button(frame, text="Abrir fichero", command=openWindow)
button.pack()



root.mainloop()