from tkinter import *
root = Tk()

root.geometry("700x600")


def hello():
    print("Hello user")


def name():
    print("Your name is Mihir")


f1 = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")

b1 = Button(f1, bg="red", text="Print", command=hello)
b1.pack(side=LEFT, padx=5)

b2 = Button(f1, bg="red", text="Name", command=name)
b2.pack(side=LEFT, padx=5)

root.mainloop()
