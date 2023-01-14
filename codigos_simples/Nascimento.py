# Receber entrada do usuário e imprimir uma mensagem

def obter_mes(n):
    if n == '1': return 'janeiro'
    if n == '2': return 'fevereiro'
    if n == '3': return 'março'
    if n == '4': return 'abril'
    if n == '5': return 'maio'
    if n == '6': return 'junho'
    if n == '7': return 'julho'
    if n == '8': return 'agosto'
    if n == '9': return 'setembro'
    if n == '10': return 'outubro'
    if n == '11': return 'novembro'
    if n == '12': return 'dezembro'

print('\nNascimento')
dia = input('\nEntre com o dia do seu nascimento: ')
mes = input('Entre com o mês do seu nascimento: ')
ano = input('Entre com o ano do seu nascimento: ')
print('\nVocê nasceu dia',dia,'de',obter_mes(mes),'de',ano,'\n')