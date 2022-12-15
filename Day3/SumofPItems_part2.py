# try using "if x in y" to check

# import the "valueOfChar" function from part 1
from SumofPItems import valueOfChar

SumofBadge = 0

# A function that:
# Takes in 3 arrays (x,y,z)
# returns the common char found in all 3 arrays
# EA = each
def commonChar (x, y, z):
    for EA in x:
        if EA in y and EA in z:
            return EA


# main function
with open('SackLog.txt') as fileLog:
    content = fileLog.readlines()
    # E3L = every 3 lines
    for E3L in range(0, len(content), 3):
        SumofBadge += valueOfChar(commonChar(content[E3L], content[E3L+1], content[E3L+2]))
    print(SumofBadge)