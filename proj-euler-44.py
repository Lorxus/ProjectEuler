# A pentagonal number is one of the form n(3n-1)/2
# This program finds the pair of pentagonal numbers whose sum and difference are both pentagonal
# and for which their difference is minimal
# It also finds their difference

pentagonallist = []

for i in range(1, 3000):
    temp = (i * ((3 * i) - 1)) / 2
    temp = int(temp)
    pentagonallist.append(temp)

# pentagonallist.sort()
plength = len(pentagonallist)

def ispentagonal(n):
    return n in pentagonallist

mindifference = float('inf')

for j in range(plength):
    for k in range(j):  # only loop over smaller indices so that the difference is always positive and we still check everything
        tempsum = pentagonallist[j] + pentagonallist[k]
        tempdiff = pentagonallist[j] - pentagonallist[k]
        if tempdiff > mindifference:
            continue
        if ispentagonal(tempsum) and ispentagonal(tempdiff) and mindifference > tempdiff:
            mindifference = tempdiff
            print('new min difference pair:', j+1, pentagonallist[j], k+1, pentagonallist[k], tempdiff)

print(mindifference)