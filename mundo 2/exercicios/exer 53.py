import re


frase = str(input('Me diga uma frase.\n'))
pattern = r'\s+$'
s1 = re.sub(pattern, '', frase)
print(s1)