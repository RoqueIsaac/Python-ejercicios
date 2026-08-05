from turtle import Turtle, Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#tracer(0) apaga las animaciones, para mostrarlas se hace uso del metod update()
screen.tracer(0)
#listen permite eventos del teclado
screen.listen()

snakes = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snakes.up,"Up")
screen.onkey(snakes.down,"Down")
screen.onkey(snakes.left,"Left")
screen.onkey(snakes.right,"Right")


game_is_on = True
while game_is_on:
    # dibuja una vez movidos todos los segmentos
    screen.update()
    time.sleep(0.1)
    snakes.move()

    #detectar colision con food
    if snakes.head.distance(food) < 15:
        food.refresh()
        snakes.extend()
        scoreboard.increase_score()

    #colisiones con paredes
    if snakes.head.xcor() > 280 or snakes.head.xcor() < -280 or snakes.head.ycor() > 280 or snakes.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #colisiones con cola, no se toma la pos 0, ya que es la cabeza
    for segment in snakes.snake[1:]:
        if snakes.head.distance(segment) < 10:
            game_is_on = False
            scoreboard. game_over()


screen.exitonclick()

