### código para formatar a entrada de CPF
### o código só aceita números e o tamanho da entrada não pode ultrapassar 11 dígitos
### se for digitado números e pontos ou traço, o código ignora e ao fim formata o CPF
from tkinter import *


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


tela = Tk()
tela.title("Formatação de CPF")

label = Label(tela, text="Informe o CPF", font=("Arial", 20))
label.pack(side='left', padx=10)
entry = Entry(tela, font=("Arial", 20), width=15, justify='center')
entry.bind("<KeyRelease>", formatar_cpf)
entry.pack(padx=10, pady=50)

tela.mainloop()