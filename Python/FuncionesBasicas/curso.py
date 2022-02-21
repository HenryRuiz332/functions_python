print("mi nombre es\nHenry")
#Comentario
rango=0

for i in range(5):
	rango+=1
	print(rango);



############################################################
############################################################
print("Video 5 => Funciones"); 
def mensaje(): #def= definir una nueva funcion
	print("Estamos aprendiendo Python")
	print("Este es un mensaje de prueba")

#print(mensaje())
mensaje()#Imprimiendo la funcion.
print("Ejecutando otras lineas de código")
mensaje()

############################################################
############################################################
print("_______________________________________________")
print("Video 6 => Funciones con parametros o argumento")

def suma():
	numero1 = 1;
	numero2 = 2;
	resultadoSuma = numero1 + numero2;
	print(resultadoSuma);

suma();

def sumaParam(num1, num2):
	resultadoParam = num1+num2;
	print(resultadoParam);

print("Suma de parametros o argumentos");
sumaParam(3,6);
sumaParam(10,11);
sumaParam(4,4);

def restaParam(obj1, obj2):
	resultadoResta = obj1 - obj2;
	return resultadoResta;
	print(resultadoResta)
print("Resta de parametros o argumentos");
print(restaParam(10, 43));
print(restaParam(2, 33));



############################################################
############################################################
print("__________________________")
print("Video7 => Listas => Arrays")

def lista():
	listaString = ["Nombre1","Nombre2","Nombre3","Nombre4"];
	listaNumerica = [0,1,2,3,4,5,6,7,8,9,10];
	print("Accediendo a la lista del string en la posicion 3. indice [0]")
	print(listaString[3]);#Accediendo al elemento del array

	print("Accediendo a todos los elementos del array")
	print(listaNumerica[:]);#Accediendo al elemento del array.

	print("Accediendo a una porción del indice")
	print(listaNumerica[1:5]);#Accediendo a una proción del indice.

	print("Agregar un elemento a lista metodo append()")
	print(listaString.append("Henry"), "Agregando un elemento al final de una lista");#Agregando un elemento al final de una lista
	print(listaString.insert(2,"Henry"), "Agregando un elemento a una posicion determinada");#Agregando un elemento a una posicion determinada
	print(listaString.extend(["Henry", "Manuel", "Bryan", "Luis"]), "Extendiendo un array");
	print("Indice", listaString.index("Henry"), "//Encontrar un indice");
lista();

print("_________________")
print("Video 8 => Tuplas")

def tupla():
	tupla = (1,2,4,8);
	tupla2 = ("Henry", "28-19-91")
	print(tupla);print(tupla2);
	print("Verificar si un string esta dentro de la tupla: "); 
	print("Henry" in tupla2)
	print("Verificar Cuantas Veces esta el elemento dentro de la Tupla")
	print(tupla2.count("Henry"))
tupla();


print("_________________")
print("Video 10 => Condicionales IF")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion = "No has aprobado odavia"
	return valoracion;

print(evaluacion(3));

print("Por defecto ela funion input solo admite string. La pasamos a integer con int()");
notaAlumno = int(input("Introduccir nota: "))
def evaluacion(nota):
	print("Introduccion de valores por teclado de notas de alumnos");
	
	valoracion="aprobado"
	if nota<5:
		valoracion = "No has aprobado todavia"
	return valoracion;

print(evaluacion(notaAlumno));







