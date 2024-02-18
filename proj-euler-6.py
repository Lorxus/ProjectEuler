#compute the difference between sum(n)^2 and sum(n^2)

n = 100

squared_sum = (n*(n+1)/2)**2

sum_of_squares = n*(n+1)*(2*n+1)/6

print(squared_sum - sum_of_squares)
