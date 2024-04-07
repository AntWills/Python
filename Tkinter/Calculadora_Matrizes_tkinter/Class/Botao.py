import tkinter as tk
from tkinter import *


class Botao:
    def __init__(self, text, comando):
        self.text = text
        self.comando = comando
        self.tam_texto = 13
        self.largura = 14
        self.altura = 1
        pass

    def printBotaoPack(self, frame):
        self.frame = frame
        button = Button(self.frame, text=self.text, command=self.comando, 
        font=('Arial', self.tam_texto, 'bold'), borderwidth=2,  relief='groove', 
        width=self.largura, height=self.altura)
        button.pack(pady=2, padx=2)
        
    def printBotaoGrid(self, linha, coluna,  frame):
        self.frame = frame
        button = Button(self.frame, text=self.text, command=self.comando, 
        font=('Arial', self.tam_texto, 'bold'), borderwidth=2,  relief='groove', 
        width=self.largura, height=self.altura)
        button.grid(row=linha, column=coluna, pady=2, padx=2)
    
    def setAltura(self, altura):
        self.altura = altura
    def setLargura(self, largura):
        self.largura = largura
