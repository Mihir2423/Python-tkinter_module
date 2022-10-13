from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i = i + 1


i = 0
root = Tk()
root.geometry("300x300")
root.title("Listbox Tut")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item in our listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()
