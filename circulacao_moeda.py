from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests


def pesquisa_moeda():
    try:
        data = data_entry.get()
        link = f"https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=100&$filter=Data%20eq%20{data}&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"
        requisicao = requests.get(link)
        informacoes = requisicao.json()

        valores = informacoes['value']
        if len(valores) == 0:
            messagebox.showwarning(title="Aviso", message="Não foi possível obter os dados para a data informada!")
            return

        # apura o montante total de moeda em circulação
        total_valor = 0
        for i in valores:
            total_valor += i["Valor"]

        # cria lista de tuplas, cada uma com os dados da moeda correspondente
        lista_moedas = []
        for i in valores:
            vespecie = i["Especie"]
            vtipo = i["Denominacao"]
            vquantidade = f'{i["Quantidade"]:,.0f}'.replace(',','.')
            vvalor = f'{i["Valor"]:,.2f}'.replace('.','v').replace(',','.').replace('v',',')
            vpercentual = f'{i["Valor"] / total_valor:.2%}'
            lista_moedas.append((vespecie, vtipo, vquantidade, vvalor, vpercentual))
            
                 
        # classifica a lista de moeda em ordem crescente de espécie
        lista_moedas.sort(key=lambda x:x[0])

        # preenche o treeview
        for (vespecie, vtipo, vquantidade, vvalor, vpercentual) in lista_moedas:
            treeview.insert("", END, values=(vespecie, vtipo, vquantidade, vvalor, vpercentual))
    except:
        messagebox.showwarning(title="Aviso", message="Não foi possível obter os dados para a data informada!")
        return


### criando a janela
janela = Tk()
janela.title("Dinheiro em Circulação")
janela.geometry("530x500")
janela.resizable(False, False)

frame = Frame(janela, relief=RIDGE, borderwidth=1)
frame.pack(fill="both", expand="yes", padx=10, pady=5)

label_data = Label(frame, text="Informe a data (AAAA-MM-DD)", padx=10, pady=10)
label_data.place(x=10, y=10)

data_entry = Entry(frame, width=15, justify='center')
data_entry.place(x=200, y=20)

botao = Button(frame, text="Pesquisar", command=pesquisa_moeda, relief=RAISED, overrelief=RIDGE)
botao.place(x=350, y=20)

treeview = ttk.Treeview(frame, columns=("especie", "tipo", "quantidade", "valor", "percentual"), show="headings", height=15, padding=10)
treeview.column("especie", minwidth=0, width=70)
treeview.column("tipo", minwidth=0, width=50, anchor="center")
treeview.column("quantidade", minwidth=0, width=100, anchor="e")
treeview.column("valor", minwidth=0, width=120, anchor="e")
treeview.column("percentual", minwidth=0, width=100, anchor="center")
treeview.heading("especie", text="ESPÉCIE")
treeview.heading("tipo", text="TIPO")
treeview.heading("quantidade", text="QUANTIDADE", anchor="e")
treeview.heading("valor", text="VALOR", anchor="e")
treeview.heading("percentual", text="% VALOR TOTAL", anchor="center")
treeview.place(x=20, y=70)

# estiliza a treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", background="lightblue", foreground="black")

label_versao = Label(janela, text="Fonte: Banco Central", font=("Arial", 10), padx=10)
label_versao.place(x=20, y=450)

data_entry.focus()

janela.mainloop()