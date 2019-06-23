#!/usr/bin/env python3
"""Check power supply."""

# stand lib
import subprocess as sp
from typing import Text

DEBUG = False
all_good = "throttled=0x0"
cmd = "/opt/vc/bin/vcgencmd get_throttled"


def status(cmd: Text) -> Text:
    """Get power status. Return String."""
    return str(sp.run(cmd, stdout=sp.PIPE,
               shell=True).stdout).lstrip("b'throttled=").rstrip("\\n'")


def convert_values_to_bin(values: List[Text]) -> List[Text]:
    """Converts a string to binary. Returns List."""
    temp = []
    for value in values:
        temp.append(str(bin(int(value)))[2:])
    return temp


def pad_digits(digit: Text) -> Text:
    """Pads the missing digits from a binary representation. Returns String."""
    if len(digit) is 1:
        return "000" + digit
    elif len(digit) is 2:
        return "00" + digit
    elif len(digit) is 3:
        return "0" + digit
    return digit


if __name__ == "__main__":
    if DEBUG:
        response = "0x50005"
    else:
        response = status(cmd)
        print(response)

    # easy way, for now
    if status(cmd) != "0x0":
        print("Some kind of error.")
    else:
        print("All good.")

    # long way, but works
#     binary = convert_values_to_bin(response[2:])
#     long_binary = []
#     for digit in binary:
#         long_binary.append(pad_digits(digit))
#     answer = "".join(long_binary)
#     new_ans = []
#     for char in answer[::-1]:
#         new_ans.append(char)
#     result = "".join(new_ans)
#     print(result[2])
