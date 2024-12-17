from tkinter import *
import time

m=Tk()
m.title('Digital Clock')
m.config(bg="skyblue")
m.geometry("500x500")

l=Label(m,text="Digital Clock ",font="Georgia 25 bold",bg="pink")
l.place(x=150,y=50)


def T():

	h=time.strftime('%I')
	m=time.strftime('%M')
	s=time.strftime('%S')
	day=time.strftime('%A')
	am_pm=time.strftime('%p')


	l.config(text=f"{h}:{m}:{s}:{am_pm}\n {day}",font=("Calibri 30 bold"))
	l.after(1,T)


l=Label(m,text="",font="Georgia 25 bold",bg="yellow")
l.place(x=150,y=200,width=220)

T()



m.mainloop()
