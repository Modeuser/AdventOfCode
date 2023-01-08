# ========================================
# Thoughts
# for each 'dir xyz' there must be a corresponding 'cd ..'

# Pseudo code
#   for each '$ ls', between this line and the end:

#       sizeTracker = 0
#       dirTracker = 0

#       find the next '$' line

#       (now we have the start of the dir and the end of the dir)

#       for each line between the start and the end of this 'ls'
#           if the line is a number:
#               parse it and add it to the sizeTracker
#           if the line is a 'dir':
#               dirTracker += 1
#           if the line starts with '$':
#               break
#       for each line between the start and the entire log
#           while dirTracker is not 0:
#               if the line starts with number:
#                   add number to sizeTracker
#               if the line is '$ cd ..':
#                   dirTracker -= 1
#               if the line starts with 'dir xyz':
#                   dirTracker += 1


#           if the sizeTracker is > 100000:
#               return 0
#           else:
#               return sizeTracker    

# ====================================
# Code

def numConverter (line):
    # removes everything pass the last space
    newLine = line[:line.rfind(" ")]
    newLine = int(newLine)
    return newLine

# a function that:
#   takes in a '$ ls' line and the original log
#   returns sizeTracker if the dir size is <= 100000
#   returns 0 if dir size is > 100000


def sizeChecker(lineNumber, content):

    sizeTracker = 0
    dirTracker = 0

    for line in range((lineNumber+1), len(content)):
        if ord(content[line][0]) in range(48, 58):
            sizeTracker += numConverter(content[line])
        if content[line][0] == 'd':
            dirTracker += 1
        # failsafe incase the last line is not a $
        if content[line][0] == '$' or line == len(content):
            endLine = line
            break

    if dirTracker > 0:
        for line in range((endLine), len(content)):
            if ord(content[line][0]) in range(48, 58):
                sizeTracker += numConverter(content[line])
            if content[line][0] == 'd':
                dirTracker += 1
            if content[line] == '$ cd ..\n':
                dirTracker -= 1
            if dirTracker == 0:
                break
    
    if sizeTracker > 100000:
        return 0
    else:
        return sizeTracker

with open ('DIRLog.txt') as file:

    totalSize = 0

    content = file.readlines()
    for line in range(len(content)):
        if content[line] == '$ ls\n':
            totalSize += sizeChecker(line,content)
    print(totalSize)