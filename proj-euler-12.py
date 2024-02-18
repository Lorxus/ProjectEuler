#find the first triangular number with >max factors

max = 500
factors = 0
i = 0

while factors < max:
    factors = 0
    i += 1
    n = int(i*(i+1)/2) 
    for j in range(1, int(n**0.5)+1):
        if n%j == 0:
            factors += 2 #one below sqrt(n), one above it 

print(factors)
print(i)
print(n)
