### código para formatar a entrada de CNPJ
### o código só aceita números e o tamanho da entrada não pode ultrapassar 14 dígitos
### se for digitado números e pontos ou traço ou barra, o código ignora e ao fim formata o CNPJ
from tkinter import *


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


tela = Tk()
tela.title("Formatação de CNPJ")
# tela.geometry("600x200")

label = Label(tela, text="Informe o CNPJ", font=("Arial", 20))
label.pack(side='left', padx=10)
entry = Entry(tela, font=("Arial", 20), width=20, justify='center')
entry.bind("<KeyRelease>", formatar_cnpj)
entry.pack(padx=10, pady=50)

tela.mainloop()