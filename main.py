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
    
def create_button( text, command, column, row, font,bg):
    Button(font=font, 
           text= text, 
           bg=bg, 
           command=command).grid(column=column,
                                 row=row)
    


# Interface

ent = Entry(font=('Arial', 20), width=30)
ent.grid(column=0, row=0, padx=10, pady=10)

buttons = [['Enter', converte, 1, 0, ('Arial', 15), 'orange'],
           ['Clear', clear, 1, 1, ('Arial', 15), 'orange'],
           ['Atbash', None, 0, 2, ('Arial', 10), 'gray']]

for i in buttons:
    x, c, v, b, n, m = i
    create_button(x, c, v, b, n, m)





lab = Label(font=('Arial', 20), width=28, text='', anchor='w')
lab.grid(column=0, row=1, padx=10, pady=10)





root.mainloop()