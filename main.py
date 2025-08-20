from tkinter import *
from cipher import morse, atbash

root = Tk()
root.geometry('550x150+800+100')
root.configure(bg='Black')
root.resizable(False, False)
root.title('Text encryptor')


#Functions 
atbsh = False


def converte():
    a = ent.get()
    if atbsh:
        result = ''.join(atbash[x] if x.isalpha() else x for x in a)
    else:
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


def swith_to():
    global atbsh
    if atbsh:
        btn['text'] = 'Encryption Type: Morse'
        atbsh = False
    else:
        btn['text'] = 'Encryption Type: Atbash'
        atbsh = True
    


# Interface

ent = Entry(font=('Arial', 20), width=30)
ent.grid(column=0, row=0, padx=10, pady=10)

buttons = [['Enter', converte, 1, 0, ('Arial', 15), 'orange'],
           ['Clear', clear, 1, 1, ('Arial', 15), 'orange'],]

for i in buttons:
    x, c, v, b, n, m = i
    create_button(x, c, v, b, n, m)
    
btn = Button(font=('Arial', 10), 
           text='Encryption Type: Morse', 
           bg='grey', 
           command=swith_to)
btn.grid(column=0, row=2)





lab = Label(font=('Arial', 20), width=28, text='', anchor='w')
lab.grid(column=0, row=1, padx=10, pady=10)





root.mainloop()