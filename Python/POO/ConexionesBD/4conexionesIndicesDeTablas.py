import sqlite3

#create DataBase
conexion = sqlite3.connect("gestionProductos");#Se crea la conexión. Se asigna un nombre de BD

miCursor = conexion.cursor();#Crear cursor

#Query for create table
# miCursor.execute(
# "CREATE TABLE PRODUCTOS (id integer primary key AUTOINCREMENT, nombre_articulo varchar(50), precio integer, seccion varchar(20))"
# 	);#cREAR TABLA CON TABLA ID AUTOINCREMENT

productosA = [
	("Arroz", 10, "Alimentos"),
	("Harina", 10, "Alimentos"),
	("Jabon", 10, "Detergente"),
	("Mayonesa", 10, "Miscelaneos"),
];

miCursor.executemany("insert into productos values(null,?,?,?)", productosA);#Null. Python y el gestor de bases de datos, se enncargaran de llenar el campo clave
# conexion.commit();#confirmar cambios de la consulta anterior

miCursor.execute("select * from productos"); #Consulta a database

data = miCursor.fetchall();#Obtain data

for x in data:
	print(x); #Luego se podran obtener indices



conexion.close();