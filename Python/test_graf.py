import turtle
import math
import random

# Ustawienia
t = turtle.Turtle()
t.speed(100)
t.pensize(0)
dlugosc = 1
liczba_t = 50
kolory = ["red", "green", "blue", "orange", "purple",
          "pink", "yellow"]  # Make a list of colors to picvk from
wn = turtle.Screen()
wn.bgcolor('black')

# Definicje rysowania


def w_prawo_trojkat():
    t.begin_fill()
    b = 30
    a = b * math.sqrt(dlugosc)
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(180 - math.degrees(math.atan(a / b)))
    t.forward(math.sqrt(a**2 + b**2))
    t.left(180)
    t.end_fill()


def w_lewo_trojkat():
    t.begin_fill()
    b = 30
    a = b * math.sqrt(dlugosc)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(180 - math.degrees(math.atan(a / b)))
    t.forward(math.sqrt(a**2 + b**2))
    t.right(180)
    t.end_fill()


def losuj():
 #   z = random.choice(kolory)
    z = random.randint(1,254)

    return z



# wywolanie rysowania
for y in range(10):
    for i in range(liczba_t):
        t.color(losuj(),losuj(),losuj())
        w_prawo_trojkat()
        dlugosc += 1

  # for i in range(liczba_t):
  #       t.color(losuj())
  #       w_lewo_trojkat()
  #       dlugosc -= 1
