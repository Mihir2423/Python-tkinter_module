from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("300x300")

image = Image.open("main.jpj.jpeg")
photo = ImageTk.PhotoImage(image)

py = Label(image=photo)
py.pack()

root.mainloop()
