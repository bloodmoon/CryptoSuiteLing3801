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
sList = {k: v for k, v in sorted(charMap.items(), key=lambda item: item[1])}
mostFreqChar = sList.popitem()[0]

if mostFreqChar is not 'E':
    shift = ord('E') - ord(mostFreqChar)

    if shift <= 0:
        shift = shift + 26

outputFile.write("Most Frequent character found is : ")
outputFile.write(str(mostFreqChar))
outputFile.write("\n")
outputFile.write("Amount of Shift Required to Shift to \"E\" : ")
outputFile.write(str(shift))
outputFile.write("\n")

# Shift current character from "element" and file writing / formatting
decoder = ShiftDecode(element)
for ele in cipherText:
    if ord(ele) is 10:
        outputFile.write("\n")
    elif ele is not ' ':
        outputFile.write(decoder.decode_char(ele).lower())

outputFile.write("\n")
