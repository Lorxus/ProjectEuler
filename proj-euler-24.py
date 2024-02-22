import itertools

# def beforeness(m, n):
#     length = len(m)
#     if m == n:
#         return False
#     for i in range(length):
#         if m[i] > n[i]:
#             return False
    
#     return True

ten = []
for i in range(10):
    ten.append(i)

permutedten = list(itertools.permutations(ten))
print(permutedten[999999])