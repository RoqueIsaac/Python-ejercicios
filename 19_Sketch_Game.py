import turtle as tr

screen = tr.Screen()
screen.title("Sketch game")

trt = tr.Turtle()
trt.pensize(2)

text = tr.Turtle()
text.ht()
text.pu()
text.setpos(-400,350)
text.write("W -> Forwards",font=('Arial', 10, 'normal'))
text.setpos(-400,330)
text.write("S -> Backwards", font=('Arial', 10, 'normal'))
text.setpos(-400,310)
text.write("A -> Counter-Clockwise", font=('Arial', 10, 'normal'))
text.setpos(-400,290)
text.write("D -> Clockwise", font=('Arial', 10, 'normal'))
text.setpos(-400,270)
text.write("C -> Clear / Reset", font=('Arial', 10, 'normal'))
text.setpos(-400,250)
text.write("mouse click -> exit", font=('Arial', 10, 'normal'))
text.setpos(-400,230)


def move_fd():
    trt.fd(25)

def move_back():
    trt.back(25)

def right():
    trt.right(10)

def left():
    trt.left(10)

def clear():
    trt.reset()
    trt.pensize(2)


screen.onkeypress(key="w", fun=move_fd)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="c", fun=clear)

screen.listen()
screen.exitonclick()

