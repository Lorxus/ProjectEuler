#sum the digits of n factorial

n = 100
prod = 1
digits = []
sum = 0

for i in range(1, n+1):
    prod = prod * i

print(prod)

while prod > 0:
    digits.append(prod % 10)
    prod = prod // 10

for j in digits:
    sum += j

print(sum)
