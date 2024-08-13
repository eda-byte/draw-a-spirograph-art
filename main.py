from turtle import Turtle, Screen
import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
def random_color():
    r =random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup=(r,g,b)
    return tup

tim.hideturtle()
tim.speed("fastest")
degrees=[90,180,270,0]
tim.pensize(1)


for _ in range(1,360):

    while True:
        tim.circle(100, None, 36)  # t.colormode(255)

        tim.pencolor(random_color())
        lefty=tim.left(2)
astamp = tim.stamp()
tim.settiltangle(1)



screen=Screen()
screen.exitonclick()