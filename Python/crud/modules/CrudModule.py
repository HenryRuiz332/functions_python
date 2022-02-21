from tkinter import *
from modules.conectLite import *

class Crud():

	def __init__(self):
		#Elementos de Menu
		self.bd = "BD"
		self.borrar = "Borrar"
		self.crud = "Crud"
		self.ayuda = "Ayuda"


		self.arrayMenu = [self.bd, self.borrar, self.crud, self.ayuda]

		self.myRoot=Tk()
		self.geometry = self.myRoot.geometry("800x500")
		self.myFrame=Frame(self.myRoot, width="300", height="300")

		#StringVar
		self.miId = StringVar()
		self.miName = StringVar()
		self.miLastName = StringVar()
		self.miPass = StringVar()
		self.miaddress = StringVar()

		print(self.geometry)

	def conectin(self):
		conect()# connect To data base sqlite
	
	#Crear registros
	def create(self):
		miconexion = sqlite3.connect("usuarios")

		cursor = miconexion.cursor()

		cursor.execute("INSERT INTO datos_usuarios VALUES(NULL, '" + self.miName.get() +  
			"', '" + self.miLastName.get() +
			"', '" + self.miPass.get() + 
			"', '" + self.miaddress.get() +
			"', '" + self.comentarios.get("1.0", END) + "')")

		miconexion.commit()
		messagebox.showinfo("Info", "Registro insertado con éxito!")
		self.resetFields()

	#Leer registros
	def read(self):
		miconexion = sqlite3.connect("usuarios")
		cursor = miconexion.cursor()

		cursor.execute("SELECT * FROM datos_usuarios WHERE id = " + self.miId.get())

		#Devuelve array con los registros
		readUser = cursor.fetchall()
		print(readUser)

		for user in readUser:
			self.miId.set(user[0])
			self.miName.set(user[1])
			self.miLastName.set(user[2])
			self.miaddress.set(user[3])
			self.comentarios.insert(1.0, user[4])

		miconexion.commit()
		miconexion.close()


	def update(self):
		miconexion = sqlite3.connect("usuarios")

		cursor = miconexion.cursor()

		cursor.execute("UPDATE datos_usuarios SET nombre = '" + self.miName.get() + 
		"', apellido='"  + self.miLastName.get() +
		"', direccion='" + self.miaddress.get() +
		"', password='"  + self.miPass.get() +
		"', comentarios='" + self.comentarios.get("1.0", END) + 
		"'  wHERE id=" + self.miId.get())


		miconexion.commit()
		messagebox.showinfo("Info", "Informacion Actualizado con éxito!")

	def delete(self):
		validar
		else:
			miconexion = sqlite3.connect("usuarios")

			cursor = miconexion.cursor()

			cursor.execute("DELETE from datos_usuarios where id=" + self.miId.get())

			miconexion.commit()
			messagebox.showinfo("Info", "Registro Borrado!")
			self.resetFields()


	def root(self):
		self.myRoot.title("Crud")
		self.myRoot.resizable(0,0)
		self.barMenu = Menu(self.myRoot)
		self.myRoot.config(menu=self.barMenu)


	def navbar(self):
		#Nombre menu
		bdMenu = Menu(self.barMenu, tearoff=0)
		#Submenu
		bdMenu.add_command(label="Conectar", command=self.conectin)
		bdMenu.add_command(label="Salir", command=self.exit)

		resetMenu = Menu(self.barMenu, tearoff=0)
		resetMenu.add_command(label="Borrar", command=self.resetFields)

		crudMenu = Menu(self.barMenu, tearoff=0)
		crudMenu.add_command(label="Crear", command=self.create)
		crudMenu.add_command(label="Leer",  command=self.read)
		crudMenu.add_command(label="Actualizar", command=self.update)
		crudMenu.add_command(label="Borrar",command=self.delete)

		helpMenu = Menu(self.barMenu, tearoff=0)
		helpMenu.add_command(label="Ayuda")
		helpMenu.add_command(label="Saber más")

		arrayMenuCreate = [bdMenu, resetMenu, crudMenu, helpMenu]

		count = 0

		for i in arrayMenuCreate:
			while count <= 3 :
				self.barMenu.add_cascade(label=f"{self.arrayMenu[count]}", menu=arrayMenuCreate[count])
				count+=1

	def frame(self):
		self.myFrame.pack(fill="y", expand=True, anchor="w")
		self.myFrame.config(bg=None)

		#Call function entrys
		self.entrys()

	def resetFields(self):
		#StringVar
		self.miId.set("")
		self.miName.set("")
		self.miLastName.set("")
		self.miPass.set("")
		self.miaddress.set("")

		self.comentarios.delete(1.0, END)
		
	def entrys(self):

		ids = "ID: "
		name = "Nombre: "
		lastName = "Apellido: "
		address = "Dirección: "
		self.password = "Password: "
		self.comments = "Comentarios"

		
		

		identificador = Entry(self.myFrame, textvariable=self.miId)#textvariable=stringVar
		identificador.grid(row=0, column=1, padx=5, pady=5)
		labelId = Label(self.myFrame, text=f"Información id: ")
		labelId.grid(row=0, column=0, sticky="e", pady=5)

		nombre = Entry(self.myFrame, textvariable=self.miName)#textvariable=stringVar
		nombre.grid(row=1, column=1, padx=5, pady=5)
		labelNombre = Label(self.myFrame, text=f"Nombre")
		labelNombre.grid(row=1, column=0, sticky="e", pady=5)

		apellido = Entry(self.myFrame, textvariable=self.miLastName)#textvariable=stringVar
		apellido.grid(row=2, column=1, padx=5, pady=5)
		labelApe = Label(self.myFrame, text=f"Apellido")
		labelApe.grid(row=2, column=0, sticky="e", pady=5)

		direccion = Entry(self.myFrame, textvariable=self.miaddress)#textvariable=stringVar
		direccion.grid(row=3, column=1, padx=5, pady=5)
		labelDireccion = Label(self.myFrame, text=f"Dirección")
		labelDireccion.grid(row=3, column=0, sticky="e", pady=5)

		password = Entry(self.myFrame, textvariable=self.miPass)#textvariable=stringVar
		password.grid(row=4, column=1, padx=5, pady=5)
		password.config(show="*")
		labelPass = Label(self.myFrame, text=f"Password")
		labelPass.grid(row=4, column=0, sticky="e", pady=5)


		#Label and Input for Comments Crud
		self.comentarios = Text(self.myFrame, width=16, height=5)
		self.comentarios.grid(row=5, column=1, padx=5, pady=5)
		self.scrollerComments()

		labelComentarios = Label(self.myFrame, text="Comentarios: ")
		labelComentarios.grid(row=5, column=0, sticky="e", pady=5)

		

		# self.arrayStringVar  = [midId, miName, miLastName,  miaddress, self.miPass]

		# arrayEntrys 	= [ids, name, lastName, address, self.password, self.comments]
		# loopLabels = 0



		# for x in arrayEntrys:
		# 	while loopLabels <= 5:
		# 		stringValue = arrayEntrys[loopLabels]
		# 		stringVar = self.arrayStringVar[loopLabels]

		# 		if loopLabels == 4:
		# 			self.password = Entry(self.myFrame, textvariable=self.miPass)
		# 			self.password.grid(row=loopLabels, column=2, padx=5, pady=5)
		# 			self.password.config(show="*")
		# 			label = Label(self.myFrame, text=f"{arrayEntrys[loopLabels]}")
		# 			label.grid(row=loopLabels, column=1, sticky="e", pady=5)

		# 		elif loopLabels == 5:
		# 			#Label and Input for Comments Crud
		# 			self.comments = Text(self.myFrame, width=16, height=5)
		# 			self.comments.grid(row=5, column=2, padx=5, pady=5)
		# 			self.scrollerComments()

		# 			label = Label(self.myFrame, text="Comentarios: ")
		# 			label.grid(row=5, column=1, sticky="e", pady=5)
		# 		else:
		# 			stringValue = Entry(self.myFrame, textvariable=stringVar)
		# 			stringValue.grid(row=loopLabels, column=2, padx=5, pady=5)
		# 			label = Label(self.myFrame, text=f"{arrayEntrys[loopLabels]}")
		# 			label.grid(row=loopLabels, column=1, sticky="e", pady=5)

		# 		loopLabels+=1
				# print(loopLabels)


	def scrollerComments(self):
		scrollvert = Scrollbar(self.myFrame, command=self.comentarios.yview)
		scrollvert.grid(row=5,column=2, sticky="nsew")
		scrollvert.config(width=3)
		self.comentarios.config(yscrollcommand=scrollvert.set)


	def buttons(self):
		#Generate Loops of buttons
		# loopButtons = 0
		# #Call property arraymenu
		# for i in self.arrayMenuCrud:
		# 	# print(i)
		# 	while loopButtons <= 3:
		# 		valueButton = f"buttton-{self.arrayMenuCrud[0]}"

		# 		if valueButton == "buttton-Crear":
		# 	 		valueButton = Button(self.myFrame, text=f"{self.arrayMenuCrud[loopButtons]}")
		# 	 		valueButton.grid(row=6, column=loopButtons, sticky="w")
		# 	 		valueButton.config(bg="blue", fg="white", cursor="hand2", width=10)
		# 		loopButtons+=1

		valueButton = Button(self.myFrame, text="Crear",  command=self.create)
		valueButton.grid(row=6, column=0, sticky="w")
		valueButton.config(bg="blue", fg="white", cursor="hand2", width=10)

		valueButton = Button(self.myFrame, text="Leer",  command=self.read)
		valueButton.grid(row=6, column=1, sticky="w")
		valueButton.config(bg="blue", fg="white", cursor="hand2", width=10)

		valueButton = Button(self.myFrame, text="Actualizar", command=self.update)
		valueButton.grid(row=6, column=2, sticky="w")
		valueButton.config(bg="blue", fg="white", cursor="hand2", width=10)

		valueButton = Button(self.myFrame, text="Borrar", command=self.delete)
		valueButton.grid(row=6, column=3, sticky="w")
		valueButton.config(bg="blue", fg="white", cursor="hand2", width=10)


	def exit(self):
		exitDialog	= messagebox.askquestion("Salir", "Deseas salir de la aplicación")

		if exitDialog == "yes":
			self.myRoot.destroy()
		else:
			pass


	def mainloopcrud(self):
		
		self.myRoot.mainloop()

