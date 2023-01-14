# Qual o servidor de e-mail?
print('\n\033[1;32mServidor de e-mail')
email = input('\nEntre com seu email: ')
tamanho = len(email)
servidor = ''
for i in range(tamanho):
   if email[i] == '@':
       servidor = email[i + 1:]
if servidor == '':
    print('\n\033[0;31me-mail inválido\n')
else:
      print('\n\033[0;35mO servidor de email é:',servidor,'\n')
