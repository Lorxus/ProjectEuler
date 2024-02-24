# (28433 * 2^7830457) + 1 is prime
# this program calculates its last 10 digits

primestub = 28433
exp = 7830457

for i in range(exp):
    primestub *= 2
    if primestub > 10000000000:
        primestub %= 10000000000

primestub += 1

print(len(str(primestub)))
print(primestub)