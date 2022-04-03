###ATALHOS###
# \w -> [a-zA-Z0-9á- ú_]
# \W -> negacao de \w
# \d -> Digitos de 0 a 9
# \D -> negacao de \d
# \s -> [\r\n\f\t]  Espacos em branco
# \S -> Tudo que nao eh espaco
# \b -> Encontrara a borda
# \B -> Algo que nao eh a borda

###FLAGS###
#re.A - Achar ASCII
#re.I - Ignore case
#re.M - Multiline -> ^ $
#re.S - Dotall -> Reconhece quebra de linhas 
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''
print(re.findall(r'[a-zA-Z]+', texto))
print(re.findall(r'[a-zA-Z0-9]+', texto))

#Os dois sao iguais
print(re.findall(r'[a-zA-Z0-9á- ú]+', texto))
print(re.findall(r'\w+', texto)) 

 #Pega apenas a tabela ASCII
print(re.findall(r'\w+', texto, flags=re.A)) 


print(re.findall(r'\bflo\w+', texto, flags=re.I))  