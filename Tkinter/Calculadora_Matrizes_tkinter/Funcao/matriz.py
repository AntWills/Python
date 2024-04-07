import tkinter as tk
from tkinter import *


def printMatriz(frame, matriz, numLinha, numColuna):
    printMatriz = tk.Frame(frame, background='#fff')
    printMatriz.pack(side='left')

    for i in range(numLinha):
        for j in range(numColuna):
            label_elemento = tk.Label(
                printMatriz, text=matriz[i][j], font=('Arial', 15, 'bold'), bg='#fff')
            label_elemento.grid(row=i, column=j, padx=10)


def printErro(frame, tipo_erro):
    printErro = tk.Frame(frame, background='#fff')
    printErro.pack(side='left')

    label_erro = tk.Label(printErro, text=tipo_erro,
                          font=('Arial', 15, 'bold'), bg='#fff')
    label_erro.pack()


def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def printResultado(frame, matriz, erro, tipo_erro):
    limpar_frame(frame)

    msg_frame = tk.Frame(frame, bg='#000')
    msg_frame.pack(padx=10, pady=10)

    msg_label = tk.Label(msg_frame, text='Resultado:',
                         font=('Arial', 15, 'bold'), bg='#fff')
    msg_label.pack()

    conteudo_frame = tk.Frame(frame)
    conteudo_frame.pack()

    if erro:
        printErro(conteudo_frame, tipo_erro)
    else:
        printMatriz(conteudo_frame, matriz.getMatriz(),
                    matriz.getNumLinha(), matriz.getNumColuna())
