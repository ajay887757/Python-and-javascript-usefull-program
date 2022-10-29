from curses import window
from tkinter import *
import time
import sys
from functools import partial
root = Tk()
root.geometry('400x300')
root.resizable(0,0)
root.config(bg ='snow')
root.title('Manoj Project')
Label(root, text = 'Countdown Clock and Timer' , font = 'arial 20 bold',  bg ='snow').pack()


Label(root, font ='arial 15 bold', text = 'current time :', bg = 'snow').place(x = 40 ,y = 70)
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='snow')
curr_time.place(x = 190 , y = 70)
clock()


sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')


def countdown(stop=None):
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
      
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        window=root


   
        root.update()
        if stop==1:
            window.destroy()
            print("Hello World")
            sys.exit()

        if stop==2:
            pause = True
            # mins, secs = divmod(times, 60)
            # hours = 0
            # if mins > 60:
            #     # hour minute
            #     hours, mins = divmod(mins, 60)

            sec.set(second)
            mins.set(minute)
            hrs.set(hour)
           
        time.sleep(1)
        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1

Label(root, font ='arial 15 bold', text = 'set the time',   bg ='snow').place(x = 40 ,y = 150)
Button(root, text='START', bd ='5', command = countdown, bg = 'light grey', font = 'arial 10 bold').place(x=-1, y=210)
Button(root, text='RESET', bd ='5', command = countdown, bg = 'light grey', font = 'arial 10 bold').place(x=310, y=210)
Button(root, text='STOP', bd ='5', command = partial(countdown, 1), bg = 'light grey', font = 'arial 10 bold').place(x=150, y=260)
Button(root, text='PAUSE', bd ='5', command =  partial(countdown, 2), bg = 'light grey', font = 'arial 10 bold').place(x=100, y=210)
Button(root, text='RESUME', bd ='5', command = countdown, bg = 'light grey', font = 'arial 10 bold').place(x=200, y=210)
 
root.mainloop()