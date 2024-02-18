#how many different numbers are there in {a^b | 2 <= a, b <= 100}?

powers = {4} #this will be a repeat

for i in range(2, 101):
    for j in range(2, 101):
        pow = i**j
        powers.add(pow)

print(len(powers))