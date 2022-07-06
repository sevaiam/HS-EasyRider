import re

password = input()
# your code here
template = r'^\w{6,15}$'
match = re.match(template, password, flags=re.A)
if match:
    print('Thank you!')
else:
    print('Error!')
