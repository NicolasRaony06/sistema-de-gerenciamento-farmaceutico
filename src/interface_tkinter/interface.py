from tkinter import *
from tkinter import messagebox
from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto
from decimal import Decimal
from datetime import datetime

class Interface:
    def __init__(self):
        self.root = None
        self.farmacia = None
    
    def interface(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Interface')

        botao_registrarFarmacia = Button(
            self.root, 
            text="Registrar Farmacia", 
            padx=10, 
            pady=10, 
            command=self.registrarFarmacia).grid(row=0, column=0)
        
        botao_registrarGerente = Button(
            self.root, 
            text="Registrar Gerente", 
            padx=10, 
            pady=10, 
            command=self.registrarGerente).grid(row=0, column=1)
        
        botao_registrarAtendente = Button(
            self.root, 
            text="Registrar Atendente", 
            padx=10, 
            pady=10, 
            command=self.registrarAtendente).grid(row=2, column=0)
        
        botao_registrarProduto = Button(
            self.root, 
            text="Registrar Produto", 
            padx=10, 
            pady=10, 
            command=self.registrarProduto).grid(row=2, column=1)
        
        self.root.mainloop()

    def __temFarmacia(self):
        if not self.farmacia:
            messagebox.showinfo("Farmácia não registrada.", "É necessário criar farmácia primeiro.")
            self.root.destroy()
            self.interface()
        return True
    
    def __campoVazioMessagem(self, funcao):
        messagebox.showerror("Erro de Valor", f"Campo não pode estar vázio.")
        funcao()

    def __botaoRegistrar(self, texto, funcao):
        botao_registrar = Button(
            self.root, 
            text=texto, 
            padx=10, 
            pady=10, 
            command=funcao)
        return botao_registrar

    def registrarFarmacia(self):
        from src.farmacia.farmacia import Farmacia
        self.root.destroy()
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
                self.interface()

        self.__botaoRegistrar('Registrar Farmácia', instanciar).grid(row=1, column=0)

        self.root.mainloop()

    def registrarAtendente(self):
        self.root.destroy()
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Registrar Atendente')
        self.__temFarmacia()

        Label(self.root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.root, text="CPF:").grid(row=1)
        campo_cpf = Entry(self.root, width=25, borderwidth=1)
        campo_cpf.grid(row=1, column=1, columnspan=2)

        Label(self.root, text="Data de Nascimento:").grid(row=2)
        campo_dataNasc = Entry(self.root, width=25, borderwidth=1)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarAtendente)
            cpf = campo_cpf.get()
            data_nascimento = datetime.strptime(campo_dataNasc.get(), "%d-%m-%Y") if campo_dataNasc.get() else None
            salario = campo_salario.get()

            try:
                self.farmacia._registrarAtendente(nome, cpf, data_nascimento, Decimal(salario))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Atendente.", f"{erro}")
                self.registrarAtendente()
            
            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.root.destroy()
            self.interface()

        self.__botaoRegistrar('Registrar Atendente', instanciar).grid(row=4, column=1)

        self.root.mainloop()

    def registrarGerente(self):
        self.root.destroy()
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Registrar Gerente')
        self.__temFarmacia()
        
        if self.farmacia.getGerente():
            messagebox.showinfo("Gerente já registrado", "Gerente só pode ser registrado uma única vez.")
            self.root.destroy()
            self.interface()

        Label(self.root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.root, text="CPF:").grid(row=1)
        campo_cpf = Entry(self.root, width=25, borderwidth=1)
        campo_cpf.grid(row=1, column=1, columnspan=2)

        Label(self.root, text="Data de Nascimento:").grid(row=2)
        campo_dataNasc = Entry(self.root, width=25, borderwidth=1)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarGerente)
            cpf = campo_cpf.get()
            data_nascimento = datetime.strptime(campo_dataNasc.get(), "%d-%m-%Y") if campo_dataNasc.get() else None
            salario = campo_salario.get()

            try:
                self.farmacia._registrarGerente(nome, cpf, data_nascimento, Decimal(salario))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                self.registrarGerente()
            
            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.root.destroy()
            self.interface()

        self.__botaoRegistrar('Registrar Gerente', instanciar).grid(row=4, column=1)

        self.root.mainloop()

    def registrarProduto(self):
        '''Cria objeto de produto e já adiciona em estoque''' # por enquanto fica essa solução apra produto
        self.root.destroy()
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Registrar Produto')
        self.__temFarmacia()

        Label(self.root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.root, text="Preço:").grid(row=1)
        campo_preco = Entry(self.root, width=25, borderwidth=1)
        campo_preco.grid(row=1, column=1, columnspan=2)

        Label(self.root, text="Fabricante:").grid(row=2)
        campo_fabricante = Entry(self.root, width=25, borderwidth=1)
        campo_fabricante.grid(row=2, column=1, columnspan=2)

        Label(self.root, text="Quantidade:").grid(row=3)
        campo_qtd = Entry(self.root, width=25, borderwidth=1)
        campo_qtd.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarProduto)
            fabricante = campo_fabricante.get() if campo_fabricante.get() else self.__campoVazioMessagem(self.registrarProduto)
            preco = campo_preco.get()
            quantidade = campo_qtd.get()

            try:
                self.farmacia._estoque.adicionar_produto(Produto(nome, Decimal(preco), fabricante), int(quantidade))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Produto.", f"{erro}")
                self.registrarProduto()
            
            campo_nome.delete(0, END)
            campo_fabricante.delete(0, END)
            campo_preco.delete(0, END)
            self.root.destroy()
            self.interface()

        self.__botaoRegistrar('Registrar Produto', instanciar).grid(row=4, column=1)

        self.root.mainloop()

    