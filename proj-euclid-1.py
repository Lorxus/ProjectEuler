#add together all multiples of 3 or 5  

#there is a clever PIE bash for this but loopwise seems better pedagogically
total = 0 

for i in range(1000):
    if (i%3 == 0) or (i%5 == 0): 
        total += i
    

print(total)