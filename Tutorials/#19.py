from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("You just Clicked Me")

    def createbutton(self, imptext):
        l1 = Frame(self, relief=SUNKEN, padx=5, bg="red", bd=10)
        l1.pack()
        Button(l1, text=imptext, command=self.click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Click me")
    window.mainloop()
