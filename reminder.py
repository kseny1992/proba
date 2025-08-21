from tkinter import *
from  tkinter import  messagebox as mb
from  tkinter import  simpledialog as sd
import datetime
import time
import  pygame #для работы со звуком

window = Tk()
window.title("Напоминание")
label = Label(text="установите напоминание")
label.pack(pady=10)
set_button = Button(text="установить", command = set)
set_button.pack()

window.mainloop()