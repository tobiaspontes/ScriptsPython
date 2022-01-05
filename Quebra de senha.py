# Quebra de senha

def achar_senha():
    for i in range(tamanho):
        for j in range(tamanho):
            for k in range(tamanho):
                for l in range(tamanho):
                    for m in range(tamanho):
                        for n in range(tamanho):
                            if lista[i]+lista[j]+lista[k]+lista[l]+lista[m]+lista[n] == senha:
                                print('A senha é {}'.format(lista[i]+lista[j]+lista[k]+lista[l]+lista[m]+lista[n]))
                                return
    print('Senha não identificada')
    return

senha = input('Entre com a senha(6 letras minúsculas): ')

lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','z']
tamanho = len(lista)

achar_senha()