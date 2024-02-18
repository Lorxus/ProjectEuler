#find the nth prime

n = 10001
primes = [2, 3]
count = 4

while len(primes) < n:
    for i in range(2, int(count**0.5) + 1):
        if count % i == 0:
            count += 1
            break 
        elif i == int(count**0.5):
            primes.append(count)
            count += 1

print(primes[-1])
