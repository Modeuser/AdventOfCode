# go through the DIRLog
# 'cd' marks a directory
# perform DIR navigation for each unique DIR
# 'number' marks a file
# 

# could we use recursion?
# a function that:
# takes in DIRLog
# takes in line (i.e the line where a '$ cd DIR-ID was found)
# for each line in DIRLog[line of DIR-ID:end]:
#   if it's a 'dir DIRID':
#       re-call this function (line of $ cd DIRID, DIRLog)

#   this function should return the last nagivated line
#   before the back-recursion & sum of file size





# main function
# with open('DIRLog.txt') as file:

# for line in DIRLog
#   if line starts with '$ cd DIR-ID':
#       PH = DIRNAVSUM(line, DIRLog)
#       


#   DIRNAVSUM should return the sum of all the items for each respective DIR-ID
#   if PH <= 10000:
#       sumTracker += PH