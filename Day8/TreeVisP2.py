# a function that takes in the position of an int and content
# check if any value from it to the edge is >= to it
# returns true if nothing is larger than it
# else returns false
def visChecker(row,colm,content):

    currentValue = int(content[row][colm])
    aboveCounter = 0
    belowCounter = 0
    frontCounter = 0
    backCounter = 0
    # above and below counter (working)
    for A_row in range(row-1,-1,-1):
        adjValue = int(content[A_row][colm])
        if adjValue < currentValue:
            aboveCounter += 1
        else:
            aboveCounter += 1
            break
    for B_row in range(row+1,len(content)):
        adjValue = int(content[B_row][colm])
        if adjValue < currentValue:
            belowCounter += 1
        else:
            belowCounter += 1
            break
    
    # front and back counter
    for F_col in range(colm-1,-1,-1):
        adjValue = int(content[row][F_col])
        if adjValue < currentValue:
            frontCounter += 1
        else:
            frontCounter += 1
            break
    for B_col in range(colm+1,len(content[0])-1):
        adjValue = int(content[row][B_col])
        if adjValue < currentValue:
            backCounter += 1
        else:
            backCounter += 1
            break
    
    #print(frontCounter,aboveCounter,backCounter,belowCounter)
    scenicScore = frontCounter*aboveCounter*backCounter*belowCounter

    return scenicScore


#=================================(main)
def main():
    with open('TreeLog.txt') as file:
        content = file.readlines()

        currentScore = 0
        scenicScore = 0

        # content[0] is row 0, it has +1 due to \n
        # therefore we -2 to account for \n
        for row in range(1,len(content[0])-2):
            for colm in range(1,len(content)-1):

                # we pass the position of this each int to a function
                # which returns t/f
                # if true, increment the counter by 1
                # if false, do nothing
                scenicScore = visChecker(row,colm,content)

                if scenicScore > currentScore:
                    currentScore = scenicScore
        print(currentScore)

if __name__ == '__main__':
    main()