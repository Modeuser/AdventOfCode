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
    return stackLog

# a function that:
# takes in the stackLog
# takes in the instructions
# sort the stackLog based on the instructions
# returns the new stackLog
def stackSorter (oldLog, instruct):
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
    print(moveAmount, fromStack, toStack)

    # find the charaters between fromStack and fromStack+1
    #   i.e oldLog.find(fromStack) and find(str(int(fromStack)+1)
    # copy the values to a variable
    #   movingCrates = oldLog[fromStack(position)+1 : end(position)]
    # 


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