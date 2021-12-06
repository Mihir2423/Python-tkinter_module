from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("400x400")
root.title("Radio Button Tutorial")


def order():
    tmsg.showinfo("Order Recieved", f"We have recieved your order for {var.get()}.Thanks for ordering")


var = StringVar()
var.set("Radio")

Label(root, text="What would you like to order", font="lucida 19 bold", justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idli", padx=14, variable=var, value="Idli").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Biryani", padx=14, variable=var, value="Biryani").pack(anchor="w")

Button(root, text="Submit Your Order", command=order).pack()


root.mainloop()
