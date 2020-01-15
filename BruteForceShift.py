from ShiftDecoder import ShiftDecode
shiftList = list(range(26))
inputFile = open("cipherText.txt")
outputFile = open("plainText.txt", "w")

cipherText = []

while True:
    currentChar = inputFile.read(1)
    if currentChar is '':
        break
    else:
        cipherText.append(currentChar)

for element in shiftList:
    outputFile.write("\n")
    outputFile.write(str(element))
    outputFile.write("\n")

    test = ShiftDecode(element)
    for ele in cipherText:
        if ord(ele) is 10:
            outputFile.write("\n")
        elif ele is not ' ':
            outputFile.write(test.decode_char(ele).lower())
    outputFile.write("\n")

inputFile.close()
outputFile.close()
