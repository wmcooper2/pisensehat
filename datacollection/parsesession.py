#!/usr/bin/env python3
"""Module for parsing the raw data from the data collecting sessions."""

from pathlib import Path
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np


def open_session(file_):
    """Gets session data. Returns List."""
    with open(file_, "r") as f:
        return f.readlines()


def parse_sample(sample):
    """Parse a sample. Returns List."""
    return list(sample.split(","))


if __name__ == "__main__":
    file_ = "../sessions/2019-04-18__02:31:48__02:32:22"
    lines = open_session(file_)
    header = lines[0].strip().split(",")                # header line

    # remove newline characters
    data = []
    for line in lines[1:]:
        data.append(line.strip())

    # separate the data into categories
    magx, magy, magz = [], [], []
    accx, accy, accz = [], [], []
    gyrox, gyroy, gyroz = [], [], []

    # later, use zip with function?
    for sample in data:
        temp = sample.split(",")
        magx.append(float(temp[1]))
        magy.append(float(temp[2]))
        magz.append(float(temp[3]))
        accx.append(float(temp[4]))
        accy.append(float(temp[5]))
        accz.append(float(temp[6]))
        gyrox.append(float(temp[7]))
        gyroy.append(float(temp[8]))
        gyroz.append(float(temp[9]))

    # make a graph
    plt.ylabel("stuff")
    plt.xlabel("time")

    plt.plot(magx)
    plt.plot(magy)
    plt.plot(magz)

    plt.plot(accx)
    plt.plot(accy)
    plt.plot(accz)

    plt.plot(gyrox)
    plt.plot(gyroy)
    plt.plot(gyroz)


    fig, axes = plt.subplots(1,3)
    

    plt.show()
