from tkinter import *
from cipher import morse

root = Tk()
root.geometry('550x150+800+100')
root.configure(bg='Black')
root.resizable(False, False)
root.title('Text to morze')


#Functions 

def converte():
    a = ent.get()
    result = ' '.join(morse[x] for x in a.upper())
    lab['text'] = result
    
def clear():
    ent.delete(0, END)
    lab['text'] = ''
    
def create_button( text, command, column, row):
    Button(font=('Arial', 15), 
           text= text, 
           bg='orange', 
           command=command).grid(column=column,
                                 row=row)
    


# Interface

ent = Entry(font=('Arial', 20), width=30)
ent.grid(column=0, row=0, padx=10, pady=10)


create_button('Enter', converte, 1, 0)
create_button('Clear', clear, column=1, row=1)


lab = Label(font=('Arial', 20), width=28, text='', anchor='w')
lab.grid(column=0, row=1, padx=10, pady=10)



root.mainloop()