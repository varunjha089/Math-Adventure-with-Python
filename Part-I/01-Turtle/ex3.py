"""
On page-13:-

"""

from turtle import *
from time import sleep


def triangle():
    for i in range(3):
        forward(100)
        left(120)


def times(TIMES):
    for i in range(TIMES):
        triangle()
        right(5)

times(1)
# this will save the art in .eps format which can be viewed using Inkscape.
getcanvas().postscript(file="triangle.eps")
sleep(5)
