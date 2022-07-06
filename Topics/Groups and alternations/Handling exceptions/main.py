import re


# put your regex in the variable template
template = "(Value|Name|Type)Error"
string = input()
# compare the string and the template
match = re.match(template, string)
if match:
    print(match.group(1))
else:
    print(match)
