import turtle
import math


t = turtle.Turtle()
a = 140
b = 140
czcionka = ('Courier', 10, 'normal')
wart = 2


pozycja_start = [0, 0]


t.color('green')

t.write(a, align="right", font=czcionka)
t.forward(a)

t.left(90)

t.forward(b)
t.write(90, align="left", font=czcionka)

t.write(('P', wart), align="center", font=czcionka)
t.goto(pozycja_start)


turtle.done()
