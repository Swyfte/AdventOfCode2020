"Split line into before and after colon"
"Create RegEx from first half"
"Apply RegEx to second half"
"If valid, incriment counter."

import re

miniumum = 0
wholePattern = re.compile('^[0-9]+-[0-9]+\\s[a-zA-Z]:\\s[a-zA-Z]+$')
linelist = []
with open("input.txt") as f:
    for line in f:
        match = re.search('^[0-9]+', line)
        miniumum = int(match.expand())
        
