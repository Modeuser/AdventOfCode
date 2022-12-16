# a function that:
# takes in a seq
# check if any letter in the seq is dup
# returns true if dup else false
def dup14Checker(seq):
    dupTF = False
    for letter in range(14):
        # same method as part 1
        # if there is a dup, then replace would shorten the len(seq) more than 1
        compSeq = seq.replace(seq[letter],'')
        if len(compSeq) < 13:
            dupTF = True
            break
        else:
            dupTF = False
    return dupTF

# main function
with open ('SignalLog.txt') as file:
    content = file.readlines()
    # a for loop that sends 4 characters in sequence to dupChecker
    for data in range(len(content[0])):
        # check if it and the next 3 letters are in range of the index
        if data < len(content[0])-13:
            isDup = dup14Checker(content[0][data:data+14])

            if not isDup:
                # +13 for the position of the last char, +1 for elven index (start@1)
                print(data+13+1,content[0][data:data+14])
                break
