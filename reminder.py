from tkinter import *
from  tkinter import  messagebox as mb
from  tkinter import  simpledialog as sd
import datetime
import time
import  pygame #для работы со звуком

t=None #глобальная
music=False #переменная для отслеживания проигрывания музыки музыка не играет при запуске программы
def set(): #установка

    global t

    rem = sd.askstring("время напоминания", "введите время напоминания в формате ЧЧ:ММ (в 24 часовом формате)")
    if rem:
        try:
            hour = int(rem.split(":")[0]) #делим на строку из двух символов = часы(нулевой элемент строки) и минуты
            minute=int(rem.split(":")[1]) #аналогично
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour,minute=minute,second=0,microsecond=0) #заменяем часы на новые часы и минуты заменяем на минуты
            #получим текущее время в котором изменены часы и минуты и обнуляем секунды
            print(dt)
            t=dt.timestamp()#получить временнУю метку в млд секунд
            print(t)
            label.config(text= f"Напоминание установлено на: {hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка","Неверный формат времени")
        except EXCEPTION as e:
            mb.showerror(("ошибка",f"произошла ошибка: {e}"))
def check(): #
    global t
    if t:#если не пустая
        now = time.time() #время которое сейчас
        if now>=t: #ecли >= то вкл напоминание
            play_snd()
            t=None #обнуляем
    window.after(10000, check) #вызываем функцию чек через 10 секунд автоматически (6 раз в минуту) - рекурсия


def play_snd():#
    global music #
    music = True #
    pygame.mixer.init()#инициализируем миксер который играет музыку
    pygame.mixer.music.load("reminder.mp3") #загружаем музыку
    pygame.mixer.music.play() #включение музыки


def stop_music():
    global music
    if music: #если музыка играет то стоп
        pygame.mixer.music.stop()
        music=False
    label.config(text="Установить новое напоминание")


window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание")
font = ("Arial",14)#более крупный шрифт
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command = set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music) #отключение напоминания
stop_button.pack(pady=5)

check()

window.mainloop()