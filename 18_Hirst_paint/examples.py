import turtle
import turtle as tr
import heroes
import random

tm = tr.Turtle()
tm.shape("turtle")
screen = tr.Screen()

# for _ in range(4):
#     tm.fd(100)
#     tm.right(90)

# tm.pensize(5)
# for _ in range(15):
#     tm.fd(10)
#     tm.up()
#     tm.fd(10)
#     tm.down()

tr.colormode(255)
tm.pensize(2)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    var = (r,g,b)
    return var


#-- poligonos --
def draw_shape(edges):
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tm.pencolor(r,g,b)
    angle = 360 / edges
    for k in range(edges):
        tm.fd(100)
        tm.right(angle)

for i in range(3,11):
    draw_shape(i)


#-- random walk --
direction = [0, 90, 180, 270]
tm.pensize(10)
tm.hideturtle()
tm.speed(0)
for j in range(200):
    tm.pencolor(random_color())
    tm.setheading(random.choice(direction))
    tm.fd(30)


#-- spirograph --
tm.pensize(2)
grados = 5
circulos = 360//grados
tm.speed(0)
for j in range(circulos):
    tm.pencolor(random_color())
    tm.left(grados)
    tm.circle(100)

screen.exitonclick()
