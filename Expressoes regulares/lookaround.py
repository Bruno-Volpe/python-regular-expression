import re

texto = '''
........................................
'''

# Positive lookahead
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+\.)\s+\w+\s+(?=active)', texto, flag=))

# Negative lookahead
print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+\.)\s+\w+\s+(?!active)', texto, flag=))
print(re.findall(r'(?=.*[^in]active).+', texto, flag=re.S))


# Positive lookbehind
print(re.findall(r'\w+(?<=online)\s+(\d+\.\d+\.\d+\.\d+\.)\s+\w+\s+\w+)', texto, flag=))

# Negative lookbehind
print(re.findall(r'\w+(?<!online)\s+(\d+\.\d+\.\d+\.\d+\.)\s+\w+\s+\w+)', texto, flag=))
