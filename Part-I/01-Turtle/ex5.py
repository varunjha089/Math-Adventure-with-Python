"""
Page:- 16
Make a function to draw 60 squares, turning 5 degrees after each square and making each successive square bigger.
Start at a length of 5 and increment 5 units every square.
"""
from turtle import *
from time import sleep


def squares(length):
    for i in range(4):
        forward(length)
        right(90)


# TIMES:- Times to rotate
def sixtySquares(TIMES=60):
    length = 5
    for i in range(TIMES):
        squares(length)
        length = length + 5
        right(5)


sixtySquares()

# this will save the art in .eps format which can be viewed using Inkscape.
getcanvas().postscript(file="variable_square_exercise.eps")
sleep(5)
