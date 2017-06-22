import re
password = input()
if len(password)<=5 or len(password)>=16:
    print('Password length must be between 5 and 16')
else:
    strength = 1
    digitChkRegEx = re.compile(r'[0-9]')
    match = digitChkRegEx.search(password)
    if (match!= None):
        strength = strength + 1
    upperCaseChkRegEx = re.compile(r'[A-Z]')
    match = upperCaseChkRegEx.search(password)
    if (match!=None):
        strength = strength + 1
    lowerCaseChkRegEx = re.compile(r'[a-z]')
    match = lowerCaseChkRegEx.search(password)
    if (match!=None):
        strength = strength + 1

    if (strength == 2 or strength == 1):
        str_strength = 'weak'
    if (strength == 3):
        str_strength = 'medium'
    if (strength == 4):
        str_strength = 'strong'

    print('Your password is '+ str_strength)
