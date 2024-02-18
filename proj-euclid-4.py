#find the largest palindrome that factors as the product of two 3-digit numbers

i = 999
j = 0
prod = 1
maxprod = 2

while i > 500:
    j = i
    while j > 500:
        prod = i * j 
        string = str(prod)
        if(string==string[::-1] and prod > maxprod):
            maxprod = prod
            j -= 1 
            break 
        j -= 1
    i -= 1
    
print(maxprod)
    

