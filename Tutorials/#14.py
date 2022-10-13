from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("300x140")
root.title("Sliders tutorial")


def customer_experience():
    print(f"You rated {my_sliders2.get()} out of 10")
    value = f"You rated {my_sliders2.get()} out of 10"
    tmsg.showinfo("Thanks For Rating us", f"You rated {my_sliders2.get()} out of 10\n")
    with open("Ratings.txt", "a") as f:
        f.write(value)


Label(root, text="How was your experience").pack()
my_sliders2 = Scale(root, from_=0, to=10, orient=HORIZONTAL)
my_sliders2.pack()
Button(root, text="Submit", pady=10, command=customer_experience).pack()

root.mainloop()
