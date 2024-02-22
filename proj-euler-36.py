# some numbers are palindromes in base 10, like 1331. others are palindromes in base 2, like 17 (10001).
# this program computes the sum of all positive integers less than a magic value (PE = 1000000) which are both.

magic = 1000000

def striptodigitsten(n):
    digits = []
    numberstub = n
    
    while numberstub > 0:
        d = numberstub % 10
        digits.insert(0, d)
        numberstub -= d
        numberstub /= 10
        numberstub = int(numberstub)
    
    return digits
        
def striptodigitstwo(n):
    digits = []
    numberstub = n
    
    while numberstub > 0:
        d = numberstub % 2
        digits.insert(0, d)
        numberstub -= d
        numberstub /= 2
        numberstub = int(numberstub)
    return digits
        
def ispalindrome(l):
    if type(l) != list:
        return False
    else:
        return l == l[::-1]
    
doublepalindromes = []
for i in range(1, magic):
    binarydigits = striptodigitstwo(i)
    decimaldigits = striptodigitsten(i)
    #print(binarydigits, decimaldigits)
    if ispalindrome(binarydigits) and ispalindrome(decimaldigits):
        doublepalindromes.append(i)
        print('double palindrome found:', i)

print(doublepalindromes)
print(sum(doublepalindromes))