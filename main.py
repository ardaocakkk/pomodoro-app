from cgitb import text
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer_text,text="00:00")
    checkmark_label.config(text="")
    global reps 
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    
    work_sec = WORK_MIN *60
    long_break_sec = LONG_BREAK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    
    
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="BREAK",fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="BREAK",fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="STUDY",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    if count >=0:
        global timer
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="pomodoro-start\Tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130,text="00:00",fill="white" ,font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

#Label

timer_label = Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
timer_label.grid(row=1,column=2)

checkmark_label = Label(fg=GREEN,bg=YELLOW,highlightthickness=0)
checkmark_label.grid(row=4,column=2)

#Buttons

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=3,column=1,)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=3,column=3)


window.mainloop()