"""
On page-11:-
Write and run a function that draws 60 squares, turning right 5 degree after each square.
Use a loop! Your result should end up looking like this:
"""

from turtle import *
from time import sleep


def squares():
    for i in range(4):
        forward(100)
        right(90)


def sixtySquares():
    for i in range(60):
        squares()
        right(5)


sixtySquares()
sleep(5)
