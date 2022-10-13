# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE


# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)


from tkinter import *
root= Tk()
root.geometry("300x300")
root.title("My First Gui")

title_label= Label(text= '''The Vampire Diaries is an American supernatural teen drama television series developed by Kevin 
 Williamson and Julie Plec, based on the book series of the same name written by L. J. Smith. The series 
 premiered on The CW on September 10, 2009, and concluded on March 10, 2017, having aired 171 episodes
 over eight seasons.''' , bg= "black",fg= "green",font= "Comicsansms 28 bold", borderwidth=3 , relief= GROOVE)

title_label.pack(side=TOP, fill= X)

root.mainloop()
