"Split line into before and after colon"
"Create RegEx from first half"
"Apply RegEx to second half"
"If valid, incriment counter."

linelist = []
with open("input.txt") as f:
    for line in f:
        minimum = 0
        maximum = 0
        numString = ''
        charactermatch = ''
        for char in line:
            if (char != '-') & (minimum == 0):
                numString += char
            elif char == '-':
                minimum = int(numString)
                numString = ''
            