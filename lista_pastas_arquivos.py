import os

os.system('cls')

# caminho = r"C:\Users\jtspontes\OneDrive - Secretaria da Fazenda e Planejamento do Estado de São Paulo\Documentos"
pasta = input('Informe o nome da pasta: ')
caminho = f'C:/Users/jtspontes/OneDrive - Secretaria da Fazenda e Planejamento do Estado de São Paulo/{pasta}'

lista_geral = os.listdir(path=caminho)
lista_diretorio = []
lista_arquivo = []
for item in lista_geral:
    if os.path.isdir(f'{caminho}/{item}'):
        lista_diretorio.append(item)
    if os.path.isfile(f'{caminho}/{item}'):
        lista_arquivo.append(item)

print(f'DIRETÓRIO: {caminho}\n')

print('PASTAS\n')
for diretorio in lista_diretorio:
    print(f'{diretorio}')
print(f'\nTotal: {len(lista_diretorio)} pastas\n\n')

print('ARQUIVOS\n')
for arquivo in lista_arquivo:
    print(f'{arquivo}')
print(f'\nTotal: {len(lista_arquivo)} arquivos')