#!/usr/bin/env python3
"""Making shapes on the Sense Hat 8x8 LED matrix."""

# stand lib
from time import sleep
from typing import Tuple

# 3rd party
from sense_hat import SenseHat


def checker_board(fg:, bg):
    X = fg
    O = bg
    return [X, O, X, O, X, O, X, O,  
            O, X, O, X, O, X, O, X,  
            X, O, X, O, X, O, X, O, 
            O, X, O, X, O, X, O, X, 
            X, O, X, O, X, O, X, O, 
            O, X, O, X, O, X, O, X, 
            X, O, X, O, X, O, X, O, 
            O, X, O, X, O, X, O, X,]


def frowney(fg, bg):
    X = fg
    O = bg
    return [O, O, X, X, X, X, O, O,  
            O, X, O, O, O, O, X, O, 
            X, O, X, O, O, X, O, X, 
            X, O, O, O, O, O, O, X, 
            X, O, O, X, X, O, O, X, 
            X, O, X, O, O, X, O, X, 
            O, X, O, O, O, O, X, O, 
            O, O, X, X, X, X, O, O,]


def okay(fg, bg):
    X = fg
    O = bg
    return [O, O, O, O, O, O, O, O,  
            O, X, X, O, X, O, O, X, 
            X, O, O, X, X, O, X, O, 
            X, O, O, X, X, X, O, O, 
            X, O, O, X, X, X, O, O, 
            X, O, O, X, X, O, X, O, 
            O, X, X, O, X, O, O, X, 
            O, O, O, O, O, O, O, O,]


def solid(fg, bg):
    X = fg
    O = bg
    return [O, O, O, O, O, O, O, O,  
            O, O, O, O, O, O, O, O, 
            O, O, O, O, O, O, O, O, 
            O, O, O, O, O, O, O, O, 
            O, O, O, O, O, O, O, O, 
            O, O, O, O, O, O, O, O, 
            O, O, O, O, O, O, O, O, 
            O, O, O, O, O, O, O, O,]


def small_zero(fg, bg):
    O = fg
    X = bg
    return [X, X, X, X, X, X, X, X,  
            X, X, X, O, O, X, X, X, 
            X, X, O, X, X, O, X, X, 
            X, X, O, X, X, O, X, X, 
            X, X, O, X, X, O, X, X, 
            X, X, O, X, X, O, X, X, 
            X, X, X, O, O, X, X, X, 
            X, X, X, X, X, X, X, X,]


def smiley(fg, bg):
    X = fg
    O = bg
    return [O, O, X, X, X, X, O, O,  
            O, X, O, O, O, O, X, O, 
            X, O, X, O, O, X, O, X, 
            X, O, O, O, O, O, O, X, 
            X, O, X, O, O, X, O, X, 
            X, O, O, X, X, O, O, X, 
            O, X, O, O, O, O, X, O, 
            O, O, X, X, X, X, O, O,]


    def train(fg: Tuple[int, int, int],
              bg: Tuple[int, int, int]) -> None:
    X = fg
    O = bg
    return [O, X, X, X, O, O, O, O,  
            O, O, X, O, O, O, O, O, 
            O, O, O, X, O, O, O, O, 
            O, X, X, X, X, X, X, O, 
            X, O, O, O, O, O, O, X, 
            X, O, O, O, O, O, O, X, 
            X, X, X, X, X, X, X, X, 
            O, X, X, O, O, X, X, O,]


if __name__ == "__main__":
    from colors import *
    sh = SenseHat()
    sh.set_pixels(train(WHITE, BLACK))
    sleep(3)
    sh.clear()
