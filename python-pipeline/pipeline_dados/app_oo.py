import json
import csv

##### FUNÇÕES DE LEITURA DOS ARQUIVOS CSV E JSON
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r', encoding='utf-8') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r', encoding='utf-8') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)            
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados = []

    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
        
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
        
    return dados

# para obter as chaves do dicionário, converter para uma lista e retornar
def get_columns(dados):
    return list(dados[0].keys())

# Renomeia as colunas
def rename_columns(dados, key_mapping):
    new_dados_csv = []
    
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
            
    return new_dados_csv

# Recebe novos dados e retorna o tamanho da lista
def size_data(dados):
    return len(dados)

# Juntando os dados de ambas as listas
def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def transformando_dados_tabela(dados, nomes_colunas):
    
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    
    return dados_combinados_tabela

# Salvando os dados
def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)



######################## EXTRAÇÃO DOS DADOS #########################

# Leitura dos dados em json
path_json = './data_raw/dados_empresaA.json'

dados_json = leitura_json(path_json)
print(dados_json[0])

# Leitura dos dados em csv
path_csv = './data_raw/dados_empresaB.csv'

dados_csv = leitura_csv(path_csv)
print(dados_json[0])

# Arquivos json
dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)

print(f"Nome colunas dados json: {nome_colunas_json}")
print(f"Tamanho dos dados json: {tamanho_dados_json}")

# Arquivos csv
dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(nome_colunas_csv)
print(tamanho_dados_csv)


nome_colunas_csv = list(dados_csv[0].keys())
print(nome_colunas_csv)

dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)

print()
print(f"Nome colunas dados json: {nome_colunas_json}")
print()

dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)

#### TRANSFORMAÇÃO DOS DADOS ####

"""
key_mapping é muito importante e precisa ser incluída
corretamente no script, pois é o momento em que interagimos
com o time de BI e entendemos quais colunas eles precisam.
"""
print("KEY MAPPING")
key_mapping = {'Nome do Item': 'Nome do Produto',
                            'Classificação do Produto': 'Categoria do Produto',
                            'Valor em Reais (R$)': 'Preço do Produto (R$)',
                            'Quantidade em Estoque': 'Quantidade em Estoque',
                            'Nome da Loja': 'Filial',
                            'Data da Venda': 'Data da Venda'}
dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)

dados_fusao = join(dados_json, dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print(nome_colunas_fusao)
print(tamanho_dados_fusao)

############### SALVANDO DADOS ######################
dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)
path_dados_combinados = 'data_processed/dados_combinados.csv'
salvando_dados(dados_fusao_tabela, path_dados_combinados)
print(path_dados_combinados)