with open("input.txt","r") as input:
    elveTotals = sorted([sum([int(food) for food in elve.split("\n")]) for elve in input.read().split("\n\n")], reverse=True)
    print(elveTotals[0])
    print(sum(elveTotals[0:3]))