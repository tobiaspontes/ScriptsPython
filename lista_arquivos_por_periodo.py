import os
from datetime import datetime

# limpa a tela
os.system('cls')

# define a pasta inicial da pesquisa
pasta = input('O caminho inicial é C:/Users/jtspontes/OneDrive - Secretaria da Fazenda e Planejamento do Estado de São Paulo/\n\nInforme o nome da pasta: ')
caminho = f'C:/Users/jtspontes/OneDrive - Secretaria da Fazenda e Planejamento do Estado de São Paulo/{pasta}'

# lista todos os arquivos e diretórios da pasta inicial
lista_geral = os.listdir(path=caminho)

# cria lista só com os arquivos (data de modificação e nome)
lista_arquivo = []
for item in lista_geral:
    if os.path.isdir(f'{caminho}/{item}'):
        continue
    if os.path.isfile(f'{caminho}/{item}'):
        nome = item
        data_modificacao = os.path.getmtime(f'{caminho}/{item}')
        data_modificacao = datetime.fromtimestamp(data_modificacao).strftime('%d/%m/%Y %H:%M:%S')
        data_modificacao = datetime.strptime(data_modificacao, '%d/%m/%Y %H:%M:%S')
        lista_arquivo.append((data_modificacao, nome))

# classifica em ordem decrescente de data de modificação
lista_arquivo.sort(reverse=True)

# usuário informa datas para pesquisa
data_inicial = input('Data inicial (dd/mm/aaaa): ')
data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
data_final = input('Data final (dd/mm/aaaa): ')
data_final = datetime.strptime(data_final, '%d/%m/%Y')

# imprime resultado
print(f'\nDIRETÓRIO: {caminho}\n')
print(f'ARQUIVOS EDITADOS ENTRE {data_inicial:%d/%m/%Y} E {data_final:%d/%m/%Y}\n')
contador = 0
for data_modificacao, nome in lista_arquivo:
    if data_modificacao >= data_inicial and data_modificacao <= data_final:
        print(f'{nome:<80} - {data_modificacao:%d/%m/%Y %H:%M:%S}')
        contador += 1
print(f'\nTOTAL: {contador} arquivos')