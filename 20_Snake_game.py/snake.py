import turtle as tr

INIT_POS = [(0,0), (-20,0), (-40,0)]

MOVE_DISTANCE = 20

UP    = 90
DOWN  = 270
LEFT  = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.x = 0
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in INIT_POS:
            self.add_segment(position)


    def add_segment(self, position):
        tu = tr.Turtle(shape="square")
        tu.color("white")
        tu.penup()
        tu.goto(position)
        self.snake.append(tu)


    def extend(self):
        self.add_segment(self.snake[-1].position())


    def move(self):
        # para el movimiento, recorremos el snake de atras hacia adelante, de tal manera
        # que la posicion del ultimo elemento, se recorre a la posicion del elemento siguiente.
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)

        self.snake[0].fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

