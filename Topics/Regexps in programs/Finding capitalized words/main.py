import re

string = input()
# your code here
template_1 = r'[A-Z]\w+'
template_2 = r'\d+'
match_1 = re.findall(template_1, string)
match_2 = re.findall(template_2, string)
print(f"Capitalized words: {', '.join(match_1)}")
print(f"Digits: {', '.join(match_2)}")

