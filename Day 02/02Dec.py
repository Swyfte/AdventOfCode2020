import re

charMatch = re.compile('[a-z]|[A-Z]')

validPasswords = 0
invalidPasswords = 0
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
            
            elif (isPassword) & (char != '\n'):
                password += char

        """count = 0
        for x in password:
            if x == charactermatch:
                count += 1
        if (count <= maximum) & (count >= minimum):
            validPasswords += 1
        else:
            invalidPasswords += 1"""
        if (len(password) >= maximum):
            if (password[minimum-1] == charactermatch) & (password[maximum-1] != charactermatch):
                validPasswords += 1
            elif (password[minimum-1] != charactermatch) & (password[maximum-1] == charactermatch):
                validPasswords += 1
            else:
                invalidPasswords += 1
        else:
            invalidPasswords += 1

            "This code does not work, it produces the wrong answer"
print(validPasswords)