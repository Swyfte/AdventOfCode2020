"Split line into before and after colon"
"Create RegEx from first half"
"Apply RegEx to second half"
"If valid, incriment counter."

import re

charMatch = re.compile('[a-z]|[A-Z]')

linelist = []
with open("passwords.txt") as f:
    for line in f:
        minimum = 0
        maximum = 0
        numString = ''
        charactermatch = ''
        password = ''
        isPassword = False
        for char in line:
            if (char != '-') & (minimum == 0):
                numString += char
            elif char == '-':
                minimum = int(numString)
                numString = ''

            elif (char != ' ') & (maximum == 0):
                numString += char
            elif (char == ' ') & (maximum == 0):
                maximum = int(numString)
                numString = ''

            elif charactermatch == '':
                if re.search(charMatch, char):
                    charactermatch = char
            
            elif (char == ' ') & (charactermatch != ''):
                isPassword = True
            
            elif (isPassword):
                password += char
        print(minimum)
        print(maximum)
        print(charactermatch)
        print(password)