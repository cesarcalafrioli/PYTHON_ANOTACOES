url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print(url)

# Fatiamento de string
texto = 'abcde'

print(texto[0:1])

url2 = "bytebank.com/cambio?moedaOrigem=real"

url_base = url2[0:19]

print(url_base)

url_parametros = url2[20:36]

print(url_parametros)

texto = 'abcde'


# O método find é utilizado para encontrar o índice de um caractere dentro de uma string, como em url.find("?").
# Find é um método bem flexível e pode ser usado de diversas outras maneiras como mostra a documentação oficial
# do Python.
# str.find(sub[, start[, end]]) #  retorna -1 caso sub não seja encontrado em str.
texto.find('c')

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print("A base: ", url_base)

url_parametros = url[indice_interrogacao+1:36]
print("Parâmetros: ", url_parametros)

url_parametros = url[indice_interrogacao+1:]
print("Parâmetros: ", url_parametros)

print()
########### 
url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

print()
###########
texto = "Eu estudo na alura"
print(texto.find('E'))

print(texto.find('Eu'))

print(texto.find('Alura'))

print()
########### 
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

print()
###########
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

# Separa a base e os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)
tamanho_parametro = len(parametro_busca)
indice_valor = indice_parametro + tamanho_parametro + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

print()
############# Validando URL
url = " "

# "" e " " são diferentes. "" é espaço vazio e " " é um caractere
if url == "":
    raise ValueError("A URL Está Vazia")

url = " "
# Sanitizando uma URL
url = url.replace(" ", "")

if url == "":
    raise ValueError("A URL Está Vazia")

print()
################
