#find the lcm of the numbers from 1 to n>3
import math

magic = 20;

primes = [2, 3]

for i in range(4, magic + 1):
    for j in range(2, int(math.sqrt(i))+2):
        if i % j == 0:
            break
        elif j == int(math.sqrt(i))+1:
            primes.append(i)


powers = primes.copy()

for p in primes:
    q = p*p
    while q <= magic:
        if q * p > magic:
            powers.append(q)
            powers.remove(p)
        q *= p

prod = 1

for k in powers:
    prod *= k 

print(prod)