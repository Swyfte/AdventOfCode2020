"Open input"
"Read line"
"Split line into before and after colon"
"Create RegEx from first half"
"Apply RegEx to second half"
"If valid, incriment counter."

linelist = []
with open("input.txt") as f:
    for line in f:
        linelist.append(int(line))