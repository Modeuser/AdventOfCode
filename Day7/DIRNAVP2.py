def numConverter (line):
    # removes everything pass the last space
    newLine = line[:line.rfind(" ")]
    newLine = int(newLine)
    return newLine


with open ('DIRLog.txt') as file:

    totalSize = 0
    content = file.readlines()
    for line in range(len(content)):
        if ord(content[line][0]) in range(48,58):
            totalSize += numConverter(content[line])
    freeSpace = 70000000 - totalSize
    needSpace = 30000000 - freeSpace
    print(needSpace)
#   we need to remove a directory that is larger than 8748071