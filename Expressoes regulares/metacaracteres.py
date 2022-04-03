# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'Joao|Maria|ad..tos', texto))
print(re.findall(r'[jJ]oao|[mM]aria|ad..tos', texto))
print(re.findall(r'[a-z]oao', texto))  # Qualquer letra de A ate Z
print(re.findall(r'Joao', texto, flags=re.I))  #Para deixar de ser cap sensitive