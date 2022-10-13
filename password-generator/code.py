from tkinter import *
from tkinter.ttk import *
import random
import pyperclip
from tkinter.messagebox import showinfo


def low():
    entry.delete(0, END)
    length = value1.get()
    easy = "abcdefghijklmnopqrstuvwxyz"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    hard = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if value.get() == 1:
        for i in range(0, length):
            password = password + random.choice(easy)
        return password

    elif value.get() == 0:
        for i in range(0, length):
            password = password + random.choice(medium)
        return password
    elif value.get() == 3:
        for i in range(0, length):
            password = password + random.choice(hard)
        return password
    else:
        print("Please choose an option")


def copy_password():
    password = entry.get()
    pyperclip.copy(password)


def generate():
    password1 = low()
    entry.insert(10, password1)


def about():
    showinfo("Help", "Made by Mihir")


if __name__ == '__main__':
    root = Tk()
    value = IntVar()
    value1 = IntVar()
    root.geometry("550x80")
    root.resizable(0, 0)
    root.title("Password generator")

    MenuBar = Menu(root)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="Help", command=about)
    MenuBar.add_cascade(label="About", menu=HelpMenu)
    root.config(menu=MenuBar)

    l = Label(root, text="Password")
    l.grid(row=0)
    entry = Entry(root)
    entry.grid(row=0, column=1)

    l1 = Label(root, text="Length")
    l1.grid(row=1)

    b1 = Button(root, text="Copy", command=copy_password)
    b1.grid(row=0, column=2)
    b2 = Button(root, text="Generate", command=generate)
    b2.grid(row=0, column=3)

    r1 = Radiobutton(root, text="Easy", variable=value, value=1)
    r1.grid(row=1, column=2, sticky="E")
    r2 = Radiobutton(root, text="Medium", variable=value, value=0)
    r2.grid(row=1, column=3, sticky="E")
    r3 = Radiobutton(root, text="Hard", variable=value, value=3)
    r3.grid(row=1, column=4, sticky="E")
    combo = Combobox(root, textvar=value1)
    combo['values'] = (7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
    combo.current(0)
    combo.bind('<<ComboboxSelected>>')
    combo.grid(row=1, column=1)

    root.mainloop()
