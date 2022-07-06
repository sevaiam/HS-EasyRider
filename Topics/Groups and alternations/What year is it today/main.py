import re


# put your regex in the variable template
template = r"(\d\d?)[\/\.](\d\d?)[\/\.](\d{4})"
string = input()
# compare the string and the template
match = re.match(template, string)
if match:
    print(match.group(3))
else:
    print(match)
