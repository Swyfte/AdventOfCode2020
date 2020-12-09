slope = []
with open("input.txt") as f:
    for line in f:
        charray = []
        for char in line:
            if char != '\n':
                charray.append(char)
        slope.append(charray)

X, Y, startY, startX, treesFound = [0,0,0,0,0]
foundEnd = False
lineLength = len(slope[0])
slopeHeight = len(slope)
while not foundEnd:
    X += 3
    if (lineLength - (X+1)) < 0:
        X = 0 + (X - (lineLength))
    Y += 1
    if Y > (slopeHeight - 1):
        foundEnd = True
    elif slope[Y][X] == '#':
        treesFound += 1

print(treesFound)

a = 156
b = 79
c = 85
d = 82
e = 41
print(a*b*c*d*e)