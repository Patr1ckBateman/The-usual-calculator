import tkinter
from tkinter import messagebox


def add_0():
    entry_label['text'] += '0'


def add_1():
    entry_label['text'] += '1'


def add_2():
    entry_label['text'] += '2'


def add_3():
    entry_label['text'] += '3'


def add_4():
    entry_label['text'] += '4'


def add_5():
    entry_label['text'] += '5'


def add_6():
    entry_label['text'] += '6'


def add_7():
    entry_label['text'] += '7'


def add_8():
    entry_label['text'] += '8'


def add_9():
    entry_label['text'] += '9'


def plus():
    if entry_label['text'][-1] in '+-*/':
        backspace()

    entry_label['text'] += '+'


def minus():
    if entry_label['text'][-1] in '+-*/':
        backspace()

    entry_label['text'] += '-'


def multiply():
    if entry_label['text'][-1] in '+-*/':
        backspace()

    entry_label['text'] += '*'


def divide():
    if entry_label['text'][-1] in '+-*/':
        backspace()

    entry_label['text'] += '/'


def equals():
    try:
        entry_label['text'] = str(eval(entry_label['text']))
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Нельзя делить на ноль!')
    except SyntaxError:
        messagebox.showerror('Ошибка', 'Некорректный ввод')


def backspace():
    entry_label['text'] = entry_label['text'][:-1]


def clear():
    entry_label['text'] = ''


def key_pressed(event):
    if event.char == '0':
        add_0()
    elif event.char == '1':
        add_1()
    elif event.char == '2':
        add_2()
    elif event.char == '3':
        add_3()
    elif event.char == '4':
        add_4()
    elif event.char == '5':
        add_5()
    elif event.char == '6':
        add_6()
    elif event.char == '7':
        add_7()
    elif event.char == '8':
        add_8()
    elif event.char == '9':
        add_9()
    elif event.char == '+':
        plus()
    elif event.char == '-':
        minus()
    elif event.char == '*':
        multiply()
    elif event.char == '/':
        divide()
    elif event.keysym == 'Return':
        equals()
    elif event.keysym == 'BackSpace':
        backspace()
    elif event.keysym == 'Delete':
        clear()


"""Окно"""
window = tkinter.Tk()
window.geometry('275x400')
window.resizable(False, False)

window.bind('<Key>', key_pressed)

"""Поле ввода"""
entry_label = tkinter.Label(text='',
                            font=('Arial', 18),
                            bg='white',
                            anchor='e',
                            width=18
                            )
entry_label.place(relx=0.5, y=10, anchor='n')

"""Кнопки"""
button_0 = tkinter.Button(text='0', font=('Arial', 20), width=3, command=add_0)
button_1 = tkinter.Button(text='1', font=('Arial', 20), width=3, command=add_1)
button_2 = tkinter.Button(text='2', font=('Arial', 20), width=3, command=add_2)
button_3 = tkinter.Button(text='3', font=('Arial', 20), width=3, command=add_3)
button_4 = tkinter.Button(text='4', font=('Arial', 20), width=3, command=add_4)
button_5 = tkinter.Button(text='5', font=('Arial', 20), width=3, command=add_5)
button_6 = tkinter.Button(text='6', font=('Arial', 20), width=3, command=add_6)
button_7 = tkinter.Button(text='7', font=('Arial', 20), width=3, command=add_7)
button_8 = tkinter.Button(text='8', font=('Arial', 20), width=3, command=add_8)
button_9 = tkinter.Button(text='9', font=('Arial', 20), width=3, command=add_9)

button_plus = tkinter.Button(text='+', font=('Arial', 20), width=3, command=plus)
button_minus = tkinter.Button(text='-', font=('Arial', 20), width=3, command=minus)
button_multiply = tkinter.Button(text='*', font=('Arial', 20), width=3, command=multiply)
button_divide = tkinter.Button(text='/', font=('Arial', 20), width=3, command=divide)
button_equals = tkinter.Button(text='=', font=('Arial', 20), width=3, command=equals)

button_backspace = tkinter.Button(text='←', font=('Arial', 20), width=7, command=backspace)
button_clear = tkinter.Button(text='C', font=('Arial', 20), width=3, command=clear)

button_0.place(x=75, y=310)
button_1.place(x=10, y=250)
button_2.place(x=75, y=250)
button_3.place(x=140, y=250)
button_4.place(x=10, y=190)
button_5.place(x=75, y=190)
button_6.place(x=140, y=190)
button_7.place(x=10, y=130)
button_8.place(x=75, y=130)
button_9.place(x=140, y=130)

button_plus.place(x=205, y=130)
button_minus.place(x=205, y=190)
button_multiply.place(x=205, y=250)
button_divide.place(x=205, y=310)
button_equals.place(x=205, y=70)

button_backspace.place(x=75, y=70)
button_clear.place(x=10, y=70)

window.mainloop()
