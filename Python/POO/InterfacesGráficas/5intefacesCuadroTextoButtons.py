from tkinter import * 




root = Tk()
root.geometry("800x600")

nombre=StringVar();

frame = Frame(root, width="400", height="300");
frame.pack()
frame.config(bd=2, 
			 relief="solid")

inputText = Entry(frame, textvariable=nombre)#Con textvariables, asociamos el cuadro de texto con la variable nombre
inputText.grid(row=0, column=1)#Sistema de Regilla
nomLabel = Label(frame, text="Nombre")
nomLabel.grid(row=0, column=0, sticky="e", pady=5) #Estableciendo, alineamiento de texto con Sticky, y padding con pady

#Input Apeellido
inputApe = Entry(frame)
inputApe.grid(row=1, column=1)#Sistema de Regilla
apeLabel = Label(frame, text="Apellido")
apeLabel.grid(row=1, column=0, sticky="e", pady=5)

#Input Direccion
inputAddr = Entry(frame)
inputAddr.grid(row=2, column=1)#Sistema de Regilla
apeLabel = Label(frame, text="Dirección de casa")
apeLabel.grid(row=2, column=0, sticky="e", pady=5)


##Input Password
inputPass = Entry(frame)
inputPass.grid(row=3, column=1)#Sistema de Regilla
inputPass.config(show="*")
passLabel = Label(frame, text="Password")
passLabel.grid(row=3, column=0, sticky="e", pady=5)


#Input Textarea
inputTextarea = Text(frame, width=15, height=5)
inputTextarea.grid(row=4, column=1)#Sistema de Regilla
textareaLabel = Label(frame, text="Comentarios")
textareaLabel.grid(row=4, column=0, sticky="ne", pady=5)

#Construir objto ScroolBar para textarea
scrollY = Scrollbar(frame, command=inputTextarea.yview)#Parametro comman: Pertenece a la caja de texto determinada y será scroll vertical "yview"
scrollY.grid(row=4, column=2, sticky="nsew")#Adaptar scroll a la caja de texto

#Adaptar scroll al punto donde se encuentren el cursor en la caja de texto
inputTextarea.config(yscrollcommand=scrollY.set)


#Funcion de Boton: Por ejemplo, al pulsar el boton agregamos el boton
def defButton():
	nombre.set("Henry")

button = Button(frame,text="Enviar", command=defButton);
button.grid(row=6, column=1, sticky="w")
button.config(bg="blue", fg="white", cursor="hand2")#Fg FONTGROUND color de letra


#Propiedad sticky->Alinear arriba abajo, derecha. Valores: Punto cardinales= "n,s,e,w" -> "nw, ne, sw, se,"

root.mainloop()