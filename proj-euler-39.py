# For p the perimeter of a right triangle, for which value of p at most some magic number (1000, for PE) is the number of such possible triangles with integer side lengths maximized?

magic = 1001
squares = []
for i in range(5, 501):
    squares.append(i*i)

perimeters = []
legses = []
for i in range(3, 501):
    for j in range(4, 501):
        squaresum = i*i + j*j
        if squaresum in squares:
            temp = squares.index(squaresum) + 5
            templegs = [i, j]
            templegs = sorted(templegs)
            tempperimeter = i + j + temp
            if templegs not in legses and tempperimeter < magic:
                #print('right triangle:', templegs, temp)
                perimeters.append(tempperimeter)
                legses.append(templegs)

perimeters = sorted(perimeters)
length = len(perimeters)
modalperimeter = -1
modecardinality = 1
currentmodalcardinality = 1

for i in range(1, length):
    if perimeters[i] == perimeters[i-1]:
        currentmodalcardinality += 1
    elif currentmodalcardinality > modecardinality:
        modecardinality = currentmodalcardinality
        modalperimeter = perimeters[i-1]
        #print('longest run so far:', modecardinality, modalperimeter)
    else:
        currentmodalcardinality = 1

print('the modal perimeter is', modalperimeter)