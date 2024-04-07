import tkinter as tk
from tkinter import *

from Class.Matriz import Matriz
from Class.Botao import Botao

class EntryLinhaColunaTabela:
    def __init__(self, frame, texto_msg, text_botao):
        self.frame = frame
        self.msg = texto_msg
        self.text_botao = text_botao
        
        self.num_linha = 0
        self.num_coluna = 0
        pass
    def receber(self, comando):
        entry_conteudo_frame = Frame(self.frame)
        entry_conteudo_frame.pack()
    
        botao_msg = Label(entry_conteudo_frame, text=self.msg, font=('Arial', 14))
        botao_msg.grid(row=0,column=0)
    
        self.entry_linha = Entry(entry_conteudo_frame, width=10)
        self.entry_linha.grid(row=0, column=1, padx=3)
        
        botao_msg = Label(entry_conteudo_frame, text='X', font=('Arial', 14))
        botao_msg.grid(row=0,column=2)
        
        self.entry_coluna = Entry(entry_conteudo_frame, width=10)
        self.entry_coluna.grid(row=0, column=3, padx=3)
    
        botao_gerar_tabela = Botao(self.text_botao, comando)
        botao_gerar_tabela.printBotaoGrid(0, 4, entry_conteudo_frame)
    
    def getNumLinha(self):
        if self.entry_linha.get() == '':
            return None
        else: 
            return int(self.entry_linha.get())
    
    def getNumColuna(self):
        if self.entry_coluna.get() == '':
            return None
        else: 
            return int(self.entry_coluna.get())

class EntryTabela:
    def __init__(self, frame, texto_msg, text_botao):
        self.frame = frame
        self.msg = texto_msg
        self.tex_botao = text_botao
        self.tabela = None
        
        self.num_linhas = 2
        self.num_colunas = 2
        self.conteudo = None

    def receber(self):
        self.receber_linha_coluna = EntryLinhaColunaTabela(self.frame, self.msg, self.tex_botao)
        self.receber_linha_coluna.receber(self.verificar)
        
        self.receberValoresTabela()
        
    def verificar(self):
        self.num_linhas = self.receber_linha_coluna.getNumLinha()
        self.num_colunas = self.receber_linha_coluna.getNumColuna()
        
        if self.num_linhas != None and self.num_colunas != None:
            self.receberValoresTabela()
        
    def receberValoresTabela(self):
        if self.tabela != None:
            self.tabela.destroy()
        
        self.tabela = Frame(self.frame, padx=10, pady=5, background='#F00',
                            borderwidth=3, relief='raised')
        self.tabela.pack()
        
        self.conteudo = []

        for i in range(self.num_linhas):
            linha = []
            for j in range(self.num_colunas):
                entrada = Entry(self.tabela, width=10)
                entrada.delete(0, tk.END)
                entrada.insert(0, '0')
                entrada.grid(row=i, column=j, padx=5, pady=5)
                linha.append(entrada)
            self.conteudo.append(linha)

    def getMatriz(self):
        matriz = Matriz(self.num_linhas, self.num_colunas)
        valores = []
        for linha in self.conteudo:
            valores_linha = []
            for entrada in linha:
                valores_linha.append(float(entrada.get()))
            valores.append(valores_linha)
        matriz.setElementos(valores)
        return matriz
        

class EntryMatriAndComand():
    def __init__(self, frame):
        self.frame = frame
        pass
    
    def receber(self, msg, comando_det, comando_trans, comando_inv):
        tabela_frame = tk.Frame(self.frame)
        tabela_frame.pack(padx=3,pady=3)
        self.receber_tabela = EntryTabela(tabela_frame, msg, 'Gerar Matriz')
        self.receber_tabela.receber()
        
        botao_frame = tk.Frame(self.frame)
        botao_frame.pack()
        
        botao_det = Botao('Determiante', comando_det)
        botao_det.setLargura(12)
        botao_det.printBotaoGrid(0, 0, botao_frame)
        
        botao_trans = Botao('Transposta', comando_trans)
        botao_trans.setLargura(12)
        botao_trans.printBotaoGrid(0, 1, botao_frame)
        
        botao_inv = Botao('Inversa', comando_inv)
        botao_inv.setLargura(12)
        botao_inv.printBotaoGrid(0, 2, botao_frame)
    
    def getMatriz(self):
        return self.receber_tabela.getMatriz()