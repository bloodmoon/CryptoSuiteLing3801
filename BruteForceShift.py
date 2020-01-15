from ShiftDecoder import ShiftDecode
shiftList = list(range(26))
file = open("test.txt")

cipherText = []

while True:
    currentChar = file.read(1)
    if currentChar is '':
        break
    else:
        cipherText.append(currentChar)

print(cipherText)

for element in shiftList:
    print()
    print(element)

    test = ShiftDecode(element)
    for ele in cipherText:
        if ord(ele) is 10:
            print(" ")
        elif ele is not ' ':
            print(test.decode_char(ele).lower(), end='')
        # else:
        #     print(ele, end="")

