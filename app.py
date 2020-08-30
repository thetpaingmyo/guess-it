import tkinter as tk
from tkinter import ttk
from random import shuffle

root = tk.Tk()
root.title("Guess it!")

def shuffle_and_show_result():
    my_list = [' ', 'O', ' ']
    shuffle(my_list)
    index = int(number.get())
    if index in [0, 1, 2]:
        if my_list[index] == 'O':
            print('Bingo!')
        else:
            print('Sorry. You guessed wrong.')
            print(my_list)
    else:
        print('Index out of range.')

number = tk.StringVar()

label = ttk.Label(root, text='Guess the position of "O". 0,1 or 2? ')
label.pack(side='left', padx=(0,10))

entry = ttk.Entry(root, width=14, textvariable=number)
entry.pack(side='left')

check_button = tk.Button(root, text='Check', bg='green', command=shuffle_and_show_result)
check_button.pack(side='left', padx=(4,4))

quit_button = tk.Button(root, text='Quit', bg='red', command=root.destroy)
quit_button.pack(side='left', padx=(4,4))

root.mainloop()