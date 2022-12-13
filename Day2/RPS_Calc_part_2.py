# part 2 logic
# we can use the native XYZ to get score for all rounds summed
# we need to determine what choice is made in each round

# X = lose = 0
# Y = draw = 3
# Z = win = 6

# We'll sum the score for both winning and choice value
# during the match-case statement

# variables
totalScore = 0

with open('RPSLog.txt') as fileRPSLog:
    for line in fileRPSLog.readlines():
        match line[2]:
            case 'X' if line[0] == 'A':
                totalScore += 3
            case 'X' if line[0] == 'B':
                totalScore += 1
            case 'X' if line[0] == 'C':
                totalScore += 2
            case 'Z' if line[0] == 'A':
                totalScore += 8
            case 'Z' if line[0] == 'B':
                totalScore += 9
            case 'Z' if line[0] == 'C':
                totalScore += 7
            case 'Y' if line[0] == 'A':
                totalScore += 4
            case 'Y' if line[0] == 'B':
                totalScore += 5
            case 'Y' if line[0] == 'C':
                totalScore += 6
            case other:
                print("invalid comparison encountered?!")
    print(totalScore)