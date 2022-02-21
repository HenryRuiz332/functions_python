from tkinter import messagebox
import sqlite3

def conect():
	
	conexion = sqlite3.connect("usuarios")

	cursor=conexion.cursor()

	try:
		cursor.execute('''
			CREATE TABLE datos_usuarios(
			id integer primary key AUTOINCREMENT,
			nombre varchar(50),
			password varchar(50),
			apellido varchar(60),
			direccion varchar(50),
			comentarios varchar(200)) ''')

		messagebox.showinfo("Base de Datos", "Base de datos creada")
	except:
		messagebox.showwarning("Error", "La base de datos ya existe")
	