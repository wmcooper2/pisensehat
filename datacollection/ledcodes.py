#!/usr/bin/env python3
"""Displaying messages on the 8x8 LED matrix on the Sense Hat."""

# 3rd party
from sense_hat import SenseHat

# custom
from colors import (
        BLACK,
        BLUE,
        GREEN,
        RED,
        WHITE,)
from shapes import okay

# Error codes
# reset required
# no space on micro SD card
# low battery, powering down
# clearing cache
# need to clear cache


def clear_screen(sh):
    """Turns off the leds. 'obj' is sense hat instance. Returns None."""
    sh.clear(BLACK)


def running(sh):
    """Displays running light indicator. Returns None."""
    sh.set_pixels(okay(GREEN, BLACK))


if __name__ == "__main__":
    sh = SenseHat()
    running(sh)
    print("Testing LED display...")
