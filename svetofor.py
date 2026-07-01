import random
from tkinter import *
import tkinter as tk

def get_user_choice():
    choices = ['красный', 'жёлтый', 'зелёный']
    user = e.get().lower()

    if user == 'выход':
        m1=tk.config(text='Игра окончена')
        exit()

        # return user

    if user not in choices:
        raise ValueError('Такого варианта нет')
        # print('Такого варианта нет')

    return user

def get_computer_choice():
    choices = ['красный', 'жёлтый', 'зелёный']
    computer = random.choice(choices)
    return computer


def check_winner(user, computer):
    if user == computer:
        return ('Вы выиграли!')
    else:
        return ('Компьютер выиграл!')

root = Tk()
root.title('Угадай свет светофора')
root.geometry('500x250+200+50')

m = Label(root, text='Введи свет светофора!', width=50, height=3, fg='DarkBlue')
m.pack(pady=10)

e = Entry(root, width=20, font=('Arial', 15))
e.pack(pady=5)

b = Button(root, text=('ПРОВЕРИТЬ"'), command=check_winner)
b.pack(pady=1)

m1 = Label(root, text='', width=50, height=3, fg='DarkBlue')
m1.pack(pady=15)





# while True:
#     try:
#         # choices = ['камень', 'ножницы', 'бумага']
#         user = get_user_choice()
#         # if user == 'выход':
#         #     print('Игра окончена')
#         #     break
#         #
#         # if user not in choices:
#         #     print('Такого варианта нет')
#
#         print(f'Вы выбрали:{user}')
#
#         computer = get_computer_choice()
#         print(f'Компьютер выбрал:{computer}')
#
#         result = check_winner(user, computer)
#         print(result)
#
#     except Exception as e:
#         print(type(e).__name__)
#         print(e)

root.mainloop()
