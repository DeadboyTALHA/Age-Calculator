from tkinter import *
from datetime import date

fun = Tk()
fun.geometry("800x600")
fun.resizable(False, False)
fun.title("Talha's Age Calculator")

photo = PhotoImage(file = "Age Calculator.png")
myimage = Label(image = photo)
myimage.pack(padx = 15, pady = 15)

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text = f"{nameValue.get()}, your age is {age}", font = 30).place(x = 300, y = 500)

Label(text = "Name", font = 23).place(x = 200, y = 250)
Label(text = "Year", font = 23).place(x = 200, y = 300)
Label(text = "Month", font = 23).place(x = 200, y = 350)
Label(text = "Day", font = 23).place(x = 200, y = 400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(fun, textvariable = nameValue, width = 30, bd = 3, font = 20)
nameEntry.place(x = 300, y = 250)

yearEntry = Entry(fun, textvariable = yearValue, width = 30, bd = 3, font = 20)
yearEntry.place(x = 300, y = 300)

monthEntry = Entry(fun, textvariable = monthValue, width = 30, bd = 3, font = 20)
monthEntry.place(x = 300, y = 350)

dayEntry = Entry(fun, textvariable = dayValue, width = 30, bd = 3, font = 20)
dayEntry.place(x = 300, y = 400)

Button(text = "Calculate Age", font = 20, bg = "black", fg = "white", width = 11, height = 2, command = calculateAge).place(x = 300, y = 450)

fun.mainloop()