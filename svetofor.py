import random
from mimetypes import inited
from tkinter import *
import tkinter as tk

# user=''
# computer=''


# def get_user_choice():
#     choices = ['красный', 'жёлтый', 'зелёный']
#     user = e.get().lower()
#
#     if user == 'выход':
#         m1.config(text='Игра окончена')
#         exit()
#
#     if user not in choices:
#         m1.config(text='Такого варианта нет')
#
#     check_winner()
#     return user


# def get_computer_choice():
#     choices = ['красный', 'жёлтый', 'зелёный']
#     computer = random.choice(choices)
#     print(computer)
#     check_winner()
    # return computer


def check_winner():
    choices = ['красный', 'жёлтый', 'зелёный']
    user = e.get().lower()
    print(user)
    computer = random.choice(choices)
    print(computer)
    if user == 'выход':
        exit()
    if user not in choices:
        print(user)
        m1.config(text='нет такого варианта!')
        return
    if user == computer:
        m1.config(text='Вы угадали!')
    else:
        m1.config(text='Вы не угадали!')


root = Tk()
root.title('Угадай свет светофора')
root.geometry('500x250+200+50')

m = Label(root, text='Введи свет светофора или выход !', width=50, height=3, fg='DarkBlue')
m.pack(pady=10)

e = Entry(root, width=20, font=('Arial', 15))
e.pack(pady=5)

b = Button(root, text=('ПРОВЕРИТЬ'), command=check_winner)
b.pack(pady=1)

m1 = Label(root, text='', width=50, height=3, fg='DarkBlue')
m1.pack(pady=15)


root.mainloop()