with open("input.txt","r") as input:
    input = input.read()
    sumInd = 0
    for line in input.split("\n"):
        compartment1 = (line[:int(len(line)/2)])
        compartment2 = (line[int(len(line)/2):])
        for character in compartment1:
            if character in compartment2:
                characterOrd = ord(character.swapcase())-64
                sumInd += characterOrd if characterOrd < 28 else characterOrd - 6
                break
    sumGroup = 0
    for group in [input.split("\n")[i:i+3] for i in range(0, len(input.split("\n")), 3)]:
        for character in group[0]:
            if character in group[1] and character in group[2]:
                characterOrd = ord(character.swapcase())-64
                sumGroup += characterOrd if characterOrd < 28 else characterOrd - 6
                break
    print(sumInd)
    print(sumGroup)