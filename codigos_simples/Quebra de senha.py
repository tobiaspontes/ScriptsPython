# Quebra de senha
import os


def achar_senha(p, q):
    resultado = []
    try:  
        while p > 0:       
            for i in range(q):
                if caracteres[i] == senha[p - 1]:
                    resultado.append(caracteres[i])
            p -= 1
        return resultado
    except:
        print('Caracter inválido na senha!')


def mostra_resultado(p, resultado):
    try:
        x = ''
        while p > 0:
            x += resultado[p - 1]
            p -= 1
        print(f'\nA senha digitada foi {x}')
    except:
        print('Caracter inválido na senha!')
    

if __name__ == '__main__':
    os.system('cls')
    senha = input('Entre com a senha: ')
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z','1','2','3','4','5','6','7','8','9','0', '!','@','#','$','%','&','*','(',')','-','_','=','+','ç','^','~','[',']','{','}',',','.',';',':','/','?','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','W','Z','Ç','|','`','´','<','>','á','à','é','è','ó','ò','í','ì','ú','ù','â','ê','î','ô','û','ã','õ','¨']
    qtde_caracteres_lista = len(caracteres)
    qtde_caracteres_senha = len(senha) 
    resultado = achar_senha(qtde_caracteres_senha, qtde_caracteres_lista)
    mostra_resultado(qtde_caracteres_senha, resultado)