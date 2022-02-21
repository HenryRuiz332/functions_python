#Theme: Calculadora
#Author: Henry Ruiz
#GitLab: solid2819
#Version: 0.1

from tkinter import *

root = Tk()
root.title("Calculadora")
root.resizable(0,0)
root.geometry("400x500")

numberView = StringVar()#cadena de caracteres que se verá en la pantalla

frame = Frame()
frame.pack()

operations = "" #Variable para reaizar las operaciones y resetear numberView
result = 0 #Almacenara datos de valores introducidos en  pantalla
################
#
#InputResult
#
################
#Imput donde se mostrara resultados de operaciones de la calculadora
inputResult = Entry(frame, textvariable=numberView)#Propiedad textvariable, para llamar a la variable que mostrará los números
inputResult.pack(
	side="left",
	anchor="e",
)

#Config imput
inputResult.config(
	bg="gray", 
	fg="#03f943", 
	font="11",
	justify="right",
	width=40
)

#Config grid
inputResult.grid(
	row=1, 
	column=1, 
	pady=15, 
	sticky="w",
	columnspan=4
)

################
#
#Funciones de calculadora
#
################

####Función de concatenar caracteres pulsados.
def numberPulsado(num):
	global operations
	
	#Si se ha pulsado un boton de operacion, no concatene caracteres, de lo contrario que si lo haga
	if operations != "":
		numberView.set(num)
		operations = ""
	else:
		#numberView.set(numberView.get() + num) = concatenar lo que haya en pantalla, con lo siguiente que se ha pulsado
		numberView.set(numberView.get() + num)

####Operaciones de Suma
def suma(num):
	global operations
	global result

	result+=int(num)
	operations = "suma";

	numberView.set(result)

####Operaciones de Suma
def resta(num):
	global operations
	global result
	operations = "resta";

	result-=int(num)
	numberView.set(result)

####Operaciones de Multiplicacion
def multiplicar(num):
	global operations
	global result
	operations = "multiplicar";

	result*int(num)
	numberView.set(result)

#####Resultados de operaciones
def resultsAll():
	global result

	#Suma el resultado de lo que hay almacenado previamente + lo que esta en pantalla al pulsar el boton igual 
	numberView.set(result + int(numberView.get()))
	result=0





################
#
#Buttons
#
################

#Fila 1: 7-8-9-/
#Lambda:Pone a la función a la espera para que sea llamada

seven = Button(frame, text="7", width=3,  command=lambda:numberPulsado("7")) #command: LLama a la función de numberPulsado
seven.grid(pady=5, row=2,column=1, sticky="w")
seven.config(width=10)

eight = Button(frame, text="8", width=3,  command=lambda:numberPulsado("8"))
eight.grid(pady=5, row=2,column=2)
eight.config(width=10)

nine = Button(frame, text="9", width=3,  command=lambda:numberPulsado("9"))
nine.grid(pady=5, row=2,column=3)
nine.config(width=10)

div = Button(frame, text="/", width=3)
div.grid(pady=5, row=2,column=4)
div.config(width=10)


#Fila 2: 4-5-6-/
four = Button(frame, text="4", width=3, command=lambda:numberPulsado("4"))
four.grid(pady=5, row=3,column=1, sticky="w")
four.config(width=10)

five = Button(frame, text="5", width=3, command=lambda:numberPulsado("5"))
five.grid(pady=5, row=3,column=2)
five.config(width=10)

six = Button(frame, text="6", width=3,  command=lambda:numberPulsado("6"))
six.grid(pady=5, row=3,column=3)
six.config(width=10)

mul = Button(frame, text="x", width=3, command=lambda:multiplicar(numberView.get()))
mul.grid(pady=5, row=3,column=4)
mul.config(width=10)


#Fila 3: 1-2-3- -menos
one = Button(frame, text="1", width=3,  command=lambda:numberPulsado("1"))
one.grid(pady=5, row=4,column=1, sticky="w")
one.config(width=10)

two = Button(frame, text="2", width=3,  command=lambda:numberPulsado("2"))
two.grid(pady=5, row=4,column=2)
two.config(width=10)

three = Button(frame, text="3", width=3,  command=lambda:numberPulsado("3"))
three.grid(pady=5, row=4,column=3)
three.config(width=10)

men = Button(frame, text="-", width=3, command=lambda:resta(numberView.get()))
men.grid(pady=5, row=4,column=4)
men.config(width=10)


#Fila 4: 0-coma-igual- +mas
zero = Button(frame, text="0", width=3,  command=lambda:numberPulsado("0"))
zero.grid(pady=5, row=5,column=1, sticky="w")
zero.config(width=10)

coma = Button(frame, text=",", width=3,  command=lambda:numberPulsado(","))
coma.grid(pady=5, row=5,column=2)
coma.config(width=10)

equal = Button(frame, text="=", width=3, command=lambda:resultsAll())
equal.grid(pady=5, row=5,column=3)
equal.config(width=10)

mas = Button(frame, text="+", width=3, command=lambda:suma(numberView.get()))#Pasar el numero al numberView Tect
mas.grid(pady=5, row=5,column=4)
mas.config(width=10)






root.mainloop()