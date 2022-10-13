from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("700x600")
root.title("Python")


def my_func():
    print("Miir OP")


def Help():
    print("I will help you")
    tmsg.showinfo("Help", "Mihir will help you")

def rateus():
    print("Rate us")
    value = tmsg.askquestion("How was your experience", "Good")
    if value == "yes":
        msg = "Great, Rate us on appstore please"
        tmsg.showinfo("Experience", msg)
    else:
        msg = "want went wrong, tell us please"
        tmsg.showinfo("Experience", msg)


def Kill():
    ans = tmsg.askretrycancel("Kill someone", "Kill Lion")
    if ans:
        print("Nice keep trying")
    else:
        print("Noob")


your_menu = Menu(root)
m1 = Menu(your_menu, tearoff=0)
m1.add_command(label="New project", command=my_func)
m1.add_command(label="Save", command=my_func)
m1.add_separator()
m1.add_command(label="Save as", command=my_func)
m1.add_command(label="Print", command=my_func)
root.config(menu=your_menu)
your_menu.add_cascade(label="File", menu=m1)

m2 = Menu(your_menu, tearoff=0)
m2.add_command(label="New project", command=my_func)
m2.add_command(label="Save", command=my_func)
m2.add_separator()
m2.add_command(label="Save as", command=my_func)
m2.add_command(label="Print", command=my_func)
root.config(menu=your_menu)
your_menu.add_cascade(label="Edit", menu=m2)

m3 = Menu(your_menu, tearoff=0)
m3.add_command(label="Help", command=Help)
m3.add_command(label="Rate", command=rateus)
m3.add_command(label="Kill", command=Kill)
root.config(menu=your_menu)
your_menu.add_cascade(label="Help", menu=m3)


root.mainloop()
