from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("1200x1000")
f1 = Frame(root, bg="grey", borderwidth=6, relief= SUNKEN)
f1.pack(side=LEFT,fill=Y)

f2 = Frame(root, bg="grey", borderwidth=6, relief= SUNKEN)
f2.pack(side=TOP,fill=X)

l = Label(f1, text="Project Tkinter- Pycharm", font="comicsansms 19")
l.pack(pady=142)

l1 = Label(f2, text="The Vampire Diaries", font="Helvetica 59 bold")
l1.pack()

image = Image.open("main.jpj.jpeg")
photo = ImageTk.PhotoImage(image)

py = Label(image=photo)
py.pack()

root.title("My First Gui")

title_label= Label(text= '''The Vampire Diaries is an American supernatural teen drama television series developed by Kevin 
 Williamson and Julie Plec, based on the book series of the same name written by L. J. Smith. The series 
 premiered on The CW on September 10, 2009, and concluded on March 10, 2017, having aired 171 episodes
 over eight seasons.''' , bg= "cyan",fg= "black",font= "Comicsansms 18 bold", borderwidth=3 , relief= GROOVE)

title_label.pack(side=TOP, fill= X)

root.mainloop()
