# Some pairs of two-digit integers are like 19 and 95:
# 19/95 = 1/5 and we "cancel" the 9s.
# This program finds all such pairs, not counting trivial examples like 20/30.

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

candidatepairs = []

for i in range(10, 100):
    mydigits = striptodigitsten(i)
    denomtens = mydigits[1]
    tensplace = 10 * denomtens
    if tensplace == 0:
        continue
    for j in range(tensplace, tensplace + 10):
        if not (i % 10 == 0 and j % 10 == 0) and i != j:
            candidatepairs.append([i, j])

# print(len(candidatepairs))
# print(candidatepairs)
realpair = []

for pair in candidatepairs:
    numerdigit = striptodigitsten(pair[0])[0]
    denomdigit = striptodigitsten(pair[1])[1]
    if denomdigit == 0:
        continue
    ratio = numerdigit/denomdigit
    if pair[0]/pair[1] == ratio:
        realpair.append(pair)

print(realpair)
nproduct = 1
dproduct = 1
for pair in realpair:
    numerdigit = striptodigitsten(pair[0])[0]
    denomdigit = striptodigitsten(pair[1])[1]
    nproduct *= numerdigit
    dproduct *= denomdigit

print(nproduct, dproduct)