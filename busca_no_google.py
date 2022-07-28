# Este código utiliza a biblioteca googlesearch para realizar uma pesquisa no google

from googlesearch import search

# Texto da busca
query = 'roger federer'

# Faz a busca e cria lista com os links dos resultados
result = list(
    search(
        query,
        lang='pt-br',
        num_results=5
    )
)

# Mostra resultados
print()
print(result)