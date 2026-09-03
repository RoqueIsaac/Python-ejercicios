import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

user_answer = (screen.textinput(title="Guess the State", prompt="What's another state name?")).title()
# se obtiene la fila que coincida con el usuario
b = data[data["state"] == user_answer]

#genera una lista con todos los estados
all_states = data.state.to_list()

# print(user_answer)
# print(b)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)


count = 0
answers = []
missing_states = []
while (len(answers) < 50):
    if user_answer == "Exit":
        for state in all_states:
            if state not in answers:
                missing_states.append(state)
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv("missing_states.csv")
        break
    if len(b) > 0 and user_answer not in answers:
        count += 1
        answers.append(user_answer)
        t.goto(b.x.item(), b.y.item())
        t.write(f'{user_answer}', align='center', font=('Arial', 7, 'normal'))
    user_answer = (screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state name?")).title()
    b = data[data["state"] == user_answer]

#alternativa para escribir en el archivo.
# for state in all_states:
#     if state not in answers:
#         with open("states_to_learn.csv", "a+") as f:
#             f.write(f"{state}\n")


#screen.exitonclick()
