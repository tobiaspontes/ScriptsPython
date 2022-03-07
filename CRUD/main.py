######### importando o Tkinter #########
from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

######### importando o Tkcalendar #########
from tkcalendar import Calendar, DateEntry

######### importando a view #########
from view import *

######### definindo a paleta de cores #########
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

######### criando janela #########
janela = Tk()
janela.title('')
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

######### dividindo a janela #########
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# variável tree global
global tree

# criando a função para inserir dados
def inserir_dados():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    dia = e_cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()
    lista = [nome, email, tel, dia, estado, assunto]
    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir(lista)
        messagebox.showinfo('Sucesso', 'Dados inseridos!')
        # limpar campos de entrada
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')
        # limpar o frame direito
        for widget in frame_direita.winfo_children():
            widget.destroy()
        # chamar a função mostrar para apresentar todos os dados
        mostrar()

# criando função para atualizar os dados
def atualizar_dados():
    try:
        tree_dados = tree.focus()  # coloca o foco na linha selecionada da tabela(tree)
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']  # nesta lista tem id, nome, email, telefone, estado, assunto

        valor_id = tree_lista[0]

        # limpar campos de entrada
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')

        # mostrar os dados selecionados
        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_cal.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_assunto.insert(0, tree_lista[6])

        def atualiza():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_tel.get()
            dia = e_cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()
            lista = [nome, email, tel, dia, estado, assunto, valor_id]
            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualizar(lista)
                messagebox.showinfo('Sucesso', 'Dados atualizados!')
                # limpar campos de entrada
                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                e_cal.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_assunto.delete(0, 'end')
                # limpar o frame direito
                for widget in frame_direita.winfo_children():
                    widget.destroy()
                #  chamar a função mostrar para apresentar todos os dados
                mostrar()

        # botão confirmar
        b_confirmar = Button(frame_baixo, command=atualiza, text='Confirmar', width=10, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=115, y=370)  

    except IndexError:
        messagebox.showerror('Erro', 'Selecione dado na tabela')

# criando função para deletar os dados
def deletar_dados():
    try:
        tree_dados = tree.focus()  # coloca o foco na linha selecionada da tabela(tree)
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']  # nesta lista tem id, nome, email, telefone, estado, assunto

        valor_id = [tree_lista[0]] # passando o id como uma lista 

        # limpar campos de entrada
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')

        # mostrar os dados selecionados
        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_cal.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_assunto.insert(0, tree_lista[6])

        def deleta():
            deletar(valor_id)
            messagebox.showinfo('Sucesso', 'Dados deletados!')
            # limpar campos de entrada
            e_nome.delete(0, 'end')
            e_email.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_estado.delete(0, 'end')
            e_assunto.delete(0, 'end')
            # limpar o frame direito
            for widget in frame_direita.winfo_children():
                widget.destroy()
            #  chamar a função mostrar para apresentar todos os dados
            mostrar()

        # botão confirmar
        b_confirmar = Button(frame_baixo, command=deleta, text='Confirmar', width=10, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=215, y=370)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione dado na tabela') 

######### configurando frame direito #########
def mostrar():

    global tree  # tree será chamada em outras funções

    lista = consulta()

    # lista para cabeçalho
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

######### label cima #########
app_nome = Label(frame_cima, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

######### configurando frame baixo #########

# nome
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

# email
l_email = Label(frame_baixo, text='Email *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

# telefone
l_tel = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_tel.place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)

# data consulta
l_cal = Label(frame_baixo, text='Data da Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2,  justify='center', date_pattern='dd/mm/yyyy')
e_cal.place(x=15, y=220)

# estado consulta
l_estado = Label(frame_baixo, text='Estado da Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=165, y=220)

# sobre
l_assunto = Label(frame_baixo, text='Consulta Sobre *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_assunto.place(x=10, y=250)
e_assunto = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_assunto.place(x=15, y=280)

# botão inserir
b_inserir = Button(frame_baixo, command=inserir_dados, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

# botão atualizar
b_atualizar = Button(frame_baixo, command=atualizar_dados, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=115, y=340)

# botão deletar
b_deletar = Button(frame_baixo, command=deletar_dados, text='Deletar', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=215, y=340)

# chamando a função mostrar
mostrar()

janela.mainloop()












