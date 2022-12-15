# we might be able to use the find() function
# to check for overlap
# by specifying the range of which some
# values should be found

# track overlaps
SumofOverlaps = 0

# A function that:
# 1. takes in a line
# 2. returns the 4 values
#    e.g: 99-99,18-99 into 99,99,18,99
def valueID (line):

    # finds the position of the markers (commas and dashes)
    commaPosition = line.find(',')
    dash1Position = line.find('-', 0, commaPosition)
    dash2Position = line.find('-', commaPosition, len(line))
    # TT print(commaPosition, dash1Position, dash2Position)

    a = line[0:dash1Position]
    b = line[dash1Position+1:commaPosition]
    x = line[commaPosition+1:dash2Position]
    y = line[dash2Position+1:len(line)]
    return int(a),int(b),int(x),int(y)

# # A function that:
# # 1. takes in values a,b x,y
# # 2. checks if values between a-b can be found between x-y
# #    or vice versa
# # 3. returns true if overlap occured
def overlapID (a,b,x,y):
    for values in range(a,b+1): # stops at b+1, includes b
        if values in range(x,y+1): # same as above
            check1 = True
            break
            # if there's even a single 'false'
            # i.e one value in a-b is not in x-y
            # then they don't overlap
        else:
            check1 = False
    # now we check the vice versa (is x-y in a-b)
    for values in range(x,y+1):
        if values in range(a,b+1):
            check2 = True
            break
        else:
            check2 = False
    # if either one of the checks is true, overlap return true
    if check1 or check2:
        return True
    else:
        return False


# main function
with open('PairLog.txt') as file:
    content = file.readlines()

    for line in range(len(content)):
        a, b, x, y = valueID(content[line])
        if overlapID(a, b, x, y):
            SumofOverlaps += 1
    print(SumofOverlaps)