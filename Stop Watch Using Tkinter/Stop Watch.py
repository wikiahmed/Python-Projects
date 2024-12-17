from tkinter import *
import time

w = Tk()
w.title('Stop Watch')
w.geometry("500x600")
w.config(bg='#00ffff')
h = 0
m = 0
s = 0

Label(w, text="STOP WATCH", font="Ariel 25").place(x=150, y=50)

canvas = Canvas(w, width=500, height=450, bg="yellow")
canvas.place(x=10, y=200)
r = canvas.create_rectangle(6, 100, 480, 350, fill="red")

def update():   
    l.config(text=f"{h:02d} : {m:02d} : {s:02d}")
    l.after(1000, tick)

def tick():
    global s, m, h
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    update()

l = Label(w, text="", font="Calibri 35")
l.place(x=150, y=400)

tick()

w.mainloop()
