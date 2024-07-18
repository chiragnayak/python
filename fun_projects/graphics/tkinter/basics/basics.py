from tkinter import *

window = Tk()
# all your code goes here
window.title("Hello, welcome to tkinter world !")
window.minsize(width=500, height=300)

label = Label(text="I am a label", font=("Arial", 16, "bold"))
label.pack()

count = 0


def button_clicked():
    global count
    count = count + 1
    label.config(text="I got clicked "+str(count)+" times")


button = Button(text="Click Me plz !", command=button_clicked)
button.pack()

# ------ all your code above this
window.mainloop()
