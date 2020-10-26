
from  tkinter import *
import time

# Funcion para centrar la pantalla 
def center(toplevel):
       toplevel.update_idletasks()
       w = toplevel.winfo_screenwidth()
       h = toplevel.winfo_screenheight()
       size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
       x = w/2 - size[0]/2
       y = h/2 - size[1]/2
       toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
 
#FUNCION PARA ACTUALIZAR LA HORA
def times():
        current_time=time.strftime("%H:%M:%S")
        clock.config(text=current_time,bg="black",fg="#856ff8",font="Arial 50 bold")
        clock.after(200,times)
 
#VENTANA
root=Tk()
center(root)
root.geometry("485x250")
root.title("Reloj digital con Tkinter")
#root.configure(bg='#856ff8')
clock=Label(root,font=("times",50,"bold"))
clock.grid(row=2,column=1,pady=25,padx=100)
times()
 
 
digi=Label(root,text=" Hora Actual",font="times 24 bold",fg="black")
digi.grid(row=0,column=1)
 
root.mainloop()





"""# Reloj hecho con Python, Tkinter y time
from tkinter import *
import time
 
class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", font=("Calibri", 20))
        self.label.place(x=50,y=80)
        self.update_clock()
 
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)
 
root = Tk()
app=App(root)
root.title("Reloj")
root.configure(bg='#856ff8')
root.geometry("300x300")
root.resizable(width=False, height=False)
root.after(1000, app.update_clock)
root.mainloop()"""