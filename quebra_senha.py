from tkinter import *


def analisa_senha():
    senha = ent.get()
    qtde_caracteres_lista = len(caracteres)
    qtde_caracteres_senha = len(senha) 
    resultado = achar_senha(senha, qtde_caracteres_senha, qtde_caracteres_lista)
    mostra_resultado(qtde_caracteres_senha, resultado)


def achar_senha(s, p, q):
    resultado = []      
    while p > 0:       
        for i in range(q):
            if caracteres[i] == s[p - 1]:
                resultado.append(caracteres[i])
        p -= 1
    return resultado


def mostra_resultado(p, resultado):
    n = p
    x = ''
    while p > 0:
        x += resultado[p - 1]
        p -= 1
    lbl_saida1['text'] = 'A senha digitada foi'
    lbl_saida2['text'] = f'{x}'
    lbl_saida3['text'] = f'\nA senha tem {n} caracteres.'


caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z','1','2','3','4','5','6','7','8','9','0', '!','@','#','$','%','&','*','(',')','-','_','=','+','ç','^','~','[',']','{','}',',','.',';',':','/','?','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','W','Z','Ç','|','`','´','<','>','á','à','é','è','ó','ò','í','ì','ú','ù','â','ê','î','ô','û','ã','õ','¨']

janela = Tk()
janela.title('Quebra de Senha')
janela.geometry('400x200')
janela.resizable(False, False)

frm = Frame(janela, relief=RAISED, border=2, padx=5, pady=5)
frm.pack(fill='x', expand='yes')

lbl = Label(frm, text='Digite a senha', padx=5, pady=5)
lbl.pack(side='left')

ent = Entry(frm, width=25, show='*')
ent.pack(side='left', padx=5)
ent.focus()

but = Button(frm, text='Analisa', command=analisa_senha, padx=5, relief=RAISED, overrelief=RIDGE, width=15)
but.pack(side='left')

frm_saida = Frame(janela, relief=RAISED, border=2, padx=5, pady=5, background='white')
frm_saida.pack(fill='x')

lbl_saida1 = Label(frm_saida, text='', padx=10, pady=25, font=('Arial', 12, 'bold'), background='white')
lbl_saida1.pack(side='left')

lbl_saida2 = Label(frm_saida, text='', padx=10, pady=25, font=('Arial', 12, 'bold'), fg='red', background='white')
lbl_saida2.pack(side='left')

lbl_saida3 = Label(janela, text='', padx=10, font=('Arial', 12, 'bold'))
lbl_saida3.pack()

janela.mainloop()