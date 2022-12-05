import copy
with open("input.txt", "r") as input:
    inputParts = input.read().split("\n\n")
    stacks = []
    for line in inputParts[0].split("\n")[:-1]:
        lineC = []
        for group in [line[i:i+4] for i in range(0, len(line), 4)]:
            lineC.append(group)
        stacks.append(lineC)
    stacksList = [[] for num in inputParts[0].split("\n")[-1].split("   ")]
    for i in [int(num.strip()) for num in inputParts[0].split("\n")[-1].split("   ")]:
        for stack in range(len(stacks)):
            if stacks[stack][i-1].strip(" []") != "":
                stacksList[i-1].append(stacks[stack][i-1].strip(" []"))
    for list in range(len(stacksList)):
        stacksList[list] = stacksList[list][::-1]
    p1StacksList = copy.deepcopy(stacksList)
    inputs = [(inputLine.split(" ")[1],inputLine.split(" ")[3],inputLine.split(" ")[5]) for inputLine in inputParts[1].split("\n")]
    for move in inputs:
        for _ in range(int(move[0])):
            fromList = p1StacksList[int(move[1])-1].pop()
            p1StacksList[int(move[2])-1].append(fromList)
    for i in p1StacksList:
        print(i[-1], end="")
    print("")
    for move in inputs:
        moving = []
        for _ in range(int(move[0])):
            fromList = stacksList[int(move[1])-1].pop()
            moving.append(fromList)
        moving = moving[::-1]
        stacksList[int(move[2])-1].extend(moving)
    
    for i in stacksList:
        print(i[-1], end="")
    print("")
