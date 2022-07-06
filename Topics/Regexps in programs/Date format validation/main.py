import re

string = input()
# your code here
template = r'^(\d\d)\/(\d\d)\/(\d{4})$'
match = re.match(template, string)
if match and (0 < int(match.group(1)) <= 31 or 0 < int(match.group(2)) <= 12):
    print(True)
else:
    print(False)
