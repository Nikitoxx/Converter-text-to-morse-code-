from tkinter import *

root = Tk()
root.geometry('550x150+800+100')
root.configure(bg='Black')
root.resizable(False, False)
root.title('Text to morze')

# Code morze
morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.',
    '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ':'\\',
    
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 
    'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..',
    'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 
    'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 
    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
}



#Functions 

def converte():
    a = ent.get()
    global morse_code
    result = ' '.join([morse_code[x] for x in a.upper()])
    lab['text'] = result
    
def clear():
    ent.delete(0, END)
    lab['text'] = ''


# Interface

ent = Entry(font=('Arial', 20), width=30)
ent.grid(column=0, row=0, padx=10, pady=10)

btn1 = Button(font=('Arial', 15), text= 'Enter', bg='orange', command=converte)
btn1.grid(column=1, row=0)
btn1 = Button(font=('Arial', 15), text= 'Clear', bg='orange', command=clear)
btn1.grid(column=1, row=1)

lab = Label(font=('Arial', 20), width=28, text='', anchor='w')
lab.grid(column=0, row=1, padx=10, pady=10)



root.mainloop()