#sum the digits of a large power of 2

magic = 2**1000

sum = 0 
rem = 0 

while magic > 0: 
    rem = magic % 10 
    sum += rem
    magic = magic//10
    rem = 0 

print(sum)
