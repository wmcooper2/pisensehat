#!/usr/bin/env python3
# traindata.py
"""Gathering motion-data from the Sense Hat."""

# stand lib
import csv
from datetime import datetime

# 3rd party
from sense_hat import SenseHat

# custom
from ledcodes import clear_screen
from ledcodes import running
from trainutil import filename
from trainutil import motion


def begin_session() -> None:
    sh = SenseHat()
    running(sh)
    print("Collecting sensor data...")
    session = []
    start = datetime.now()
    while True:
        try:
            session.append(motion(sh))
        except KeyboardInterrupt:
            print("\nStopped manually.")
            break
    end = datetime.now()
    print("Finished collecting sensor data.")
    
    session_file = "../sessions/" + filename(start, end)
    print("Writing session to file.")
    with open(session_file, "w+") as log:
        writer = csv.writer(log)
        writer.writerow(["timestamp",
                        "mag_x", "mag_y", "mag_z",
                        "acc_x", "acc_y", "acc_z",
                        "gryo_x", "gryo_y", "gryo_z"])
        for line in session:
            writer.writerow(line)
    print("Finished writing session to file.")
    clear_screen(sh)
    return None


# if __name__ == "__main__":
    # need menu for choosing train and start end point
    # can only use joystick as input
    # up, down, left, right, center click
