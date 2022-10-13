from tkinter import *
root= Tk()
root.geometry("250x200")


def get_values():
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")


root.title("EXERCISE")

Label(text="Window Resizer", font="comicsansms 13 bold", pady=20).grid(column=2)
Label(text="Width", font="comicsansms 13 bold").grid(row=1, column=1)
Label(text="Height", font="comicsansms 13 bold").grid(row=2, column=1)

width = StringVar()
height = StringVar()

width_entry = Entry(root, textvariable=width)
height_entry = Entry(root, textvariable=height)

width_entry.grid(row=1, column=2)
height_entry.grid(row=2, column=2)

Button(root, text="SUBMIT", command=get_values).grid(row=3, column=2)

root.mainloop()

