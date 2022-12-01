with open("input.txt","r") as input:
    inputStr = input.read()
    elves = inputStr.split("\n\n")
    elveTotals = []
    for elve in elves:
        elveLines = elve.split("\n")
        elveTotal = 0
        for line in elveLines:
            elveTotal += int(line)
        elveTotals.append(elveTotal)
    elveTotals.sort(reverse=True)
    print(elveTotals[0])
    print(elveTotals[0]+elveTotals[1]+elveTotals[2])