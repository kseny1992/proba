from tkinter import *
from  tkinter import  messagebox as mb
from  tkinter import  simpledialog as sd
import datetime
import time
import  pygame #для работы со звуком

def set(): #установка
    rem = sd.askstring("время напоминания", "введите время напоминания в формате ЧЧ:ММ (в 24 часовом формате)")
    if rem:
        try:
            hour = int(rem.split(":")[0]) #делим на строку из двух символов = часы(нулевой элемент строки) и минуты
            minute=int(rem.split(":")[1]) #аналогично
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour,minute=minute) #заменяем часы на новые часы и минуты заменяем на минуты
            #получим текущее время в котором изменены часы и минуты
            print(dt)
            t=dt.timestamp()#получить временнУю метку в млд секунд
            print(t)
        except EXCEPTION as e:
            mb.showerror(("ошибка",f"произошла ошибка: {e}"))


window = Tk()
window.title("Напоминание")
label = Label(text="установите напоминание")
label.pack(pady=10)
set_button = Button(text="установить", command = set)
set_button.pack()

window.mainloop()