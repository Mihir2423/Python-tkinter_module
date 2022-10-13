from tkinter import *


def mihir(event):
    print(f"You clicked me at {event.x} , {event.y}")


root = Tk()
root.geometry("800x400")

widget= Button(root, text="Click me please")
widget.pack()

widget.bind('<Button-1>', mihir)
widget.bind('<Double-1>', quit)


root.mainloop()
