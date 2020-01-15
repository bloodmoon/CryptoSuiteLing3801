class ShiftDecode:
    def __init__(self, shift_val):
        self.shiftVal = shift_val

    def decode_char(self, char_in):
        char_cap = char_in.capitalize()
        if (ord(char_cap) + self.shiftVal) < 91:
            return chr(ord(char_cap) + self.shiftVal)
        else:
            return chr(ord(char_cap) + self.shiftVal - 26)


# remove after testing
test = ShiftDecode(26)
print(test.decode_char('A'))
