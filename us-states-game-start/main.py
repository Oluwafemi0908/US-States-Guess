import turtle

import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title('U.S States Game')

screen.bgpic('blank_states_img.gif')

# To get the coordinates of the states by clicking on the background
# def get_mouse_click_cor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_cor)
#
# turtle.mainloop()

df = pd.read_csv('50_states.csv')

state = df['state'].to_list()
x = df['x'].to_list()
y = df['y'].to_list()
score = 0
guessed_states = []
guessed = Turtle()
guessed.hideturtle()
guessed.penup()
game_is_on = True
scoreboard = Turtle()
t = Turtle()
t.hideturtle()
t.penup()

data = {
    'State': state,
    'x': x,
    'y': y
}
while game_is_on:
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.goto(0, 280)
    scoreboard.write(f'Score: {score}/{len(state)}', align='center', font=('Arial', 25, 'bold'))
    answer = screen.textinput('Guess the state', 'A state in the U.S')
    if answer.title() in data['State']:
        if answer.title() in guessed_states:
            guessed.goto(0, 150)
            guessed.write('State guessed earlier', align='center', font=('Arial', 25, 'bold'))
        else:
            guessed_states.append(answer.title())
            guessed.clear()
            index = data["State"].index(answer.title())
            print(index)

            t.goto(data['x'][index], data['y'][index])
            t.write(answer.title(), align='center', font=('Arial', 10, 'normal'))
            score += 1
            scoreboard.clear()

    elif answer.lower() == 'exit':
        remaining_states = [x for x in state if x not in guessed_states]
        r = pd.DataFrame(remaining_states)
        r.to_csv('remaining_states ')
        game_is_on = False
    else:
        guessed.clear()
        guessed.write('Wrong guess, Game Over!!!', align='center', font=('Arial', 25, 'bold'))
        game_is_on = False

    if score == 50:
        t.goto(0, 0)
        t.write("You are a Legend!!!", align='center', font=('Arial', 25, 'bold'))

turtle.exitonclick()
