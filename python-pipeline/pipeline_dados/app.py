import json
import csv

#### EXTRAÇÃO DOS DADOS ####

# Leitura dos dados em json
path_json = './data_raw/dados_empresaA.json'

with open(path_json, 'r') as file:
    #print ( file.readline() ) -> Só vai imprimir a primeira linha
    dados_json = json.load(file)

print(type(dados_json))

print("Imprimindo a segunda linha")
print("--------------------------")
print(dados_json[1])
print("Quantidade de estoque da primeira linha:"+str(dados_json[1]['Quantidade em Estoque']))

print("Imprimindo a Décima primeira linha")
print("----------------------------------")

print(dados_json[10])

# Leitura dos dados em csv
path_csv = './data_raw/dados_empresaB.csv'

dados_csv = []
with open(path_csv, 'r') as file:
    #dados_csv = file.readlines()
    spamreader = csv.reader(file, delimiter=',') # Retorna uma lista
    for row in spamreader:
        dados_csv.append(row)

print("Imprimindo a primeira linha")
print("---------------------------")
print(dados_csv[0])

print("Imprimindo o primeiro valor da primeira linha")
print("---------------------------------------------")
print(dados_csv[0][0])

# Leitura dos dados em csv
path_csv = './data_raw/dados_empresaB.csv'

dados_csv = []
with open(path_csv, 'r', encoding='utf-8') as file:
    spamreader = csv.DictReader(file, delimiter=',') # Retorna um dicionário
    for row in spamreader:
        dados_csv.append(row)

print("Imprimindo a primeira linha")
print("---------------------------")
print(dados_csv[0])


#### TRANSFORMAÇÃO DOS DADOS #####

print()
print()
print("Exibindo as chaves, que são os nomes das colunas")
nome_colunas_json = list(dados_json[0].keys()) # Exibindo os nomes das colunas em forma de lista
print("Empresa A ( JSON ): {} Colunas. A Saber: {} ".format(len(nome_colunas_json), str(nome_colunas_json)))
# print(nome_colunas_json.values()) # Obter todos os valores
# print(nome_colunas_json.items()) # Retorna uma visão dos pares chave-valor do dicionário

nome_colunas_csv = list(dados_csv[0].keys()) # Exibindo os nomes das colunas em forma de lista
print("Empresa A ( JSON ): {} Colunas. A Saber: {} ".format(len(nome_colunas_csv), str(nome_colunas_csv)))

# Mapeamento das chaves do dicionário. Consiste em um dicionário onde queremos fazer um "de: para"
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
    }

print()
print("Exibindo o mapeamento das chaves")
print(key_mapping)

# Atualização dos nomes
new_dados_csv = []

# old_dict -> Dicionário antigo contendo os dados com os nomes das colunas que não queremos
for old_dict in dados_csv:
    dict_temp = {}
    for old_key, value in old_dict.items():
        dict_temp[key_mapping[old_key]] = value
    new_dados_csv.append(dict_temp)

print(new_dados_csv[0])

# Concatenação das duas listas JSON e CSV
combined_list = []
combined_list.extend(dados_json)
combined_list.extend(new_dados_csv)

print(len(combined_list))

#### SALVANDO OS DADOS #####
path_dados_combinados = './data_processed/dados_combinados.csv'

nomes_colunas = list(combined_list[0].keys())

with open(path_dados_combinados, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=nomes_colunas)
    writer.writeheader()

    for row in combined_list:
        writer.writerow(row)