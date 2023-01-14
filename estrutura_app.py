from tkinter import *

root =  Tk()

class funcoes():
    
   def janela(self):
       import estrutura_app1

class application(funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame()
        root.mainloop()
    
    def tela(self):
        self.root.title('Main')
        self.root.configure(background='#483D8B')
        self.root.geometry('800x600')
        self.root.resizable(True, True)
        self.root.minsize(width=600, height=480)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx= 0.25, rely= 0.25, relwidth= 0.50, relheight= 0.46)
    
    def widgets_frame(self):
        self.bt_dentista = Button(self.frame_1, text='Gerenciar 1', command=self.janela)
        self.bt_dentista.place(relx=0.3, rely=0.20, relwidth=0.35, relheight=0.12)
        
        self.bt_paciente = Button(self.frame_1, text='Gerenciar 2', command=self.janela)
        self.bt_paciente.place(relx=0.3, rely=0.34, relwidth=0.35, relheight=0.12)
        
        self.bt_consulta = Button(self.frame_1, text='Gerenciar 3')
        self.bt_consulta.place(relx=0.3, rely=0.48, relwidth=0.35, relheight=0.12)

        self.bt_sair = Button(self.frame_1, text='Sair')
        self.bt_sair.place(relx=0.3, rely=0.62, relwidth=0.35, relheight=0.12)   

        self.lb_pesquisar = Label(self.frame_1, text='O que deseja fazer?')
        self.lb_pesquisar.place(relx=0.32 , rely=0.04)






application()