import turtle as tr
import colorgram
import random

#extraccion de colores de una imagen
# colors = colorgram.extract('hist.jpg', 50)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     cols = (r,g,b)
#     rgb_colors.append(cols)
#
# print(rgb_colors)

screen = tr.Screen()

tr.colormode(255)
color_list = [(243, 249, 253), (217, 148, 102), (38, 100, 170), (165, 55, 91), (106, 170, 210), (133, 82, 54), (239, 221, 100), (220, 124, 157), (226, 82, 56), (212, 74, 110), (174, 18, 43), (41, 128, 87), (21, 172, 208), (118, 186, 145), (72, 39, 29), (16, 57, 134), (161, 147, 38), (54, 181, 148), (118, 40, 30), (97, 105, 186), (145, 221, 179), (237, 161, 178), (19, 42, 90), (239, 170, 157), (71, 30, 48), (65, 77, 36), (208, 233, 3), (132, 212, 232), (34, 86, 60), (169, 184, 225), (37, 64, 51), (247, 9, 32)]
tr.pu()
tr.setpos(-250, -250)
tr.speed(0)
tr.pensize(20)
y = 0
for j in range(10):
    for k in range(10):
        tr.pencolor(random.choice(color_list))
        tr.dot(20)
        tr.penup()
        tr.fd(50)
        tr.pendown()
    y += 50
    tr.pu()
    tr.setpos(-250, -250 + y)
    tr.pd()

tr.hideturtle()
screen.exitonclick()