from tkinter import *
from datetime import date

window = Tk()
window.geometry("400x400")
window.title("Age calculator app")

lb = Label(text="Welcome to age calculator app", height=1, width=300)
lb2 = Label(text="Enter your name", height=1, width=300)
ent = Entry()
lbl3 = Label(text="Enter your birth year")
ent2 = Entry()
lbl4 = Label(text="Enter your birth month")
ent3 = Entry()
lbl5 = Label(text="Enter your birth day")
ent4 = Entry()

def cal():
    try:
        name = ent.get()
        year = int(ent2.get())
        month = int(ent3.get())
        day = int(ent4.get())
        today = date.today()
        birth_date = date(year, month, day)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        lbr.config(text=f"Current {name}'s age is {age}")
    except ValueError:
        lbr.config(text="Please enter valid numbers!")

lbr = Label(text="")
btn = Button(text="Calculate", command=cal, relief=SUNKEN)

lb.pack()
lb2.pack()
ent.pack()
lbl3.pack()
ent2.pack()
lbl4.pack()
ent3.pack()
lbl5.pack()
ent4.pack()
btn.pack()
lbr.pack()

window.mainloop()
