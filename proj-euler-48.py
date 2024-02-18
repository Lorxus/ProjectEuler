#find the last ten digits of sum(n^n)

max = 1000
sum_end = 0

for i in range(1, max+1):
    sum_end += (i**i % 10000000000)
    sum_end %= 10000000000

print(sum_end)
 
