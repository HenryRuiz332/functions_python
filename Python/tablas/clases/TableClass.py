import tkinter as tk

from tkinter import * 

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()



    #Table  Suma
    def tableSum(self):
    	num = 0
    	array = []

    	while num <= 10:
    		
    		num+=1
    		array.append(num)

    	for i in array:
             print( array.append(i))

