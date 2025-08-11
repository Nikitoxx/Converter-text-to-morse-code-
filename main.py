from tkinter import *

root = Tk()
root.geometry('600x300+800+100')
root.configure(bg='Black')


# Interface

ent = Entry(font=('Arial', 20), width=30)
ent.grid(column=0, row=0, padx=10, pady=10)

btn1 = Button(font=('Arial', 15), text= 'Enter', bg='orange' )
btn1.grid(column=1, row=0)
btn1 = Button(font=('Arial', 15), text= 'Clear', bg='orange' )
btn1.grid(column=1, row=1)

lab = Label(font=('Arial', 20), width=28, text='')
lab.grid(column=0, row=1, padx=10, pady=10)










root.mainloop()