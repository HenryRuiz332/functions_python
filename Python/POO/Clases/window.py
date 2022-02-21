import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

    def tableSum(self):
    	num = 0
    	array = []

    	while num <= 10:
    		
    		num+=1
    		array.append(num)

    	return array

	

		

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.geometry("1000x400")

print(myapp.tableSum() )

# start the program
myapp.mainloop()