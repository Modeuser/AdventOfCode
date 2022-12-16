# a function that:
# takes in the log in the file
# returns a string containing all the data sorted
def logToString (content):
    stackLog = ''
    for stacks in range(len(content[0])):
        # check if a value in row 9 is a number 1-9
        if ord(content[8][stacks]) in range(48,58):
            for crate in reversed(range(9)):
                # remove spaces
                if content[crate][stacks] != ' ':
                    stackLog += content[crate][stacks]
    # bad way to do this, but adding 10 to help with stackSorter
    stackLog += '10'
    return stackLog

# a function that:
# takes in the stackLog
# takes in the instructions
# sort the stackLog based on the instructions
# returns the new stackLog
def stackSorter (oldLog, instruct):

    # dumbass fix for when stack1 is empty and it identifies 10 as 1
    if len(oldLog) > 67:
        fixedLog = oldLog[:66]
        fixedLog += '0'
        oldLog = fixedLog

    fromPosition = instruct.find('from')
    toPosition = instruct.find('to')
    moveAmount = ''
    # finds the amount to move by
    for number in range(len(instruct)):
        # if it's a number
        if ord(instruct[number]) in range(48,58):
            # if the number is before 'from'...
            if number < fromPosition:
                moveAmount += instruct[number]
            elif number > fromPosition and number < toPosition:
                fromStack = instruct[number]
            elif number > toPosition:
                toStack = instruct[number]

    # print(moveAmount,fromStack,toStack)
    # Figure out how to move the crates around
        # find the charaters between fromStack and fromStack+1
        #   i.e oldLog.find(fromStack) and find(str(int(fromStack)+1)
        # copy the values to a variable
        #   movingCrates = oldLog[fromStack(position)+1 : end(position)]
        # get the moving crate by providing the stackID and stackID + 1
    movingCrates = oldLog[oldLog.find(fromStack):oldLog.find(str(int(fromStack)+1))]
    remainingCrates = movingCrates[:-int(moveAmount)]
    movedCrates = (movingCrates[len(remainingCrates):])
    # reverses the moved crates since they're moving one by ones
    movedCrates = movedCrates[::-1]

    # stores the modified log in a new log
    newLog = oldLog.replace(movingCrates,remainingCrates)

    # find the existingCrates
    existingCrates = newLog[newLog.find(toStack):newLog.find(str(int(toStack)+1))]
    # add the movedCrates to the existingCrates
    updatedCrates = existingCrates + movedCrates
    # stores the modified log in new log
    newLog = newLog.replace(existingCrates, updatedCrates)
    

    print(newLog)
    # return this newly sorted log
    return newLog


# a function that:
# takes in the stackLog
# makes note of which crate is on the top of each stack
# returns the crate IDs in a string

with open ('Cratelog.txt') as file:
    content = file.readlines()
    stackLog = logToString(content)
    # for each instruction send the instruction and the stackLog
    # to stackSorter, store the new log as stackLog
    for instruction in range (10,len(content)):
        stackLog = stackSorter(stackLog, content[instruction])
    for char in range(1,len(stackLog)-1):
        if ord(stackLog[char]) in range(48,58):
            print(stackLog[char-1])

# CRATES ARE MOVED ONE AT A TIME
# THIS MEANS THAT THE ORDER IS REVERSED!
# YOU DUMPASS