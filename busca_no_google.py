# Este código utiliza a biblioteca googlesearch para realizar uma pesquisa no google

from googlesearch import Search

# Texto da busca
query = 'roger federer'

# Faz a busca e cria lista com os links dos resultados
# result = list(Search(query, lang='pt-br', num_results=5))
resultado = Search(query, language='pt-br',number_of_results=10)

# Mostra resultados
print()
tamanho = len(resultado.results)
for i in range(tamanho):
    print(resultado.results[i])
    i += 1
