# 0.0.0.0 255.255.255.255 -- IP
# 025.258.963-10 -- CPF

import re
cpf = '025.258.963-10'
cpf_rex_exp = re.compile(r'^\d{3}.\d{3}.\d{3}-\d{2}$')
print(cpf_rex_exp.search(cpf))

ip_reg_exp = re.compile(r"""
    ^
    (?:
        (?:
            25[0-9]|
            2[0-4][0-9]|
            1[0-9]{2}|
            [1-9][0-9]|
            [0-9]
        ) 
        \.?
    ){4}
    \b
    $
""")

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'