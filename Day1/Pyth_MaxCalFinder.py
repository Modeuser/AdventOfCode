currentSum = 0
largestSum = 0

with open('CalLog.txt') as fileCalLog:
    # for line in fileCalLog.readlines():
    for line in fileCalLog.readlines():
        if line != "\n":
            currentSum += int(line)
        elif line == "\n":
            if currentSum >= largestSum:
                largestSum = currentSum
            currentSum = 0
    print(largestSum)