import sqlite3


conexion = sqlite3.connect("pythonDBSQLITEconexion");#Se crea la conexión. Se asigna un nombre de BD

miCursor = conexion.cursor();#Crear cursor

#miCursor.execute("CREATE TABLE PRODUCTOS (nombre_articulo varchar(50), precio integer, seccion varchar(20))");


miCursor.execute(
	"select * from productos"
);#Execute: consulta registro

data = miCursor.fetchall();#FetchAll Devuelve una lista de registros de la instruccion anteriro

for x in data:
	print(f"productos : {x[0].lower()} , precio : {x[1]}" ) #or upper)#Ver data en minusculas 0 mayusculas


#conexion.commit();#confirmar cambios de la consulta anterior

conexion.close();