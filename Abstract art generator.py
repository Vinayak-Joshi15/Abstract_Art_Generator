import turtle
import random


a = turtle.Turtle()
a.speed(0)

sc = turtle.Screen()
sc.bgcolor("black")
sc.colormode(255)

move = ["left","right"]
#z = random.randint(1,100) will only be useful when you want to remove the limit from the art


for i in range(100):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    a.color(r,g,b)
    x = random.randint(1, 100)
    a.forward(x)
    
    y = random.choice(move)
    
    if y == "left":
        a.left(random.randint(1,360))
    else:
        a.right(random.randint(1,360))



a.hideturtle()

turtle.mainloop()
