with open("input.txt","r") as input:
    pairs = [([int(elfNum) for elfNum in elf[0].split("-")], [int(elfNum) for elfNum in elf[1].split("-")]) for elf in [line.strip().split(",") for line in input.readlines()]]
    fullyContainedPairs = 0
    for pair in pairs:
        if pair[0][0] >= pair[1][0] and pair[0][1]<=pair[1][1]:
            fullyContainedPairs += 1
        elif pair[1][0] >= pair[0][0] and pair[1][1]<=pair[0][1]:
            fullyContainedPairs += 1
    print("Part 1:",fullyContainedPairs)
    anyContainedPairs = 0
    for pair in pairs:
        if pair[0][0] <= pair[1][0]:
            if pair[1][0] <= pair[0][1]:
                anyContainedPairs += 1
        elif pair[1][0] <= pair[0][0]:
            if pair[0][0] <= pair[1][1]:
                anyContainedPairs += 1
    print("Part 2:",anyContainedPairs)
