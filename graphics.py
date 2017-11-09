"""
1. Write the lines of code that would import
and create a turtle named 'Pong'.
"""
import turtle
Pong = turtle.Turtle('turtle')
Pong.pd()

"""
2.  Draw a square with Pong of length 100
"""
import turtle
Pong = turtle.Turtle('turtle')
for i in range(4):
    Pong.fd(100)
    Pong.rt(90)


"""
3.  Write a function that will allow the user
to input the length of a square and then draw
a square of that length.
"""
import turtle
Pong = turtle.Turtle('turtle')
def square(s):
    for i in range(4):
        Pong.fd(s)
        Pong.rt(90)
square() #enter side length in parentheses after square

"""
4.  Draw a series of squares with different sizes
that share the same corner.
"""


"""
5.  Repeat the question above but change the color
each time it draws a square.
"""
