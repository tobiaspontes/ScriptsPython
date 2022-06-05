from googlesearch import search

# Texto da busca
query = 'João Tobias da Silva Pontes'

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