from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("300x140")
root.title("Sliders tutorial")


def getdollar():
    print(f"We have credited ${my_sliders2.get()} from obama's account")
    tmsg.showinfo("Amount Credited", f"We have credited ${my_sliders2.get()} from obama's account")


Label(root, text="How many dollars do you want").pack()
my_sliders2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
my_sliders2.set(69)
my_sliders2.pack()
Button(root, text="Get started", pady=10, command=getdollar).pack()

root.mainloop()
