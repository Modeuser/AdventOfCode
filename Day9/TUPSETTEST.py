# map method:
# we can make a 2D map after we know how many
# up, down, left, right moves there are in total

# then we can change the value of the 2D map whenver 'T' is on it

# one function will move H and T accordingly
# one function will change the value of the index at T

def mapMaker(content):
    maxWidth = 0
    maxHeight = 0
    
    for line in range(len(content)):
        if content[line][0] == 'R' or content[line][0] == 'L':
            appendAmount = int(content[line][2])
            maxWidth += appendAmount
        if content[line][0] == 'D' or content[line][0] == 'U':
            appendAmount = int(content[line][2])
            maxHeight += appendAmount

    print(maxWidth,maxHeight)

    maxMap = [[0]*maxWidth]*maxHeight
    return maxMap



#====================================(main)
def main():
    with open('MoveLogTEST.txt') as file:
        content = file.readlines()

        maxMap = mapMaker(content)
        print(maxMap)


if __name__ == '__main__':
    main()