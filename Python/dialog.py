import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button["text"] = "Nombre botón"
        self.button["command"] = self.say_hi #Llamado de funcion say_hi
        self.button.config(bg="blue", fg="#fff")
        self.button.pack(side="top")

        self.quit = tk.Button(self, text="Exit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()

app = Application(master=root)

app.mainloop()


