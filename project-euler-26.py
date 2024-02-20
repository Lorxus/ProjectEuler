# determines the number d < magic such that the decimal expansion of 1/d has the longest recurring part
# for PE, magic = 1000

def recurrentlength(n):
    while n % 2 == 0 or n % 5 == 0:  # strip all the 2s and 5s
        if n % 2 == 0:
            n /= 2
        if n % 5 == 0:
            n /= 5
        n = int(n)
    
    # shortest repdigit 9s that the remnant divides into
    if n == 1 :
        return 0
    count = 1
    repnines = 9
    
    while repnines % n != 0:  # this looks horrifying but as before I promise you this works out
        count += 1
        repnines *= 10
        repnines += 9
    
    return(count)

maxrecurrent = -1
bestdivisor = -1
for i in range(1, 1001):
    temp = recurrentlength(i)
    if temp > maxrecurrent:
        maxrecurrent = temp
        bestdivisor = i

print(bestdivisor, maxrecurrent)