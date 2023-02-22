import os
from datetime import datetime

# limpa a tela
os.system('cls')

"""### selecionando arquivos

# diretório corrente
caminho = os.curdir

# cria uma lista com as pastas e arquivos do diretório corrente
lista_diretorio = os.listdir(path=caminho)

# imprime só arquivos com final 'py'
for file in lista_diretorio:
    if file[-2:] == 'py':
        print(file, '\n')"""



"""### data de modificação do arquivo
# limpa a tela
os.system('cls')

# diretório corrente
caminho = os.curdir

# cria uma lista com as pastas e arquivos do diretório corrente
lista_diretorio = os.listdir(path=caminho)

# obtem a data de modificação do arquivo e monta tupla com data de modificação e nome do arquivo
lista_datas = []
for arquivo in lista_diretorio:
    data = os.path.getmtime(f'{caminho}/{arquivo}')
    lista_datas.append((data, arquivo))

# classifica lista de datas em ordem decrescente
lista_datas.sort(reverse=True)

# arquivo mais recente é a primeira tupla da lista
mais_recente = lista_datas[0]
data_mais_recente = mais_recente[0]
data_mais_recente = datetime.fromtimestamp(data_mais_recente).strftime('%d/%m/%Y %H:%M:%S')
arquivo_mais_recente = mais_recente[1]
print(f'Arquivo mais recente: {arquivo_mais_recente}, na data: {data_mais_recente}\n')
"""

### informações do arquivo

# diretório corrente
# caminho = os.curdir
caminho = os.getcwd()

# cria uma lista com as pastas e arquivos do diretório corrente
lista_diretorio = os.listdir(path=caminho)

# verifica quais são arquivos e cria lista com as informações
lista_inf = []
for item in lista_diretorio:
    if os.path.isfile(f'{caminho}/{item}'):
        nome = item
        data_criacao = os.path.getctime(item)
        data_modificacao = os.path.getmtime(item)
        tamanho = os.path.getsize(item)
        lista_inf.append((tamanho, data_criacao, data_modificacao, nome))

# classifica em ordem decrescente de tamanho
lista_inf.sort(reverse=True)

# imprime a lista de arquivo com as informações
print(f'Diretório: {caminho}\n')
print('NOME', 31*' ', 'CRIADO', 18*' ', 'MODIFICADO', 11*' ', 'TAMANHO')
for tamanho, data_criacao, data_modificacao, nome in lista_inf:
    data_criacao = datetime.fromtimestamp(data_criacao).strftime('%d/%m/%Y %H:%M:%S')
    data_modificacao = datetime.fromtimestamp(data_modificacao).strftime('%d/%m/%Y %H:%M:%S')
    print(f'{nome:<30} {data_criacao:>25} {data_modificacao:>25} {tamanho:>10,}\n'.replace(',','.'))
print(f'Total de Arquivos: {len(lista_inf)}\n')




"""### informações do sistema
sistema = os.environ
for chave, valor in sistema.items():
    print(f'{chave}: {valor}\n')"""