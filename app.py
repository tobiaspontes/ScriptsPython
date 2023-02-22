from tkinter import *
from tkinter import messagebox
from datetime import datetime
 
def formatacao_cpf():
    def formatar_cpf(event = None):
        texto = entry.get().replace(".", "").replace("-", "")[:11]
        novo_texto = ""
        if event.keysym.lower() == "backspace": return      
        for index in range(len(texto)):           
            if not texto[index] in "0123456789": continue
            if index in [2, 5]: novo_texto += texto[index] + "."
            elif index == 8: novo_texto += texto[index] + "-"
            else: novo_texto += texto[index]
        entry.delete(0, "end")
        entry.insert(0, novo_texto)

    tela = Toplevel(app)
    tela.title("Formatação de CPF")
    label = Label(tela, text="Informe o CPF", font=("Arial", 20))
    label.pack(side='left', padx=10)
    entry = Entry(tela, font=("Arial", 20), width=15, justify='center')
    entry.bind("<KeyRelease>", formatar_cpf)
    entry.pack(padx=10, pady=50)


def formatacao_cnpj():
    def formatar_cnpj(event = None):   
        texto = entry.get().replace(".", "").replace("-", "").replace("/","")[:14]
        novo_texto = ""
        if event.keysym.lower() == "backspace": return       
        for index in range(len(texto)):           
            if not texto[index] in "0123456789": continue
            if index in [1, 4]: novo_texto += texto[index] + "."
            elif index == 7: novo_texto += texto[index] + "/"
            elif index == 11: novo_texto += texto[index] + "-"
            else: novo_texto += texto[index]
        entry.delete(0, "end")
        entry.insert(0, novo_texto)


    tela = Toplevel(app)
    tela.title("Formatação de CNPJ")
    # tela.geometry("600x200")
    label = Label(tela, text="Informe o CNPJ", font=("Arial", 20))
    label.pack(side='left', padx=10)
    entry = Entry(tela, font=("Arial", 20), width=20, justify='center')
    entry.bind("<KeyRelease>", formatar_cnpj)
    entry.pack(padx=10, pady=50)


def equacao_2_grau():
    def main():
        '''
        Função principal do programa: pede ao usuário os coeficientes
        da equação de segundo grau
        '''
        if entry_a.get() == "" or entry_b.get() == "" or entry_c.get() == "":
            messagebox.showerror(title="ERRO", message="Preencha todos os campos de constantes.")
            return       
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        imprime_raizes(a, b, c)

        
    def imprime_raizes(a, b, c):
        '''
        Função que calcula e imprime as raízes
        '''
        import math
        d = Delta(a, b, c)
        if d < 0:
            label_resulado["text"] = "Esta equação não possui raízes reais."
        else:
            if d == 0:
                raiz1 = -b / (2 * a) 
                label_resulado["text"] = f'A raiz desta equação é {raiz1:.2f}'
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                if raiz1 < raiz2:
                    label_resulado["text"] = f'As raízes da equação são {raiz1:.2f} e {raiz2:.2f}'
                else:
                    label_resulado["text"] = f'As raízes da equação são {raiz2:.2f} e {raiz1:.2f}'

                                    
    def Delta(a, b, c):
        '''
        Função que retorna o delta da fórmula de Bhaskara.
        '''
        return (b ** 2) - (4 * a * c)


    janela = Toplevel(app)
    janela.title("Equação do 2º Grau")
    janela.geometry("300x250")
    janela.resizable(False, False)

    frame_constantes = LabelFrame(janela, text="Constantes", relief=SOLID, borderwidth=1)
    frame_constantes.pack(fill="both", expand="yes", padx=10, pady=10)
    label_a = Label(frame_constantes, text="a =")
    label_a.place(x=10, y=10)
    entry_a = Entry(frame_constantes, width=5, justify='center')
    entry_a.place(x=40, y=10)
    label_b = Label(frame_constantes, text="b =")
    label_b.place(x=100, y=10)
    entry_b = Entry(frame_constantes, width=5, justify='center')
    entry_b.place(x=130, y=10)
    label_c = Label(frame_constantes, text="c =")
    label_c.place(x=190, y=10)
    entry_c = Entry(frame_constantes, width=5, justify='center')
    entry_c.place(x=220, y=10)
    button_calcular = Button(frame_constantes, text="Calcular", command=main)
    button_calcular.place(x=110, y=50)
    frame_resultado = LabelFrame(janela, text="Resultado", relief=SOLID, borderwidth=1)
    frame_resultado.pack(fill="both", expand="yes", padx=10, pady=10)
    label_resulado = Label(frame_resultado, text="", padx=10, pady=10, font=("Ivy", 10, "bold"))
    label_resulado.place(x=10, y=10)
    entry_a.focus()


