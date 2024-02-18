#add together all even fibonnaci numbers at most 4m

fibs = []

fib_new = 1 
fib_last = 0

while fib_new <= 4000000:
    fibs.append(fib_new)
    fib_last += fib_new
    temp = fib_new
    fib_new = fib_last
    fib_last = temp
    
#print(fibs[5])
    
total = 0 
    
for i in fibs:
    if i%2 == 0:
        total += i     
        
print(total)
