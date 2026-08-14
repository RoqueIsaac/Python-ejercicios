from turtle import Turtle

ALIGNMENT = "center"
FONT      = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_high_score()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.highscore = self.read_high_score()
        self.goto(0, 260)
        self.write(f"Score: {self.score}            High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.exit_game()
disp
    def increase_score(self):

        self.score += 1
        self.update_scoreboard()

    def resets(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as f:
                f.write(f"{self.score}")

            #self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open(f"data.txt", "r") as f:
            highscore = int(f.read())

        return highscore

    def exit_game(self):
        self.goto(225,-275)
        self.write("q -> Stop", align=ALIGNMENT, font=("Courier", 13, "bold"))


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
