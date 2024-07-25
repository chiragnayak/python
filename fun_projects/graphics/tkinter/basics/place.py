from tkinter import *

"""
pack : left, top, right, bottom
place : coordinates
grid : column and row (relative to previous widget)
"""

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.place(x=0, y=0)
# my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.place(x=10, y=50)

new_button = Button(text="New Button")
new_button.place(x=10, y=100)

#Entry
input = Entry(width=10)
print(input.get())
input.place(x=10, y=150)









window.mainloop()