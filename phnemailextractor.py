import pyperclip
import re
text = str(pyperclip.paste())
phoneNumberRegEx = re.compile(r'''(
                                (\+\d{2}\ )?        # +91 as country code
                                (\d{10}))''',re.VERBOSE)

emailRegEx = re.compile(r'''(
                            [a-zA-Z0-9.]+   # username
                            @               # @ symbol
                            [a-zA-Z0-9.-]+  # domain name
                            (\.[a-zA-Z]{2,4})
                            )''',re.VERBOSE)

matches = []
for groups in phoneNumberRegEx.findall(text):
    if (groups[1]!=' '):
        phoneNum = ''.join([groups[1],groups[2]])
    else:
        phoneNum = groups[2]
    matches.append(phoneNum)

for groups in emailRegEx.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found!')
