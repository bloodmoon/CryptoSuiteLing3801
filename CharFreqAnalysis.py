"""
Author: Brian Batey

A simple program that takes a text file of cipherText as input and can perform character
frequency analysis and linear shifting.

Allows for shifting the full range [0-25] and viewing the cipher and/or writing to file at
anytime.

Initial shift attempts to align the most frequent character to the character 'E'
"""

import string
from ShiftDecoder import ShiftDecode

# Setup File I/O and get user response
inputFile = open(input("Please enter the path/name of the cipher text file: "))
outputFile = open(input("Please enter the path/name of the desired output file: "), "w")

# Create Map of Uppercase ASCII chars
charMap = dict.fromkeys(string.ascii_uppercase, 0)

# List for cipher text storage
cipherText = []

# Default Shift is 0
shift = 0

# Count individual characters from cipherText and store in charMap
while True:
    currentChar = inputFile.read(1)
    if currentChar is '':  # Check if EOF is reached
        break
    else:
        cipherText.append(currentChar)
        if currentChar is not ' ' and currentChar is not '\n':
            charMap[currentChar] = charMap.get(currentChar)+1  # increment character count

# for x in charMap:
    # print(x, end="")
    # print(" ", charMap.get(x))

# Code Snippet modified from :
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

# Reverse dictionary for easy printing
sListRev = {k: v for k, v in sorted(charMap.items(), reverse=True, key=lambda item: item[1])}
outputFile.write("CipherText Distribution: \n")
outputFile.write(str(sListRev))
outputFile.write("\n")

# Re-order dictionary
sList = {k: v for k, v in sorted(charMap.items(), key=lambda item: item[1])}

# Get Max Value Key
mostFreqChar = sList.popitem()[0]

# Match most frequent character to most frequently used English letter 'E'
if mostFreqChar is not 'E':
    shift = ord('E') - ord(mostFreqChar)

    # Using Strictly Positive Shift Values
    if shift <= 0:
        shift = shift + 26

# Write to file and formatting
outputFile.write("Most Frequent character found is : ")
print("Most Frequent character found is : " + mostFreqChar)
outputFile.write(str(mostFreqChar))
outputFile.write("\n")

outputFile.write("Amount of Shift Required to Shift to \"E\" : ")
print("Amount of Shift Required to Shift to \"E\" : " + str(shift))
outputFile.write(str(shift))
outputFile.write("\n\n")

# Write CipherText as plaintext with approximated shift
# Shift current character from "element" and file writing / formatting
decoder = ShiftDecode(shift)
shiftDict = {}

# Create shifted Dictionary for manipulation
for k, v in sListRev.items():
    shiftDict[decoder.decode_char(k)] = v

# output to file
outputFile.write("Shifted distribution: \n")
outputFile.write(str(shiftDict))
outputFile.write("\n")

# Decode cipherText and write to file
for ele in cipherText:
    if ord(ele) is 10:
        outputFile.write("\n")
    elif ele is not ' ':
        outputFile.write(decoder.decode_char(ele).lower())

# Enter interactive loop
while True:
    print("\nCurrent Shift:", shift)
    print("Current Distribution: ")
    print(shiftDict)
    print()

    userPress = input("Enter l to shift left (-1), r to shift right(+1), "
                      "d to view shifted plaintext, \nw to write to file, or q to quit:")
    if userPress is 'q':  # Quit Command
        inputFile.close()
        outputFile.close()
        print("\nGOODBYE!!!")
        break

    elif userPress is 'r':  # Shift Right ( + 1)
        shift = shift+1
        if shift > 25:
            shift = shift-26

    elif userPress is 'l':  # Shift Left ( -1 )
        shift = shift-1
        if shift < 0:
            shift = shift+26

    elif userPress is 'w':  # Write current shift/plaintext to file
        outputFile.write("\n\n")
        outputFile.write("Current Shift: " + str(shift))
        outputFile.write("\n")
        outputFile.write(str(shiftDict) + "\n")

        for ele in cipherText:
            if ord(ele) is 10:
                outputFile.write("\n")
            elif ele is not ' ':
                outputFile.write(decoder.decode_char(ele).lower())

    elif userPress is 'd':  # view plaintext from cipherText with current shift

        print("PlainText with Current Shift is: ")
        for ele in cipherText:
            if ord(ele) is 10:
                print()
            elif ele is not ' ':
                print(decoder.decode_char(ele).lower(), end="")
            else:
                print(" ", end="")

    # update ShiftDecoder with current shift values
    decoder = ShiftDecode(shift)

    # update ShiftDict for current distribution
    shiftDict = {}
    for k, v in sListRev.items():
        shiftDict[decoder.decode_char(k)] = v
