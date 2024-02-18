#find the largest prime factor of the magic number

import math

small_factors = []

magic = 600851475143
lim = int(math.sqrt(magic))

for i in range(2, lim, 1):
    if magic % i == 0: 
        small_factors.append(i)
        magic /= i

print(small_factors)

for j in small_factors:
    for k in range(2, int(math.sqrt(j))):
        if j % k == 0:
            small_factors.remove(j)

print(small_factors)
