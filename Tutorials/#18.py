from tkinter import *

def upload():
    statusvar.set("Processing...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Executed")


root = Tk()
root.geometry("400x400")
root.title("Status Bar tut")

statusvar = StringVar()
statusvar.set("Press run to Execute")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X, pady=10)


f1 = Frame(root, bg="grey", borderwidth=6, relief= SUNKEN)
f1.pack()
Button(f1, text="RUN", command=upload).pack()

root.mainloop()
