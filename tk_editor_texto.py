import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def abrir_arquivo():
    # abre um arquivo para edição
    arquivo = askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not arquivo:
        return
    txt_editor.delete('1.0', tk.END) # limpa a caixa de edição
    with open(arquivo, mode='r', encoding='utf-8') as arquivo_entrada:
        texto = arquivo_entrada.read()
        txt_editor.insert(tk.END, texto)
    janela.title(f'Editor de Texto Simples - {arquivo}')


def salvar_arquivo():
    # salva um arquivo
    arquivo = asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not arquivo:
        return
    with open(arquivo, mode='w', encoding='utf-8') as arquivo_saida:
        texto = txt_editor.get('1.0', tk.END)
        arquivo_saida.write(texto)
    janela.title(f'Editor de Texto Simples - {arquivo}')


janela = tk.Tk()
janela.title('Editor de Texto Simples')
janela.geometry('900x450')
janela.resizable(False, False)
# janela.rowconfigure(0, minsize=700, weight=1)
# janela.columnconfigure(1, minsize=800, weight=1)

txt_editor = tk.Text(janela, font=('Arial', 12))
frm_botoes = tk.Frame(janela, relief=tk.RAISED, bd=2)
btn_abrir = tk.Button(frm_botoes, text='Abrir', command=abrir_arquivo)
btn_salvar = tk.Button(frm_botoes, text='Salvar como', command=salvar_arquivo)

btn_abrir.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_salvar.grid(row=1, column=0, sticky='ew', padx=5)
frm_botoes.grid(row=0, column=0, sticky='ns')
txt_editor.grid(row=0, column=1, sticky='nsew')

janela.mainloop()
