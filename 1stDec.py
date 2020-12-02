import os
linelist = []
with open("input.txt") as f:
    for line in f:
        linelist.append(int(line))

for x in linelist:
    for y in linelist:
        if x != y:
            for z in linelist:
                if (z != x) and (z != y):
                    if (x + y + z == 2020):
                        print (x * y * z)