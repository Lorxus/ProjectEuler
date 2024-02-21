# calculates d_1 * d_10 * d_100 * d_1k * d_10k * d_100k of the decimal part of Champernowne's constant

def nthconcatdigit(n):
    n = int(n)
    if n < 1:
        return -1
    if n < 10:
        return n
    
    champ = '123456789'
    count = 9
    
    while len(champ) < n:
        count += 1
        countstr = str(count)
        champ += countstr
    
    thedigit = int(champ[n-1])
    
    return thedigit

print(nthconcatdigit(1), nthconcatdigit(10), nthconcatdigit(100), nthconcatdigit(1000), nthconcatdigit(10000), nthconcatdigit(100000))
print(nthconcatdigit(1) * nthconcatdigit(10) * nthconcatdigit(100) * nthconcatdigit(1000) * nthconcatdigit(10000) * nthconcatdigit(100000))
    
