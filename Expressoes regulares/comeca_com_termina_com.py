import re


# Meta caracteres: 
# ^ --> comeca com
# $ --> Termina com
# [^a-z] --> Qualquer letra que nao sje entre A a Z

cpf = 'a 147.852.963-12 a'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
