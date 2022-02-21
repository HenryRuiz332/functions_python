from tkinter import *

#Creando Array de checkbox

#Radio buttons para seleccionado 
root = Tk(); 


root.geometry("800x600")
root.title("Ejemplo checkbox")

add = StringVar()
cantidad = 0
bucle = 1;
#checkbox = int(input("Introdcue cuantos checbox quieres: "));

check=IntVar()
check2=IntVar()
check3=IntVar()

def option():
	optionEscogida = ""

	if check.get()==1:
		optionEscogida+="playa"

	if check2.get()==1:
		optionEscogida+="montagna"

	if check3.get()==1:

		optionEscogida+="turismo"

	textFinal.config(text=optionEscogida)

#Crear un Array de checkbox dependiendo la cantidad que pusemos
def checkbox(cant):
	global cantidad
	global bucle

	cantidad = int(cant)
	add.set(cantidad)

	while bucle <= cantidad:
		
		Checkbutton(root, text=f"checkbox {bucle}", variable=bucle, onvalue=bucle, offvalue=0, command=lambda:option).grid(row=bucle, column=1)
		bucle = bucle+1


foto = PhotoImage(file="favicon.png")

button = Button(root,text="5 checkbox", command=lambda:checkbox("5"))
button.grid(row=0, column=1, sticky="w")
button.config(bg="blue", fg="white", cursor="hand2")


button2 = Button(root,text="10 checkbox", command=lambda:checkbox("10"))
button2.grid(row=0, column=2, sticky="w")
button2.config(bg="blue", fg="white", cursor="hand2")


button3 = Button(root,text="15 checkbox", command=lambda:checkbox("15"))
button3.grid(row=0, column=3, sticky="w")
button3.config(bg="blue", fg="white", cursor="hand2")


textFinal = Label(root)

root.mainloop()