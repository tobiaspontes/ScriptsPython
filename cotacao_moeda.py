import requests
import os

os.system("cls")

moeda = input("Informe a moeda para cotação (USD, EUR, etc.): ").upper()

url = f"https://economia.awesomeapi.com.br/all/{moeda}-BRL"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    cotacao = data[f"{moeda}"]["bid"]
    print(f"\nCotação: 1 {moeda} = {cotacao} Reais\n".replace(".",","))
else:
    print(f"\nErro ao ler cotação da moeda informada {moeda}.\n")