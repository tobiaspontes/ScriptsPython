from pathlib import Path


# # # # # # # # # # # # #   manipulando diretórios   # # # # # # # # # # # # # # # # # # # #
caminho = Path()
caminho_absoluto = caminho.absolute()
nome = caminho_absoluto.name
raiz = caminho_absoluto.root
pai = caminho_absoluto.parent
lista_pais = list(caminho_absoluto.parents)
parts = caminho_absoluto.parts
arquivo = Path(__file__)
home = Path.home()

print(f'\nCaminho relativo: {caminho}\n')
print(f'Caminho absoluto: {caminho_absoluto}\n')
print(f'Nome: {nome}\n')
print(f'Raiz: {raiz}\n')
print(f'Pai: {pai}\n')
print(f'Lista de pais: {lista_pais}\n')
print(f'Parts: {parts}\n')
print(f'Arquivo: {arquivo}\n')
print(f'Home: {home}\n')

# criando diretórios
pastas_gerais = caminho / 'pastas_gerais'
pastas_gerais.mkdir(exist_ok=True)  # cria o diretório 'pastas_gerais'
pasta_qualquer = pastas_gerais / 'pasta_qualquer'
pasta_qualquer.mkdir(exist_ok=True)  # cria o diretório 'pasta_qualquer'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # #   manipulando arquivos   # # # # # # # # # # # # # # # # # # # #
caminho = Path.home() / 'OneDrive' / 'Documentos'
lista_arquivos = caminho.glob('*.*')  # gera lista de arquivos do diretório atual
for arquivo in lista_arquivos:
    print(f'\n{arquivo.name}')

# criando arquivo
arquivo_qualquer = pasta_qualquer / 'arquivo_qualquer.txt'
arquivo_qualquer.touch()   # cria o arquivo

# preenchendo a pasta com arquivos
for i in range(10):
    arquivo = pasta_qualquer / f'arquivo_{i}.txt'
    arquivo.touch()


# glob
# pasta_teste.glob("**/*.txt"): todos arquivos txt de todas as pastas a partir de pasta_teste
# pasta_teste.glob('*.txt'): todos arquivos txt da pasta_teste

# renomeando um arquivo
outro_nome = arquivo_qualquer.rename(pasta_qualquer / 'outro_nome.txt')   # renomeia o arquivo
print(f'Nome do arquivo: {outro_nome.name}')

# renomeando vários arquivos
for contador, arquivo_txt in enumerate(pasta_qualquer.glob("**/*.txt")):
    novo_nome = pasta_qualquer / f"outro_nome{contador:02d}.txt"
    arquivo_txt.rename(novo_nome)

# imprime os arquivos
for arquivo in pasta_qualquer.glob('*.txt'):
    print(arquivo)

# deleta os arquivos
for arquivo in pasta_qualquer.glob('*.txt'):
    arquivo.unlink()


# criando o arquivo
arquivo_qualquer = pasta_qualquer / 'arquivo_qualquer.txt'
arquivo_qualquer.touch()   # cria o arquivo

# escrevendo no arquivo
arquivo_qualquer.write_text('Olá mundo!')
# imprimindo o texto contido no arquivo
print(arquivo_qualquer.read_text()) 

# outra maneira
arquivo_qualquer.write_text('') # apaga o texto anterior do arquivo
with arquivo_qualquer.open('a+') as file:   # abre o arquivo no modo append
    file.write('Uma linha\n')
    file.write('Outra linha\n')
print(arquivo_qualquer.read_text())

# testando existência do arquivo
print(f'\nArquivo existe? : {arquivo_qualquer.exists()}\n')  # True
print(f'É um arquivo? : {arquivo_qualquer.is_file()}\n')     # True

# nome completo, extensão e nome do arquivo
print(f'Nome completo: {arquivo_qualquer.name}\n')    # retorna o nome completo do arquivo
print(f'Extensão: {arquivo_qualquer.suffix}\n')       # retorna o sufixo do arquivo
print(f'Nome: {arquivo_qualquer.stem}\n')             # retorna o nome do arquivo


arquivo_qualquer.unlink()         # exclui o arquivo
pasta_qualquer.rmdir()            # exclui o diretório
pastas_gerais.rmdir()             # exclui o diretório