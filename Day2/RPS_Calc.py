# variables
oppChoice = 0
youChoice = 0

totalScore = 0
# rules: A<B<C = X<Y<Z = R<P<S

# The logic
# 1.Store both inputs as numbers
# 2.Make logical comparisons between the numbers to
#    determine win/lose
# 3.Add the value of their choice (1,2,3) with score of this
#   round (0,3,6) for every round

# actual program
with open('RPSLog.txt') as fileRPSLog:
    for line in fileRPSLog.readlines():
        match line[0]:
            case 'A':
                oppChoice = 1
            case 'B':
                oppChoice = 2
            case 'C':
                oppChoice = 3
        match line[2]:
            case 'X':
                youChoice = 1
            case 'Y':
                youChoice = 2
            case 'Z':
                youChoice = 3
        match youChoice:
            case _ if youChoice - oppChoice == 1 or youChoice - oppChoice == -2:
                totalScore += 6
            case _ if youChoice - oppChoice == -1 or youChoice - oppChoice == 2:
                totalScore += 0
            case _ if youChoice == oppChoice:
                totalScore += 3
            case other:
                print("invalid comparison encountered?!")
        # add the value of your choice into the total score
        totalScore += youChoice
    print(totalScore)