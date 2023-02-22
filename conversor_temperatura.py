from tkinter import *


def cel_fahr():
   C = float(ent_celsius.get())
   F = C * (9 / 5) + 32
   lbl_celsius_convertido['text'] = f'{F:.1f} °F'

def fahr_cel():
   F = float(ent_farenheit.get())
   C = (F - 32) * (5 / 9)
   lbl_farenheit_convertido['text'] = f'{C:.1f} °C'


janela = Tk()
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

janela.mainloop()