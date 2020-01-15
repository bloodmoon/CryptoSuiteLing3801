"""
Author: Brian Batey

ShiftDecode Class

Shifts an input ASCII character by the designated shift value.
Valid ASCII input is only characters in the range [A - Z] and [a - z]

Parameter
    shift_val
        Integer used to set the shift value
        Valid Shift range is 0 to 25
"""


class ShiftDecode:

    def __init__(self, shift_val):

        # If no shift_val is input default to no shift
        if shift_val is None:
            self.shift_val = 0
        else:
            if (shift_val >=0) or (shift_val <= 25):
                self.shiftVal = shift_val

    def decode_char(self, char_in):

        # Force Capitalization
        char_cap = char_in.capitalize()

        # Shift character in ASCII
        if (ord(char_cap) + self.shiftVal) < 91:
            return chr(ord(char_cap) + self.shiftVal)
        else:
            return chr(ord(char_cap) + self.shiftVal - 26)
