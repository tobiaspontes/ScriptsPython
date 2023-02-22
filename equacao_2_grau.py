from tkinter import *
from tkinter import messagebox


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


janela = Tk()
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

janela.mainloop()

