from tkinter import *
import math
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
timer = ''

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  window.after_cancel(timer)
  global reps 
  reps = 0
  canvas.itemconfig(timer_text, text="00:00")
  timerLabel.config(text='Timer', fg=GREEN)
  checkLabel.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1
  
  if reps % 2 == reps:
    time = WORK_MIN
    timerLabel.config(text='Work', fg=GREEN)
    countdown(time * 60)
  elif reps % 8 == 0:
    time = LONG_BREAK_MIN
    timerLabel.config(text='Long Break', fg=RED)
    countdown(time * 60)
  else:
    time = SHORT_BREAK_MIN
    timerLabel.config(text='Break', fg=PINK)
    countdown(time * 60)
  
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
  global timer
  
  count_min = math.floor(count/60)
  count_sec = count%60
  if count_sec < 10:
    count_sec = f'0{count_sec}'
  
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count>0:
    timer = window.after(1000, countdown, count-1)
  else:
    start_timer()
    marks = ''
    work_sess = math.floor(reps/2)
    for _ in range(work_sess):
      marks += '✔'
    checkLabel.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)


timerLabel = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timerLabel.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='Week-4/Pomodoro/tomato.png')
canvas.create_image(100, 112, image=img)

timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)


startBtn = Button(text='Start', command=start_timer)
startBtn.grid(column=0, row=3)

resetBtn = Button(text='Reset', command=reset_timer)
resetBtn.grid(column=3, row=3)

checkLabel = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME ,14))
checkLabel.grid(column=1, row=4)

window.mainloop()