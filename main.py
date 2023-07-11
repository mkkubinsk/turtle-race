from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to the turtle races!")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
turtlenum = 0
step = 0
winner = ""

for color in colors:
    turtlenum += 1
    jimmys = Turtle(shape="turtle")
    jimmys.color(color)
    turtles.append(jimmys)
    jimmys.penup()
    jimmys.goto(x=-230, y=-90 + turtlenum * 30)

bet = screen.textinput(title="Turtle races", prompt="Which turtle is going to win the race? Type a color: ")

while winner == "":
    for turtle in turtles:
        step = random.randint(1, 10)
        turtle.forward(step)
        where_turtle = turtle.position()
        # print(where_turtle)
        if where_turtle[0] >= 230:
            winner = turtle.color()
            break

if winner[0] == bet:
    print(f"Congratulations! {winner[0].title()} won the race!")
else:
    print(f"Sorry, {winner[0].title()} won the race, {bet.title()} lost!")

screen.exitonclick()
