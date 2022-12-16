# a function that:
# takes in 4 characters
# checks if there's a duplicate
# returns true if there is
def dupChecker (a,b,c,d):
    seq = a+b+c+d
    dupTF = False
    # for each letter in seq, check if it can be found again in the seq
    for letter in range(4):
        # use replace()
        # if there's no dup, replace would remove only 1 letter
        # if there's a dup, replce would remove 2 or more
        #   therefore shortening the len(string) differently
        compSeq = seq.replace(seq[letter],'')
        # if replace() only removed 1 letter, len(compSeq) should == 3
        if len(compSeq) < 3:
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
        if data < len(content[0])-3:
            isDup = dupChecker(content[0][data],content[0][data+1], content[0][data+2], content[0][data+3])
            if not isDup:
                # +3 for the position of the last char, +1 for elven index (start@1)
                print(data+3+1)
                break
