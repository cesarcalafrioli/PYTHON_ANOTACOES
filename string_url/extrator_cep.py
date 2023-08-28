endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression -- RegEx

# 5 dígitos + hifen ( opcional ) + 3 dígitos

# {5} - Aparece 5 vezes
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")# Cada lista é um dígito do CEP
busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)

