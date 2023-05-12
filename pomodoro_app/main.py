from tkinter import *
from tkinter import messagebox
import math
import sys
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TIME = "00:00"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


win = Tk()
win.title('Pomodoro App')
win.config(padx=100, pady=50, background=YELLOW)

label = Label(text='Timer', foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40, 'bold'))
label.grid(row=0, column=1)

check_mark = Label(foreground=GREEN, background=YELLOW)
check_mark.grid(row=3, column=1)


def exit_code():
    sys.exit()


def start_press():
    long = LONG_BREAK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    work = WORK_MIN * 60
    global reps
    reps += 1
    if reps == 16:
        messagebox.showwarning('Warning', 'Do something else')
    if reps % 8 == 0:
        label.config(text='Break', foreground=RED, background=YELLOW)
        messagebox.showinfo('Message', 'A long Break is a head')
        count_down(long)
    elif reps % 2 == 0:
        label.config(text='Break', foreground=PINK, background=YELLOW)
        messagebox.showinfo('Message', 'Ready For Break')

        count_down(short)
    else:
        label.config(text='Work', foreground=GREEN, background=YELLOW)
        if reps == 3 or reps == 5 or reps == 7:
            messagebox.showinfo('Message', 'Concentrate on Work')
        count_down(work)



def reset_button():
    global reps
    win.after_cancel(timer)
    label.config(text='Timer', foreground=GREEN, background=YELLOW)
    canvas.itemconfig(timer_text, text=TIME)
    mark = ''
    check_mark.config(text=mark)
    # reps = 0


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = win.after(1000, count_down, count - 1)
    else:
        start_press()

        work_session = math.floor(reps/2)
        mark = ''
        for i in range(work_session):
            mark += '✔'
        check_mark.config(text=mark)


canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 120, text=TIME, fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text='Start', height=1, width=5, background='white', foreground='black', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=start_press)
start.grid(row=2, column=0)
reset = Button(text='Reset', height=1, width=5, background='white', foreground='black', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=reset_button)
reset.grid(row=2, column=3)
exit_button = Button(text='Exit', height=1, width=5, background='white', foreground='black', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=exit_code)
exit_button.grid(row=5, column=1)


win.mainloop()
