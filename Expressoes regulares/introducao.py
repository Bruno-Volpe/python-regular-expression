import re

# findall search sub 
# compile

sring = 'Esse eh um teste de expressoes regulares'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string, count=1))

rexexp = re.compile(r'teste')
rexexp.search(string)
rexexp.findall(string)
rexexp.sub('ABCD', string, count=1)