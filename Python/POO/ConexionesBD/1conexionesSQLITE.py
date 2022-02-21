import sqlite3


def conexion():
	conexion = sqlite3.connect("pruebaDeModulo");#Se crea la conexión. Se asigna un nombre de BD

	miCursor = conexion.cursor();#Crear cursor

	#miCursor.execute("CREATE TABLE PRODUCTOS (nombre_articulo varchar(50), precio integer, seccion varchar(20))");

	