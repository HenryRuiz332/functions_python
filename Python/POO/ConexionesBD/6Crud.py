import sqlite3

#create DataBase
conexion = sqlite3.connect("gestionProductos2");#Se crea la conexión. Se asigna un nombre de BD

miCursor = conexion.cursor();#Crear cursor


# productosA = [
# 	("A33","ArrozConCaraota", 10, "Alimentos"),
# 	# ("A2","Harina", 10, "Alimentos"),
# 	# ("A3","Jabon", 10, "Detergente"),
# 	# ("A4","Mayonesa", 10, "Miscelaneos"),
# ];

#miCursor.execute("update productos set code='A333' where id=2");#Update products table
miCursor.execute("delete from productos where id=3");#delete products table
conexion.commit();


miCursor.execute("select * from productos"); 
data = miCursor.fetchall();
for x in data:
	print(x); #Luego se podran obtener indices


conexion.close();