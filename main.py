from tkinter import *
from tkinter.ttk import *

from time import strftime

# root window is created
root = Tk()
root.title("Digital Clock")  # window name


# time method
def time():
    timex = strftime('%H:%M:%S %p')
    label.config(text=timex)
    label.after(1000, time)  # schedule an action after every second


label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()

mainloop()  # listens for events, such as button clicks or key presses, and blocks any code that comes after it from
# running until the window it's called on is closed
