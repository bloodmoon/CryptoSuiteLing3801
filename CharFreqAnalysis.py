import string

# Setup File I/O and get user response
inputFile = open(input("Please enter the path/name of the cipher text file: "))
outputFile = open(input("Please enter the path/name of the desired output file: "), "w")

# Create Map of Uppercase ASCII chars
charMap = dict.fromkeys(string.ascii_uppercase, 0)

# List for cipher text storage
cipherText = []

# Count individual characters from cipherText and store in charMap
while True:
    currentChar = inputFile.read(1)
    if currentChar is '':  # Check if EOF is reached
        break
    else:
        cipherText.append(currentChar)
        if currentChar is not ' ' and currentChar is not '\n':
            charMap[currentChar] = charMap.get(currentChar)+1  # increment character count

for x in charMap:
    print(x, end="")
    print(" ", charMap.get(x))
