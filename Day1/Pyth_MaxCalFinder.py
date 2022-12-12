# personName = "john"
# personAge = "35"

# print("there was a man named " + personName + ",")

# phrase = "Unga Bunga"
# print(phrase.upper().isupper()) converts to upper case, then check if string is now upper case
# print(len(phrase)) gets the length of the string
# print(phrase[0])

# numberGrid = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 1, 2, 3],
# ]

# for row in numberGrid:
#     for col in row:
#         print(col)

# try:
#     value = 10/0
#     number = int(input("enter a number"))
#     print(number)
# except ZeroDivisionError:
#     print("divided by zero")
# except ValueError:
#     print("invalid input")

calLogFile = open("CalLog.txt", "r")
# print(calLogFile.readable()) check if readable

print(len(calLogFile.readlines()))

# print(calLogFile.readlines()[1])

calLogFile.close()