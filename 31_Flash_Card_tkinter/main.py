import pandas as pd
import random
import tkinter as tk


BACKGROUND_COLOR = "#B1DDC6"

#---- read file ----

try:
    file = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    file = pd.read_csv("./data/french_words.csv")

d = file.to_dict(orient="records")

current_card = {}
indexx = 0

def next_card():
    global current_card, f_timer, indexx, d
    window.after_cancel(f_timer)
    indexx = random.randint(0, len(d)-1)
    current_card = d[indexx]
    frame.itemconfig(image, image=card_front)
    frame.itemconfig(lang_txt, text='French', fill = 'black')
    frame.itemconfigure(trans_txt, text=current_card['French'], fill = 'black')
    f_timer = window.after(2000, solution)

def solution():
    frame.itemconfig(image, image=card_back)
    frame.itemconfig(lang_txt, text='English', fill ='white')
    frame.itemconfigure(trans_txt, text=current_card['English'], fill ='white')

def ok_button_click():
    global indexx, d
    #remove the already known work and store rest on words_to_learn file
    del d[indexx]
    data = pd.DataFrame(d)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

#---------- UI ----------
window = tk.Tk()
window.title("Flash Cards")
window.minsize(900, 780)
window.configure(background=BACKGROUND_COLOR)

card_front = tk.PhotoImage(file="./images/card_front.png")
card_back  = tk.PhotoImage(file="./images/card_back.png")

#canvas
frame = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = frame.create_image(400, 263, image=card_front, anchor="center")
lang_txt  = frame.create_text(400,150, text="", font=("Arial", 40, "italic"))
trans_txt = frame.create_text(400,290, text="", font=("Arial", 60, "bold"))
frame.grid(row=0, column=0, columnspan=2, padx=50, pady=50)
#---------------

ok_image    = tk.PhotoImage(file="./images/right.png")
wrong_image = tk.PhotoImage(file="./images/wrong.png")

#botones
ok_button    = tk.Button(image=ok_image, highlightthickness=0, borderwidth=0,activebackground=BACKGROUND_COLOR, cursor="hand2", command=ok_button_click)
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, cursor="x_cursor", command=next_card)
ok_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)
#--------------

f_timer = window.after(2000, solution)
next_card()

window.mainloop()

