from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Witch turtle will wit the race/ Enter color + {colors}")
print(user_bet)
y = -70
all_turtles = []
for turtle_index in range(0,6):

 new_turtle = Turtle(shape="turtle")
 new_turtle.color(colors[turtle_index])
 new_turtle.penup()
 new_turtle.goto(x=-230, y=y)
 y += 30
 all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

