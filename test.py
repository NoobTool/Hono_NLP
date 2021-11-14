import re


word = "94% cgpa"

print(re.fullmatch("[0-9]+\.*[0-9]* *%* *[A-z]*",word))