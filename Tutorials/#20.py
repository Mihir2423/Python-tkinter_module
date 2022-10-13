from tkinter import *

root = Tk()
root.geometry("700x400")
root.title("MY GUI")
root.wm_iconbitmap("1.ico")
root.configure(background="black")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()

root.mainloop()
