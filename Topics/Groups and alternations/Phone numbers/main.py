import re

string = input()
# your code here
template = r"\+(\d)[ -]?(\d{3})[ -]?([\d -]+)"
match = re.match(template, string)
if match:
    print(f"Full number: {match.group()}")
    print(f"Country code: {match.group(1)}")
    print(f"Area code: {match.group(2)}")
    print(f"Number: {match.group(3)}")
else:
    print('No match')
