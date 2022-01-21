"""
Page:- 18
First write a 'star' function that will draw a five-pointed star,
Next, write a function called 'starSpiral()' that will draw a spiral of stars.
"""
from turtle import *
from time import sleep


def star(length):
    for i in range(5):
        forward(length)
        right(144)


def repeater(times=50):
    length = 5
    for i in range(times):
        star(length)
        length = length + 5
        right(20)


repeater(20)
sleep(5)
