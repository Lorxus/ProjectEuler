# The UK's currency has eight coins we care about: 1p, 2p, 5p, 10p, 20p, 50p, 100p, and 200p.
# This program calculates the number of ways of making change summing to a magic total - 200p, in the case of PE.

coinvalues = [1, 2, 5, 10, 20, 50, 100, 200]
magic = 200

dpcoinslist = [1] + [0] * magic

for coin in coinvalues:
    for i in range(coin, magic + 1):
        dpcoinslist[i] += dpcoinslist[i - coin]

print(dpcoinslist[200])

