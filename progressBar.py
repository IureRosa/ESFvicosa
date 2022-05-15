from tkinter import *
from tkinter import ttk
import time

def valBarra():
    x = 0
    while True:
        varBarra.set(x)
        if x < 100:
            x = x + 1
            time.sleep(0.01)
            appPB.update()
            continue
        else:
            try:
                appPB.destroy()
            except:
                break

appPB=Tk()
appPB.title('Controle de Presença')
appPB.geometry('300x40')

varBarra=DoubleVar()
varBarra.set(0)

pb=ttk.Progressbar(appPB, variable=varBarra, maximum=100)
pb.place(x=15, y=10, width=270, height=20)

valBarra()