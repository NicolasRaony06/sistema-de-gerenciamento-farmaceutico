from tkinter import *

class Interface:
    def __init__(self):
        self.root = None
        self.farmacia = None

    def registrarFarmacia(self):
        from src.farmacia.farmacia import Farmacia
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Registrar Farmácia')
        campo_nome = Entry(self.root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=0, columnspan=2)

        def instanciar():
            nome = campo_nome.get()
            if nome:
                self.farmacia = Farmacia(nome)
                campo_nome.delete(0, END)
                self.root.destroy()

        botao_registrar = Button(
            self.root, 
            text='Registrar Farmácia', 
            padx=10, 
            pady=10, 
            command=instanciar)
        botao_registrar.grid(row=1, column=0)

        self.root.mainloop()