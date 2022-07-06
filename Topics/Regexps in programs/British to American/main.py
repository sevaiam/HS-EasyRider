import re

string = input()
# your code here
match = re.sub('ou', 'o', string)
print(match)
