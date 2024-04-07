import tkinter as tk
from tkinter import *

# from Class.Matriz import Matriz
from Class.Botao import Botao
from Class.Tabela import *
from Funcao.matriz import printResultado
from Funcao.title import printTitle
from Funcao.comandoBotao import *

def printButtons(all_buttons_frame):
    botao_soma = Botao('Soma : A + B', lambda : comandoSomarMatrizes(resultado_frame, 
                                                                     receber_matrizA.getMatriz(),
                                                                     receber_matrizB.getMatriz()))
    botao_menos = Botao('Menos : A - B', lambda : comandoSubtrairtMatrizes(resultado_frame,
                                                                           receber_matrizA.getMatriz(),
                                                                           receber_matrizB.getMatriz()))
    botao_mult = Botao('Mult : A * B', lambda : comandoMultMatrizes(resultado_frame, 
                                                                    receber_matrizA.getMatriz(),
                                                                    receber_matrizB.getMatriz()))
    botao_sistema = Botao('Sistema : Ax = B', lambda : comandoResolverSistemaAxB(resultado_frame,
                                                                         receber_matrizA.getMatriz(),
                                                                         receber_matrizB.getMatriz()))
    botao_matriz_magica = Botao('Matriz Mágica', lambda : comandoMatrizMagica(resultado_frame))
    
    botao_soma.printBotaoPack(all_buttons_frame)
    botao_menos.printBotaoPack(all_buttons_frame)
    botao_mult.printBotaoPack(all_buttons_frame)
    botao_sistema.printBotaoPack(all_buttons_frame)
    botao_matriz_magica.printBotaoPack(all_buttons_frame)

janela_principal = tk.Tk()
janela_principal.title('Matriz')
janela_principal.configure(borderwidth=4, relief="solid", bg='red')

conteudo_geral = Frame(janela_principal)
conteudo_geral.configure(borderwidth=2, relief="solid")
conteudo_geral.pack(pady=10,padx=10)

printTitle(conteudo_geral)

conteudo = Frame(conteudo_geral, borderwidth=2, relief="solid", bg='#6495ED')
conteudo.pack(padx=5, pady=5)

# #87CEEB
# #ADD8E6
# #B0E0E6
# #AFEEEE

all_buttons_operatoin_frame = Frame(conteudo, bg='#00ff00', borderwidth=3, relief='raised')
all_buttons_operatoin_frame.grid(row=0, column=0, pady=3, padx=10)

printButtons(all_buttons_operatoin_frame)

frame_tabelas = Frame(conteudo, bg='#fff000', borderwidth=3, relief='raised')
frame_tabelas.grid(row=0, column=1, pady=5, padx=5)

frame_matrizA = Frame(frame_tabelas, borderwidth=3, relief='ridge')
frame_matrizA.pack(side='left', padx=5, pady=5)

receber_matrizA = EntryMatriAndComand(frame_matrizA)
receber_matrizA.receber('Matriz A : ', 
                        lambda : comandoDetA(resultado_frame, receber_matrizA.getMatriz()), 
                        lambda : comandoMatrizTransA(resultado_frame, receber_matrizA.getMatriz()), 
                        lambda : comandoMatrizInversaA(resultado_frame, receber_matrizA.getMatriz()))

frame_matrizB = Frame(frame_tabelas, borderwidth=3, relief='ridge')
frame_matrizB.pack(side='left', padx=5, pady=5)

receber_matrizB = EntryMatriAndComand(frame_matrizB)
receber_matrizB.receber('Matriz B : ', 
                        lambda : comandoDetA(resultado_frame, receber_matrizB.getMatriz()), 
                        lambda : comandoMatrizTransB(resultado_frame, receber_matrizB.getMatriz()),
                        lambda : comandoMatrizInversaB(resultado_frame, receber_matrizB.getMatriz()))

resultado_frame = Frame(conteudo, bg='#fff', borderwidth=3, relief='raised')
resultado_frame.grid(row=0, column=2, padx=5,pady=3)

printResultado(resultado_frame, None, True, 'Nenhuma operação realizada')

janela_principal.mainloop()