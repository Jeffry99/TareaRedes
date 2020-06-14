from tkinter import *
from tkinter.ttk import *

window = Tk()

image = PhotoImage(file = r"Imagenes\Triangulo.png")
Button(window, text = 'Click Me !', image = image).pack(side = TOP) 
  
mainloop()
