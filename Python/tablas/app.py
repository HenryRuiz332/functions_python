from clases.TableClass import *

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.geometry("1100x600")
myapp.master.resizable(0,0)


frame = Frame(myapp);
frame.pack(side="left", anchor="w")
frame["width"] = 200;
frame["height"] = 200;
frame.config(bg="#0ff")
frame.grid(row=1, column=1)


button = Label(frame,text=f"{myapp.tableSum()}")
button.grid(row=0, column=1, sticky="w")
button.config(bg="blue", fg="white", cursor="hand2")

# start the program
myapp.mainloop()