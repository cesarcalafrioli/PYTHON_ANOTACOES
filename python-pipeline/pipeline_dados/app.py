import json
import csv

#### EXTRAÇÃO DOS DADOS ####

# Leitura dos dados em json
path_json = './data_raw/dados_empresaA.json'

with open(path_json, 'r') as file:
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

#nomes_colunas = list(combined_list[0].keys())

"""
get() -> método incorporado aos dicionários em Python para procurar um valor com base em uma chave específica,
sem o risco de gerar um erro se a chave não for encontrada.

Sintaxe( chave, valor_padrao_se_nao_for_encontrado )
"""
print("Data da venda: {}".format(combined_list[0].get('Data da Venda', 'Indisponível')))

nomes_colunas = list(combined_list[-1].keys()) # É possível utilizar o append na lista, mas do jeito que está podemos tomar algumas decisões e deixar o código mais dinâmico.
print(nomes_colunas)

"""Lista de dados combinados."""
dados_combinados_tabela = [nomes_colunas]

for row in combined_list:
    linha = []
    for coluna in nomes_colunas:
        linha.append(row.get(coluna, 'Indisponível'))
    dados_combinados_tabela.append(linha)

print(dados_combinados_tabela[0])
print(dados_combinados_tabela[1])
print(dados_combinados_tabela[-1])

#### SALVANDO OS DADOS #####
path_dados_combinados = './data_processed/dados_combinados.csv'

with open(path_dados_combinados, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(dados_combinados_tabela)

"""
Utilizar e conhecer bibliotecas é um processo muito importante para uma pessoa engenheira de dados, porque existem muitas bibliotecas que vão abstrair processos para nós.

Sabemos como funciona a escrita de um CSV, poderíamos até ir mais a fundo no Python e sair da biblioteca CSV para escrever manualmente dentro de um arquivo, mas isso geraria muito código,
que não é o objetivo do nosso projeto. Quem visse nosso código, encontraria uma grande quantidade de informação que não faz sentido para o projeto, no qual só queremos salvar os dados.

Poderíamos implementar algo que não fosse tão eficiente quanto a pessoa que desenvolveu a biblioteca. Portanto, há muitos pontos de vantagem em usar a biblioteca e o Python foi construído
em cima disso. Temos bibliotecas para fazer tudo o que nós podemos imaginar. Por que mostrar esse processo mais manual? Porque é muito importante entender como funciona. A implementação que
foi feita no CSV pode ser mais eficiente do que a nossa. Mas, para o quadro geral, nós podemos encontrar situações específicas que demandarão uma maneira diferente de salvar os dados em CSV,
por exemplo.

Ao longo desse projeto, vimos que nossos dados eram poucos e a memória RAM dava conta no processamento dentro do Jupyter Notebook. Mas e se tivéssemos muitos dados? A maneira de lidar e ler
esses dados seria diferente. Talvez precisássemos de outras bibliotecas.

Para nós entendermos que precisamos mudar de uma biblioteca para outra, nós precisamos entender como as coisas funcionam. Por isso, às vezes, fazemos um processo mais verboso, ou seja, com
mais código. Isso serve para nos ajudar a entender e solidificar esse fundamento, que é justamente a proposta desse projeto.

Estamos animados para ver se vamos conseguir salvar os dados dessa vez. Então, vamos rodar esse código. Ele não gerou nenhum erro e podemos abrir nosso CSV e entender se ele está do jeito que
esperávamos. Na lateral esquerda, acessaremos o explorador. Dentro da pasta "data_processed", acessaremos o arquivo dados_combinados.csv. Podemos fechar o explorador e analisar esse CSV.
"""