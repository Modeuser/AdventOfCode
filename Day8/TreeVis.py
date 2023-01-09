# a function that takes in the position of an int and content
# check if any value from it to the edge is >= to it
# returns true if nothing is larger than it
# else returns false
def visChecker(row,colm,content):
    # store all front numbers in this row into a list
    # store all back numbers in this row into a list
    # find the max number for each list
    # compare if larger than numbIQ
    frontRow = content[row][:colm]
    backRow = content[row][colm+1:-1] #-1 remove \n
    
    currentValue = int(content[row][colm])
    # currentValue = int(currentValue)
    # to get the ints above this row (same colm)
    aboveColm = []
    belowColm = []
    for C_row in range(row-1,-1,-1):
        aboveColm.append(content[C_row][colm])
    for B_row in range(len(content)-1,row,-1):
        belowColm.append(content[B_row][colm])

    # map all char in 'frontRow' as an int, make it into a list
    # then find the max int in this list
    FRMAX = max(list(map(int,frontRow)))
    BRMAX = max(list(map(int,backRow)))
    ACMAX = max(map(int,aboveColm))
    BCMAX = max(map(int,belowColm))

    ALLMAX = [FRMAX,BRMAX,ACMAX,BCMAX]
    visMin = min(ALLMAX)

    #print(FRMAX,BRMAX,ACMAX,BCMAX,visMin)

    if visMin >= currentValue:
        return False
    else:
        return True


#=================================(main)
def main():
    with open('TreeLog.txt') as file:
        content = file.readlines()

        visCounter = 0
        TFValue = 0

        # content[0] is row 0, it has +1 due to \n
        # therefore we -2 to account for \n
        for row in range(1,len(content[0])-2):
            for colm in range(1,len(content)-1):

                # we pass the position of this each int to a function
                # which returns t/f
                # if true, increment the counter by 1
                # if false, do nothing
                TFValue = visChecker(row,colm,content)

                if TFValue:
                    visCounter += 1
        print(visCounter)

if __name__ == '__main__':
    main()