from tkinter import *
 
def mensagem():
    toplevel = Toplevel(app)
 
    toplevel.title("SEGUNDA JANELA")
    toplevel.geometry("300x100")
 
 
    l1=Label(toplevel, image="::tk::icons::question") # question, information, error, warning
    l1.grid(row=0, column=0, pady=(20, 0), padx=(10, 30), sticky="e")
    l2=Label(toplevel,text="Tem certeza de que quer sair?")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
 
    b1=Button(toplevel,text="Sim", command=app.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2=Button(toplevel,text="Não", command=toplevel.destroy, width=10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")
 
 
app = Tk()
app.geometry("300x200")
app.title("Janela Principal")
Button(app,text="Segunda Janela", command=mensagem, width=20).pack(pady=80)
 
app.mainloop()