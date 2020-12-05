import turtle
gaba = turtle.Turtle()
gaba.left(180)
gaba.speed(5)
gaba.penup()
gaba.goto(300,300)
gaba.pendown()

def kryska(i):
    if i<10:
        return
    else:
        gaba.forward(i)
        gaba.left(90)
        kryska(i*.9)
kryska(600)
turtle.done()
