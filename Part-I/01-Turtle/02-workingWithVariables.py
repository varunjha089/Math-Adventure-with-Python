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
getcanvas().postscript(file="variable_square.eps")
sleep(5)
