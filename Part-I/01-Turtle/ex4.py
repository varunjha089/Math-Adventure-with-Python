"""
On page-14:-
Write a function called polygon() that takes an integer as an argument and makes the turtle draw a polygon
with that integer's number of sides.
"""

from turtle import *
from time import sleep


def polygon(sidelength=100, sides=3):
    for i in range(sides):
        forward(sidelength)
        right(360 / sides)


polygon(sides=15)
sleep(5)
