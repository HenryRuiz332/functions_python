from tkinter import * 

root = Tk()
root.geometry("800x600")

frame = Frame(root, width="400", height="300");
frame.pack()
frame.config(bd=2, 
			 relief="solid")

inputText = Entry(frame)
inputText.grid(row=0, column=1)#Sistema de Regilla
nomLabel = Label(frame, text="Nombre")
nomLabel.grid(row=0, column=0, sticky="e", pady=5) #Estableciendo, alineamiento de texto con Sticky, y padding con pady


inputApe = Entry(frame)
inputApe.grid(row=1, column=1)#Sistema de Regilla
apeLabel = Label(frame, text="Apellido")
apeLabel.grid(row=1, column=0, sticky="e", pady=5)


inputAddr = Entry(frame)
inputAddr.grid(row=2, column=1)#Sistema de Regilla
apeLabel = Label(frame, text="Dirección de casa")
apeLabel.grid(row=2, column=0, sticky="e", pady=5)

inputPass = Entry(frame)
inputPass.grid(row=3, column=1)#Sistema de Regilla
inputPass.config(show="*input(prompt)")
passLabel = Label(frame, text="Password")
passLabel.grid(row=3, column=0, sticky="e", pady=5)


button = Button(frame,text="Enviar");
button.grid(row=4, column=1, sticky="w")
button.config(bg="blue", fg="white", cursor="hand2")#Fg FONTGROUND color de letra


#Propiedad sticky->Alinear arriba abajo, derecha. Valores: Punto cardinales= "n,s,e,w" -> "nw, ne, sw, se,"

root.mainloop()