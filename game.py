from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ','Love you too')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('Survey')
root.resizable(width=False, height=False)
root['bg']='light pink'

label=Label(root, text='Do you love me ?', font='arial 20 bold', bg='pink').pack()
btnYes = Button(root, text='No', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text= 'Yes', font='Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()