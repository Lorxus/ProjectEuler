# calculates the sum of all numbers equal to the sum of their own digits' fifth powers
# notably: these are at most 6-digit, since f(99999) = 295245 but f(999999) = 354294

def numbertofifths(n):
    digits = [0] * 6
    
    if n < 10:
        digits[5] = n
    elif n < 100:
        digits[5] = n % 10
        digits[4] = int((n - digits[5])/10)
    elif n < 1000:
        digits[5] = n % 10
        digits[4] = int((n - digits[5])/10) % 10
        digits[3] = int((n - digits[5] - (10 * digits[4]))/100)
    elif n < 10000:
        digits[5] = n % 10
        digits[4] = int((n - digits[5])/10) % 10
        digits[3] = int((n - digits[5] - (10 * digits[4]))/100) % 10
        digits[2] = int((n - digits[5] - (10 * digits[4]) - (100 * digits[3]))/1000)
    elif n < 100000:
        digits[5] = n % 10
        digits[4] = int((n - digits[5])/10) % 10
        digits[3] = int((n - digits[5] - (10 * digits[4]))/100) % 10
        digits[2] = int((n - digits[5] - (10 * digits[4]) - (100 * digits[3]))/1000) % 10
        digits[1] = int((n - digits[5] - (10 * digits[4]) - (100 * digits[3]) - (1000 * digits[2]))/10000)
    else:
        digits[5] = n % 10
        digits[4] = int((n - digits[5])/10) % 10
        digits[3] = int((n - digits[5] - (10 * digits[4]))/100) % 10
        digits[2] = int((n - digits[5] - (10 * digits[4]) - (100 * digits[3]))/1000) % 10
        digits[1] = int((n - digits[5] - (10 * digits[4]) - (100 * digits[3]) - (1000 * digits[2]))/10000) % 10
        digits[0] = int((n - digits[5] - (10 * digits[4]) - (100 * digits[3]) - (1000 * digits[2]) - (10000 * digits[1]))/100000)

    fifthsum = 0
    
    for d in digits:
        fifthsum += d ** 5
    
    print(digits)
    return fifthsum

def islikefifth(n):
    return numbertofifths(n) == n

FifthMatches = []

for i in range(10, 1000000):  # "as 1^5 is not a sum it is not included."
    if islikefifth(i):
        FifthMatches.append(i)
        print(i, 'is a match!')

print(sum(FifthMatches))