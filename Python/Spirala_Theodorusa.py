# ostatnia zmiana 2020.10.10 - wprowadzenie fukcji podpisu
import turtle
import math
import random


wn = turtle.Screen()
wn.bgcolor('black')
wn.colormode(255)

# Ustawienia
t = turtle.Turtle()
t.speed(1)
t.pensize(1)
dlugosc = 1  # wspolczynnik obliczen
liczba_t = 100  # liczba powtorzen
# parametry do fukcji podpisu, Font rozmiar i typ
czcionka = ('Courier', 10, 'normal')

# Definicje rysowania


def w_prawo_trojkat():
    t.begin_fill()
    b = 40  # staly bok trojkata (skala rysowania)
    a = b * math.sqrt(dlugosc)  # przeskalowany zmienny bok
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(180 - math.degrees(math.atan(a / b)))
    t.forward(math.sqrt(a**2 + b**2))
    t.left(180)
    t.end_fill()


def w_lewo_trojkat():
    t.begin_fill()
    b = 40
    a = b * math.sqrt(dlugosc)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(180 - math.degrees(math.atan(a / b)))
    t.forward(math.sqrt(a**2 + b**2))
    t.right(180)
    t.end_fill()

# podpis zawierajacy pierwiastek z wartosci przeciwprostokatnej


def podpisz():
    b = 40
    a = b * math.sqrt(dlugosc)
    t.up()  # podniesienie piora i odsuniecie od trojkata
    #t.forward(a * 2 / 3)
    t.forward(a + 50)
    t.down()
    podpis = str('\u221A') + str(dlugosc + 1)  # znak pierwsiastka w unicode
    t.write(podpis, align="right", font=czcionka)
    t.penup()
    t.goto(0, 0)


def losuj():
 #   z = random.choice(kolory)
    z = random.randint(0, 255)

    return z


# program glowny

for y in range(2):
    for i in range(liczba_t):
        t.pencolor(losuj(), losuj(), losuj())
        t.fillcolor(losuj(), losuj(), losuj())
        w_prawo_trojkat()  # wywolanie fukcji rysowania w prawo
        podpisz()  # wywolanie fukcji podpisu
        dlugosc += 1  # zwiekszenie wspolczynnika - iteracja umownego parametru dlugosci
    t.clear()   # czyszczenie ekranu

    for i in range(liczba_t):
        t.pencolor(losuj(), losuj(), losuj())
        t.fillcolor(losuj(), losuj(), losuj())
        w_lewo_trojkat()
        podpisz()
        dlugosc -= 1
    t.clear()

turtle.exitonclick()
