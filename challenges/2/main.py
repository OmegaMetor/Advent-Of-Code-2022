def scoreGame(elfChoice, yourChoice):
    elfChoice = elfChoice.strip()
    yourChoice = yourChoice.strip()
    # X = lose
    # Y = draw
    # Z = win
    # A = rock
    # B = paper
    # C = scisors
    score = 0
    match yourChoice:
        case "X":
            score += 0
            match elfChoice:
                case "A":
                    score += 3
                case "B":
                    score += 1
                case "C":
                    score += 2
        case "Y":
            score += 3
            match elfChoice:
                case "A":
                    score += 1
                case "B":
                    score += 2
                case "C":
                    score += 3
        case "Z":
            score += 6
            match elfChoice:
                case "A":
                    score += 2
                case "B":
                    score += 3
                case "C":
                    score += 1
    return score
    


with open("input.txt","r") as input:
    scores = []
    for line in input.readlines():
        scores.append(scoreGame(line.split(" ")[0], line.split(" ")[1]))
    print(sum(scores))