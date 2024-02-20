# calculates the sum of all numbers equal to the sum of their own digits' factorials
# notably: these are at most 7-digit, since f(999,999) = 2,177,280 but f(9,999,999) = 2,540,160

import random as r

def factorial(n):  # we only need this to work for 0 through 9
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 24
    elif n == 5:
        return 120
    elif n == 6:
        return 720
    elif n == 7:
        return 5040
    elif n == 8:
        return 40320
    elif n == 9:
        return 362880
    else: return -1 

def numbertofacts(n):
    factsum = 0
    numberstub = n
    
    while numberstub > 0:
        d = numberstub % 10
        numberstub -= d
        numberstub /= 10
        numberstub = int(numberstub)
        factsum += factorial(d)
    
    #print(digits, factsum)
    return factsum

def islikefact(n):
    return numbertofacts(n) == n

FactMatches = []

for i in range(10, 10000000):  # "as 1! and 2! are not sums they are not included."
    if r.random() < 0.0001:
        print('Now testing:', i)

    if islikefact(i):
        FactMatches.append(i)
        print(i, 'is a match!')  # 145, 40585, 40730

print('the sum is:', sum(FactMatches))