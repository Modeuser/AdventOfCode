# in python, ord(x) will convert x into a int ASCII value

SumOfItems = 0

# create another function that returns the value of a char
def valueOfChar (x):
    if x.isupper():
        return ord(x) - 38
    elif x.islower():
        return ord(x) - 96
    else:
        return 0

# another function that returns the common letter in a line
# x is a line here
def commonLetter (x):
    # if line length is even (ie when there's no \n)
    # remove 1
    if len(x) % 2 == 0:
        lineLength = len(x)
    else:
        lineLength = len(x) - 1
    # loop through the first half
    for firstHalf in range(int(lineLength/2)):
        # loop through the second half
        for secondHalf in range(int(lineLength/2), lineLength):
            if x[firstHalf] == x[secondHalf]:
                return x[firstHalf]



with open ('SackLog.txt') as fileLog:
    for line in fileLog.readlines():
        SumOfItems += valueOfChar(commonLetter(line))
    print(SumOfItems)