def analise_combinatoria():
    def calculo():
        n = int(entry_n.get())
        k = int(entry_k.get())
        label_combinacao["text"] = f'O total de combinações de {n} elementos tomados {k} a {k} é igual a {combinacao(n,k):,.0f}'.replace(',','.') + '\n\nNa combinação, a ordem dos elementos não importa: (a,b) = (b,a).'
        label_arranjo["text"] = f'O total de arranjos de {n} elementos tomados {k} a {k} é igual a {arranjo(n,k):,.0f}'.replace(',','.') + '\n\nNo arranjo, a ordem dos elementos importa: (a,b) é diferente de (b,a).'


    def fatorial(n):
        fat = 1
        while n > 1:
            fat *= n
            n -= 1
        return fat


    def combinacao(n, k):
        # Função que retorna a quantidade de combinações de n elementos
        # tomados k a k.
        # Na combinação, a ordem dos elementos não importa: (a,b) = (b,a).
        c = fatorial(n) / (fatorial(k) * fatorial(n - k))
        return c


    def arranjo(n, k):
        # Função que retorna a quantidade de arranjos de n elementos
        # tomados k a k.
        # No arranjo, a ordem dos elementos importa: (a,b) != (b,a).
        a = fatorial(n) / fatorial(n - k)
        return a 


    root = Toplevel(app)
    root.geometry("500x300")
    root.title("Análise Combinatória")
    Label(root, text="Entre com o número de elementos da análise").pack(padx=10, anchor=W)
    entry_n = Entry(root, width=10, justify='center')
    entry_n.pack(padx=10, anchor=W)
    Label(root, text="Entre com o número da combinação").pack(padx=10, anchor=W)
    entry_k = Entry(root, width=10, justify='center')
    entry_k.pack(padx=10, anchor=W)
    Button(root, text="Calcular", command=calculo).pack()
    frame_combinacao = LabelFrame(root, text="Combinação", relief=SOLID, borderwidth=1)
    frame_combinacao.pack(fill="both", expand="yes", padx=10)
    label_combinacao = Label(frame_combinacao, text="", padx=10)
    label_combinacao.place(x=10, y=5)
    frame_arranjo = LabelFrame(root, text="Arranjo", relief=SOLID, borderwidth=1)
    frame_arranjo.pack(fill="both", expand="yes", padx=10, pady=10)
    label_arranjo = Label(frame_arranjo, text="", padx=10)
    label_arranjo.place(x=10, y=5)
    entry_n.focus()


