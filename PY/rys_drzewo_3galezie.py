# rysuj drzewo trzy galezie - fraktale
import turtle
import random
hr = turtle.Turtle()
hr.left(90)
hr.speed(10)
hr.penup()
hr.goto(0,-200)
hr.pendown()

def losuj():
    x=round(random.uniform(0.6, 0.9),1)
    return x


def tree(i):
    if i < 15:
        return
    else:
        hr.forward(i)
        hr.right(20)

        tree(i*losuj())
        hr.left(20)

        tree(i*losuj())
        hr.left(20)

        tree(i*losuj())
        hr.right(20)
        hr.backward(i)



# hr.forward(i)
# hr.right(30)
# hr.forward(i*0.67)
# hr.left(30)
# hr.forward(i*0.67)
# hr.left(30)
# hr.forward(i*0.67)

tree(60)

turtle.done()


        # hr.forward(i)
        # hr.left(30)
        # tree(3 * i / 4)
        # hr.right(60)
        # tree(3 * i / 4)
        # hr.left(30)
        # hr.backward(i)
