#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False
    """
    num_following_bytes = 0

    for byte in data:
        if num_following_bytes > 0 and (byte >> 6) == 0b10:
            num_following_bytes -= 1
        elif num_following_bytes == 0:
            if (byte >> 7) == 0b0:
                num_following_bytes = 0
            elif (byte >> 5) == 0b110:
                num_following_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_following_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_following_bytes = 3
            else:
                return False
        else:
            return False

    return num_following_bytes == 0
