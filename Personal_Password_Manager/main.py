from tkinter import *
from tkinter import messagebox
import string
import random
import json

# ------------------ Constants------------------------#
PURPLE = '#8B1874'
LIGHT_PURPLE = '#B71375'
ORANGE = '#FC4F00'
WARM = '#F79540'
FONT = 'calibri'


def generate(user_input):
    password = []
    low_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    special = string.punctuation
    digits = string.digits
    lis = [low_case, digits, upper_case]
    count = 0
    while count < (user_input - 4):
        choice = random.choice(lis)
        out = random.choice(choice)
        password.append(out)
        count += 1
    for i in range(3):
        password.append(random.choice(special))
    password.append(' ')
    random.shuffle(password)
    if password[0] == ' ':
        random.shuffle(password)
    else:
        pass
    password = ''.join([i for i in password])
    entry_3.insert(0, password)


def generate_command():
    if entry_1.get() == '':
        messagebox.showwarning('Warning', 'Enter Name of the Website')
    elif entry_2.get() == '':
        messagebox.showwarning('Warning', 'Enter Your Username')
    elif entry_4.get() == '':
        messagebox.showwarning('Warning', 'Enter Number of Characters in Password')
    else:
        generate(int(entry_4.get()))
        win.clipboard_clear()
        win.clipboard_append(entry_3.get())


def add_to_file():
    website = entry_1.get()
    username = entry_2.get()
    password = entry_3.get()
    data = {
        website:
            {'username': username,
             'password': password}
    }
    if entry_1.get() == '' and entry_2.get() == '' and entry_4.get() == '':
        messagebox.showwarning('Warning', 'Generate Password First')
    else:
        try:
            with open('password_data.json', 'r') as data_file:
                new_data = json.load(data_file)

        except FileNotFoundError:
            with open('password_data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        else:
            new_data.update(data)
            with open('password_data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            entry_1.delete(0, 'end')
            entry_2.delete(0, "end")
            entry_3.delete(0, "end")
            entry_4.delete(0, "end")


def search():
    item = entry_1.get()
    try:
        with open('password_data.json', 'r') as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showinfo('Message', 'No Data File Found')

    else:
        if item in data:
            username = data[item]['username']
            password = data[item]['password']
            messagebox.showinfo('Search Result', f'username/email: {username}\n password: {password}')
        else:
            messagebox.showwarning('Warning', f'No data found of the item "{item.capitalize()}"')
    finally:
        entry_1.delete(0, 'end')


win = Tk()
win.title("Personal Password Manager")
win.config(padx=5, pady=5, background=PURPLE, highlightthickness=0)
canvas = Canvas(width=300, height=300, background=PURPLE, highlightthickness=0)
photo = PhotoImage(file='download.png')
canvas.create_image(150, 150, image=photo)
canvas.grid(row=0, column=0, columnspan=3)
label_1 = Label(text='Website:', background=PURPLE, foreground='white', font=(FONT, 15, 'bold'))
label_1.grid(row=1, column=0)
label_2 = Label(text='Email/Username:', background=PURPLE, foreground='white', font=(FONT, 15, 'bold'))
label_2.grid(row=2, column=0)
label_3 = Label(text='Password:', background=PURPLE, foreground='white', font=(FONT, 15, 'bold'))
label_3.grid(row=3, column=0)
label_4 = Label(text='Characters count:', background=PURPLE, foreground='white', font=(FONT, 15, 'bold'))
label_4.grid(row=4, column=0)

entry_1 = Entry(width=30, background=LIGHT_PURPLE, foreground='white', font=(FONT, 15, 'bold'))
entry_1.grid(row=1, column=1)
entry_2 = Entry(width=30, background=LIGHT_PURPLE, foreground='white', font=(FONT, 15, 'bold'))
entry_2.grid(row=2, column=1)
entry_3 = Entry(width=30, background=LIGHT_PURPLE, foreground='white', font=(FONT, 15, 'bold'))
entry_3.grid(row=3, column=1)
entry_4 = Entry(width=3, background=LIGHT_PURPLE, foreground='white', font=(FONT, 15, 'bold'))
entry_4.grid(row=4, column=0, columnspan=2)

generate_button = Button(text='Generate', background=WARM, foreground='white', width=15, height=1,
                         command=generate_command)
generate_button.grid(row=4, column=1)
add_button = Button(text='Add to file', background=WARM, foreground='white', width=30, height=1, command=add_to_file)
add_button.grid(row=5, column=1)
search_button = Button(text='Search', background=WARM, foreground='white', width=30, height=1, command=search)
search_button.grid(row=5, column=0)

win.mainloop()
