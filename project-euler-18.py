# calculates the maximal sum traversing the triangle that PE provided top to bottom.

triangle = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 25, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
# as provided by PE. any other triangular 2d array of numbers would do.

def maxsumatloc(m, n):
    #print('checking case:', m, n)
    total = 0
    if m == 0 and n == 0:
        return triangle[0][0]  # base case
    elif n == 0:
        for i in range(m):
            total += triangle[i][0]  # case: left edge
        return total + triangle[m][n]
    elif m == n:
        for i in range(m):
            total += triangle[i][i]  # case: right edge
        return total + triangle[m][n]
    else:
        return triangle[m][n] + max(maxsumatloc(m-1, n-1), maxsumatloc(m-1, n))  # whichever is larger, plus the cell of interest

# print(maxsumatloc(0, 0))
# print(maxsumatloc(2, 0))
# print(maxsumatloc(3, 3))
# print(maxsumatloc(1, 1))

bestbottomtot = -1
length = len(triangle)

for i in range(length):
    if maxsumatloc(length - 1, i) > bestbottomtot:
        bestbottomtot = maxsumatloc(length - 1, i)

print(bestbottomtot)