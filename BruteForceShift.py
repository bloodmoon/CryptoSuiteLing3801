"""
Author: Brian Batey

A simple program to brute force
a Shift Cipher that utilizes a non-random (consecutive) character shift.

Takes a text file as input for the cipher text and outputs a text file
containing every consecutive alphabetical shift in the range of (0-25)
"""
from ShiftDecoder import ShiftDecode

# Setup Variables
shiftList = list(range(26))
cipherText = []

# Setup File I/O and get user response
inputFile = open(input("Please enter the path/name of the cipher text file: "))
outputFile = open(input("Please enter the path/name of the desired output file: "), "w")


# Read characters into cipherText list from input file
while True:
    currentChar = inputFile.read(1)
    if currentChar is '':  # Check if EOF is reached
        break
    else:
        cipherText.append(currentChar)

# Shift each character using ShiftDecode object and output result to file
for element in shiftList:
    outputFile.write("\n")
    outputFile.write(str(element))
    outputFile.write("\n")

    # Shift current character from "element" and file writing / formatting
    shiftedChar = ShiftDecode(element)
    for ele in cipherText:
        if ord(ele) is 10:
            outputFile.write("\n")
        elif ele is not ' ':
            outputFile.write(shiftedChar.decode_char(ele).lower())
    outputFile.write("\n")

# Cleanup
inputFile.close()
outputFile.close()
