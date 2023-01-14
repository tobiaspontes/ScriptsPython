# Este código calcula fatorial, combinação e arranjo
from tkinter import *


def calculo():
    n = int(entry_n.get())
    k = int(entry_k.get())

    label_combinacao["text"] = f'O total de combinações de {n} elementos tomados {k} a {k} é igual a {combinacao(n,k):,.0f}\n\nNa combinação, a ordem dos elementos não importa: (a,b) = (b,a).'.replace(',','.')

    label_arranjo["text"] = f'O total de arranjos de {n} elementos tomados {k} a {k} é igual a {arranjo(n,k):,.0f}\n\nNo arranjo, a ordem dos elementos importa: (a,b) != (b,a).'.replace(',','.')


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


root = Tk()
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

root.mainloop()