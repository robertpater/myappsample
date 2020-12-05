import turtle
import random
import math
from turtle import*
turtle.screensize(5000,5000)
print("podaj predkosc (pomiedzy # 1-10)")
u=int(input())
if u<0:
     u=0
if u>9:
     u=-1
speed(u+1)
w=0
print("liczba powtorzen")
v=int(input())
print("kolor 1 np red")
t=input()
print("kolor 2 np green")
s=input()
color(t)
fillcolor(t)
begin_fill()
forward(75)
while w<v:
     w+=1
     color(t)
     left(90)
     forward(75)
     (x,y)=pos()
     goto(0,0)
     end_fill()
     fillcolor(s)
     begin_fill()
     z=towards(x,y)
     setheading(z)
     goto(x,y)
     if w<v:
          w+=1
          color(s)
          left(90)
          forward(75)
          (x,y)=pos()
          goto(0,0)
          end_fill()
          fillcolor(t)
          begin_fill()
          z=towards(x,y)
          setheading(z)
          goto(x,y)
print("nacisnij klawisz aby wyjsc..")
input()
#OPIS PROGRAMU
# https://zgaskill.wordpress.com/mth-487/spiral-of-theodorus-in-python/
# import turtle                                    This imports the turtle graphics library
# import random                                } These two I always import as I often need them
# import math                                     }
# from turtle import*
# turtle.screensize(5000,5000)      This and the previous line establish the screen size for the program
# print(“speed (as # 1-10)”)             This line causes the program to ask what speed to draw at
# u=int(input())                                 This line allows the user to input the speed
# if u<0:                                               This checks if users input speeds below the minimum
# u=0                                           This sets too low speeds to the minimum
# if u>9:                                      Likewise this checks for speeds the maximum or higher
# u=-1                                          Turtle has 0 as fastest, 1 as slowest and all other speeds in order 1-9
# speed(u+1)                              This implements the speed, the plus 1 sets all 0 to min and -1 to max
# w=0                                          This initializes the value w, which is used later on
# print(“number iterations”)        This asks the user the number of iterations to be run
# v=int(input())                               This line then allows the user to input the number of iterations
# print(“colour 1”)                           This line asks for the first color
# t=input()                                        This line allows for the first color to be input by the user
# print(“colour 2”)                          This line asks for the second color
# s=input()                                       This line allows for the second color to be input by the user
# color(t)                                          This turns the turtles line into the first color
# fillcolor(t)                                     This turns the fill in color to the first color
# begin_fill()                                   This begins defining the area to be filled in
# forward(75)                                  This makes the turtle move forward 75 units
# while w<v:                     This tells python to do the following as long as w< than the # of iterations
# w+=1                               This increases w by one as it is about to run one iteration
# color(t)                           This establishes the line color as color 1 (needed during loops)
# left(90)                           This causes the turtle to take a right turn from the end of his line
# forward(75)                   This causes the turtle to move after the turn
# (x,y)=pos()                    This stores the current position as the coordinate pair (x,y)
# goto(0,0)                        This causes the turtle to return to the origin
# end_fill()                       This fills in the newly created triangle
# fillcolor(s)                     This changes the fill color for the next triangle to color 2
# begin_fill()                    This begins the fill for the next triangle
# z=towards(x,y)             This saves the direction to the point (x,y) as a variable, z
# setheading(z)                This causes the turtle to turn towards point z
# goto(x,y)                        The turtle goes to point z, keeping his current heading
# if w<v:                            If the number of runs has passed the # iterations the loop stops
# w+=1                              The number of runs is increased by 1
# color(s)                          The line color is switched to color 2
# left(90)                          The turtle takes a right turn from its current heading
# forward(75)                  The turtle moves forward after the turn
# (x,y)=pos()                   The turtle stores its position again
# goto(0,0)                      The turtle returns to the origin
# end_fill()                      The turtle fills in the new triangle
# fillcolor(t)                     The fill color changes back to color 1
# begin_fill()                   This begins the fill for the next triangle
# z=towards(x,y)            This saves the direction to the point (x,y) as a variable, z
# setheading(z)               This causes the turtle to turn towards point z
# goto(x,y)                        The turtle goes to point z, keeping his current heading
# input()                           Once the loop stops this prevents the program from closing until an input