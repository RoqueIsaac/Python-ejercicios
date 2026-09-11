import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#modificar sig variables para los tiempos de work, breark y long break
WORK_MIN = 25  #25
SHORT_BREAK_MIN = 5  #5
LONG_BREAK_MIN = 20  #20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, active, timer
    reps = 0
    active = 0
    window.after_cancel(timer)
    l_timer.configure(text="Timer", foreground=GREEN)
    l_check.configure(text="")

    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
#esta bandera ayuda a prevenir activar varias veces el timer, se activa cuando termina el que esta en ejecucion
active = 0
def start_timer():
    global active, reps
    if active: return
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps == 9:
        winsound.PlaySound("C:/Windows/Media/tada.wav", winsound.SND_FILENAME)
        reset_timer()
        messagebox.showinfo("Pomodoro", "Fin de ciclo Pomodoro")
    elif reps % 2 == 1:
        count_down(work_sec)
        l_timer.configure(text="Work", background=YELLOW, foreground=GREEN)
        winsound.Beep(3500, 1000)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        l_timer.configure(text="Long Break", background=YELLOW, foreground=RED)
        winsound.PlaySound("C:/Windows/Media/Alarm10.wav", winsound.SND_FILENAME)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        l_timer.configure(text="Break", background=YELLOW, foreground=PINK)
        winsound.PlaySound("C:/Windows/Media/notify.wav", winsound.SND_FILENAME)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global active, timer

    min = count // 60
    sec = count % 60

    if min < 10:
        min = "0" + str(min)

    if sec < 10:
        sec = "0" + str(sec)

    active = 1
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        #print("hey")
        #after permite ejecutar una funcion caca cierto tiempo, sin bloquear la gui
        timer = window.after(1000, count_down, count-1)
    else:
        #si el conteo llego a 0, termina ejecucion, bandera active regresa a 0

        active = 0
        start_timer()
        mark = ""
        for _ in range(reps//2):   #reps//2 son las work session, 1 work y 1 break, y se repite
            mark += "✓"
            l_check.configure(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.minsize(550, 480)
window.config(padx=100, pady=50, bg=YELLOW)

#----------------
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
#----------------

l_timer = ttk.Label(window, text="Timer", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=GREEN)
l_timer.grid(column=1, row=0)

#----------------
#style es valido solo para botones ttk, no exist el argumento font como en tk
style = ttk.Style()
style.configure("TButton", font=("Arial", 10, "bold"))

pad_button = 30
b_start = ttk.Button(text = 'Start', command=start_timer, padding=8, style="TButton")
b_start.grid(column=0, row=2, pady=pad_button)

b_reset = ttk.Button(text = 'Reset', command=reset_timer , padding=8, style="TButton")
b_reset.grid(column=2, row=2, pady=pad_button)
#----------------

l_check = ttk.Label(window, font=(FONT_NAME, 20, "bold"), background=YELLOW, foreground=GREEN)
l_check.grid(column=1, row=3)

#----------------

window.mainloop()
