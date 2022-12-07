def findFirstAmountWithouDupesInString(string, numberOf):
    for i in range(len(inputStr)-numberOf):
        chars = []
        for e in range(numberOf):
            chars.append(inputStr[i+numberOf-1-e])
        if len(chars) == len(list(dict.fromkeys(chars))):
            print(i+numberOf)
            break
with open("input.txt","r") as input:
    inputStr = input.read().strip()
    findFirstAmountWithouDupesInString(input, 14)