import sqlite3


conexion = sqlite3.connect("pythonDBSQLITEconexion");#Se crea la conexión. Se asigna un nombre de BD

miCursor = conexion.cursor();#Crear cursor

#miCursor.execute("CREATE TABLE PRODUCTOS (nombre_articulo varchar(50), precio integer, seccion varchar(20))");

variosProductos = [
	("Camiseta", 10, "Deportes"),
	("Pantalon", 13, "Telas"),
	("Jarron", 12, "Ceramica"),
];

miCursor.executemany(
	"insert into productos values (?,?,?)", variosProductos
);#Execute: Inserta Varios registros
conexion.commit();#confirmar cambios de la consulta anterior

conexion.close();