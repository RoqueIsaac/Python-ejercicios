import turtle as tr
from tkinter import messagebox
import random

#--------------------------
def finish_line():
    """
    Pinta la linea de meta
    """
    line = tr.Turtle(visible=False)
    line.pu()
    line.goto(220, 180)
    line.right(90)
    line.pd()
    line.goto(220, -175)
    line.pu()
    line.goto(200, -195)
    line.write("Finish", font=('Arial', 11, 'bold'))
#--------------------------

screen = tr.Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list =[]
y=160
for j in range(6):
    new_turtle = tr.Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.goto(-230, y-30)
    new_turtle.write(f"{j+1}", font=('Arial',12, 'bold'))
    new_turtle.color(colors[j])
    new_turtle.goto(-230,y)
    y -=60
    turtle_list.append(new_turtle)


finish_line()

user_bet = screen.textinput(title="Make your bet", prompt="Which color will win ? Enter number: ")

while user_bet not in ["1","2","3","4","5","6"]:
    user_bet = screen.textinput(title="Make your bet", prompt="Give me a valid number: ")

is_race_on = True
indx = 0
while is_race_on:
    for trt in turtle_list:
        trt.fd(random.randint(3,12))
        if trt.xcor() >= 210:
            is_race_on = False
            indx = turtle_list.index(trt)


if int(user_bet) == (indx+1):
    messagebox.showinfo("Race", f"    You Win !!\n turtle {turtle_list[indx].pencolor()} won")
else:
    messagebox.showinfo("Race", f"  Maybe next time\nturtle {indx+1}-{turtle_list[indx].pencolor()} won", icon="error")

screen.exitonclick()

