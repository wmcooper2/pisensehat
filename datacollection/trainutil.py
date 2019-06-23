# trainutil.py
"""Utility module for train data collection project."""

# stand lib
from datetime import datetime
from time import sleep
from typing import Any
from typing import List
from typing import Text


def motion(sh) -> List[Text]:
    """Gets motion sensor data. Returns List."""
    mag = sh.get_compass_raw()
    acc = sh.get_accelerometer_raw()
    gyro = sh.get_gyroscope_raw()
    data = [
        datetime.now(),
        round(mag["x"], 3), round(mag["y"], 3), round(mag["z"], 3),
        round(acc["x"], 3), round(acc["y"], 3), round(acc["z"], 3),
        round(gyro["x"], 3), round(gyro["y"], 3), round(gyro["z"], 3)]
    return data


def filename(start: Any, end: Any) -> Text:
    """Formats file name from start/end datetimes. Returns String."""
    date = datetime.strftime(start, "%Y-%m-%d")
    time_start = datetime.strftime(start, "%H:%M:%S")
    time_end = datetime.strftime(end, "%H:%M:%S")
    return "__".join([date, time_start, time_end])


if __name__ == "__main__":
    start_time = datetime.now()
    sleep(1)
    print(filename(start_time, datetime.now()))
