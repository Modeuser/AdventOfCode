currentSum = 0
largestSum = 0

firstSum = 0
secondSum = 0
thirdSum = 0

with open('CalLog.txt') as fileCalLog:
    # this will get the 1st largest sum
    for line in fileCalLog.readlines():
        if line != "\n":
            currentSum += int(line)
        elif line == "\n":
            if currentSum > largestSum:
                largestSum = currentSum
            currentSum = 0
    #stores 1st largest sum
    firstSum = largestSum

    # resets w/r position and largest sum
    fileCalLog.seek(0)
    largestSum = 0
    # this will get the second largest sum
    for line in fileCalLog.readlines():
        if line != "\n":
            currentSum += int(line)
        elif line == "\n":
            if currentSum > largestSum and currentSum < firstSum:
                largestSum = currentSum
            currentSum = 0
    #stores 2nd largest sum
    secondSum = largestSum

    # resets w/r position and largest sum
    fileCalLog.seek(0)
    largestSum = 0
    # this will get the third largest sum
    for line in fileCalLog.readlines():
        if line != "\n":
            currentSum += int(line)
        elif line == "\n":
            if currentSum > largestSum and currentSum < secondSum:
                largestSum = currentSum
            currentSum = 0
    #stores 2nd largest sum
    thirdSum = largestSum

    print(largestSum)
    print(firstSum)
    print(secondSum)
    print(thirdSum)