def calculadora():
    # criando função para entrada de valores
    def entrar_valores(event):
        global todos_valores          # definindo a variável todos_valores como global
        todos_valores = todos_valores + str(event)
        # passando o valor para a tela
        valor_texto.set(todos_valores)


    # criando função para calcular
    def calcular():
        global todos_valores   # definindo a variável todos_valores como global
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))


    # criando a função para limpar a tela
    def limpar_tela():
        global todos_valores   # definindo a variável todos_valores como global
        todos_valores = ''
        valor_texto.set('')

    cor1 = '#3b3b3b' # black
    cor2 = '#feffff' # white
    cor3 = '#38576b' # azul
    cor4 = '#eceff1' # cinza
    cor5 = '#ffab40' # laranja

    janela = Toplevel(app)
    janela.title('Calculadora')
    janela.geometry('235x310')
    janela.config(bg=cor1)

    # criando frames
    frame_tela = Frame(janela, width=235, height=50, bg=cor3)
    frame_tela.grid(row=0, column=0)
    frame_corpo = Frame(janela, width=235, height=268)
    frame_corpo.grid(row=1, column=0)
    # criando a variável todos_valores
    global todos_valores   # definindo a variável todos_valores como global
    todos_valores = ''
    valor_texto = StringVar()
    # criando label
    app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, bg=cor3, fg=cor2, font=('Ivy 18'))
    app_label.place(x=0, y=0)
    # criando botões
    b_1 = Button(frame_corpo, command=limpar_tela, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # relief: estilo do botão; overrelief: aparência do botão quando passar o mouse
    b_1.place(x=0, y=0)
    b_2 = Button(frame_corpo, command=lambda:entrar_valores('%'), text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_2.place(x=118, y=0)
    b_3 = Button(frame_corpo, command=lambda:entrar_valores('/'), text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_3.place(x=177, y=0)
    b_4 = Button(frame_corpo, command=lambda:entrar_valores('7'), text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_4.place(x=0, y=52)
    b_5 = Button(frame_corpo, command=lambda:entrar_valores('8'), text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_5.place(x=59, y=52)
    b_6 = Button(frame_corpo,command=lambda:entrar_valores('9'), text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_6.place(x=118, y=52)
    b_7 = Button(frame_corpo, command=lambda:entrar_valores('*'), text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_7.place(x=177, y=52)
    b_8 = Button(frame_corpo, command=lambda:entrar_valores('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_8.place(x=0, y=104)
    b_9 = Button(frame_corpo, command=lambda:entrar_valores('5'), text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_9.place(x=59, y=104)
    b_10 = Button(frame_corpo, command=lambda:entrar_valores('6'), text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_10.place(x=118, y=104)
    b_11 = Button(frame_corpo, command=lambda:entrar_valores('-'), text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_11.place(x=177, y=104)
    b_12 = Button(frame_corpo, command=lambda:entrar_valores('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_12.place(x=0, y=156)
    b_13 = Button(frame_corpo, command=lambda:entrar_valores('2'), text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_13.place(x=59, y=156)
    b_14 = Button(frame_corpo, command=lambda:entrar_valores('3'), text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_14.place(x=118, y=156)
    b_15 = Button(frame_corpo, command=lambda:entrar_valores('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_15.place(x=177, y=156)
    b_16 = Button(frame_corpo, command=lambda:entrar_valores('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # relief: estilo do botão; overrelief: aparência do botão quando passar o mouse
    b_16.place(x=0, y=208)
    b_17 = Button(frame_corpo, command=lambda:entrar_valores('.'), text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_17.place(x=118, y=208)
    b_18 = Button(frame_corpo, command=calcular, text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_18.place(x=177, y=208)


def mostra_data_hora():
    janela = Toplevel(app)
    janela.title('Data e Hora Atuais')
    janela.geometry('300x150')
    janela.resizable(False, False)
    lbl_data = Label(janela, text='', border=3, relief=GROOVE, padx=5, pady=5, font=('Courier New', 15, 'bold'), foreground='blue', width=15)
    lbl_data.pack(side=TOP, pady=20)
    lbl_hora = Label(janela, text='', border=3, relief=GROOVE, padx=5, pady=5, font=('Courier New', 15, 'bold'), foreground='blue', width=15)
    lbl_hora.pack(side=BOTTOM, pady=20)
    now = datetime.now()
    lbl_data['text'] = now.strftime("%d/%m/%Y")
    lbl_hora['text'] = now.strftime("%H:%M:%S")


def converte_temperatura():
    def cel_fahr():
        C = float(ent_celsius.get())
        F = C * (9 / 5) + 32
        lbl_celsius_convertido['text'] = f'{F:.1f} °F'


    def fahr_cel():
        F = float(ent_farenheit.get())
        C = (F - 32) * (5 / 9)
        lbl_farenheit_convertido['text'] = f'{C:.1f} °C'


    janela = Toplevel(app)
    janela.title('Conversor de Temperatura')
    janela.geometry('480x200')
    janela.resizable(False, False)
    frm1 = LabelFrame(janela, text='Celsius para Farenheit', borderwidth=2, relief=RIDGE, height=100, font=('Arial', 12, 'bold'), fg='blue')
    frm1.pack(fill='x', padx=10, pady=10, expand='yes')
    lbl_celsius = Label(frm1, text='Entre com a temperatura em ˚C')
    lbl_celsius.pack(side='left', padx=10, pady=10)
    ent_celsius = Entry(frm1, width=10, justify='center')
    ent_celsius.pack(side='left', padx=10, pady=10)
    ent_celsius.focus()
    btn_celsius = Button(frm1, text='Converte', command=cel_fahr)
    btn_celsius.pack(side='left', padx=10, pady=10)
    lbl_celsius_convertido = Label(frm1, text='', bg='white', width=10)
    lbl_celsius_convertido.pack(side='left', padx=10, pady=10)
    frm2 = LabelFrame(janela, text='Farenheit para Celsius', borderwidth=2, relief=RIDGE, height=100, font=('Arial', 12, 'bold'), fg='blue')
    frm2.pack(fill='x', padx=10, pady=10, expand='yes')
    lbl_farenheit = Label(frm2, text='Entre com a temperatura em ˚F')
    lbl_farenheit.pack(side='left', padx=10, pady=10)
    ent_farenheit = Entry(frm2, width=10, justify='center')
    ent_farenheit.pack(side='left', padx=10, pady=10)
    btn_farenheit = Button(frm2, text='Converte', command=fahr_cel)
    btn_farenheit.pack(side='left', padx=10, pady=10)
    lbl_farenheit_convertido = Label(frm2, text='', bg='white', width=10)
    lbl_farenheit_convertido.pack(side='left', padx=10, pady=10)


def quebra_senha():
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

    janela = Toplevel(app)
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


app = Tk()
app.geometry("600x200")
app.resizable(False, False)
app.title("Aplicativos Python")
frame1 = Frame(app, borderwidth=2, relief=SOLID, padx=10, pady=10, border=5, background='#da70d6')
frame1.pack(fill='x', expand='yes')
frame2 = Frame(app, borderwidth=2, relief=SOLID, padx=10, pady=10, border=5, background='#a14107')
frame2.pack(fill='x', expand='yes')
frame3 = Frame(app, borderwidth=2, relief=SOLID, padx=10, pady=10, border=5, background='#82ac64')
frame3.pack(fill='x', expand='yes')
Button(frame1,text="Formatar CPF", command=formatacao_cpf, width=20, relief=RAISED, overrelief=RIDGE).pack(padx=90, side='left')
Button(frame1,text="Formatar CNPJ", command=formatacao_cnpj, width=20, relief=RAISED, overrelief=RIDGE).pack(side='left')
Button(frame2,text="Equação 2º Grau", command=equacao_2_grau, width=20, relief=RAISED, overrelief=RIDGE).pack(padx=20, side='left')
Button(frame2,text="Análise Combinatória", command=analise_combinatoria, width=20, relief=RAISED, overrelief=RIDGE).pack(padx=20, side='left')
Button(frame2,text="Calculadora", command=calculadora, width=20, relief=RAISED, overrelief=RIDGE).pack(padx=20, side='left')
Button(frame3,text="Data e Hora", command=mostra_data_hora, width=20, relief=RAISED, overrelief=RIDGE).pack(padx=20, side='left')
Button(frame3,text="Conversor Temperatura", command=converte_temperatura, width=20, relief=RAISED, overrelief=RIDGE).pack(padx=20, side='left')
Button(frame3,text="Quebra Senha", command=quebra_senha, width=20, relief=RAISED, overrelief=RIDGE).pack(padx=20, side='left')
 
app.mainloop()