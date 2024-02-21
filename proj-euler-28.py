# take a spiral of numbers, start in the center with 1, move right to 2, and then always proceed clockwise or right.
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# example of a 5 x 5 such spiral. if we were to extend it, 26 is to the right of 25, and 27 is below 26.
# we want to calculate the sum of the diagonal elements of such a spiral
# in the case of the 5 x 5 above, this would be 101.
# we want the case of 1001 x 1001.

magic = 1001  # must always be odd
currentnumber = 1
runningtotal = 1
numspins = int((magic - 1)/2)

for i in range(1, numspins + 1):
    for j in range(4):
        currentnumber += (2 * i)  # this is always the pattern for getting to the next diagonal number - increase by 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6...
        runningtotal += currentnumber

print(runningtotal)
