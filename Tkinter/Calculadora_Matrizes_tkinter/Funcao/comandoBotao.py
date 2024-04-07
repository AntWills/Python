from Funcao.matriz import printResultado
from Class.Matriz import gerar_matriz_magica
import random

def comando():
    print('A')
    
def comandoMatrizMagica(resultado_frame):
    matriz_resultado = gerar_matriz_magica(random.randrange(1, 10, 2))
    
    printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
    
def comandoResolverSistemaAxB(resultado_frame, matrizA, matrizB):
    matriz_resultado = matrizA.resolverSistemaEquacao(matrizB)
    
    if matriz_resultado == 'erro':
        printResultado(resultado_frame, None, True, 'Erro no Sistema de equaçãoes.')
    else:
        printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
    
def comandoMatrizInversaB(resultado_frame, matrizB):
    matriz_resultado = matrizB.inversa()
    
    printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
    
def comandoMatrizInversaA(resultado_frame, matrizA):
    matriz_resultado = matrizA.inversa()
    
    printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
    
def comandoMatrizTransB(resultado_frame, matrizB):
    matriz_resultado = matrizB.transposta()
    
    printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')

def comandoMatrizTransA(resultado_frame, matrizA):
    matriz_resultado = matrizA.transposta()
    
    printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
    
def comandoDetB(resultado_frame, matrizB):
    detMatriz = matrizB.detMatriz()
    
    if detMatriz == 'Erro':
        printResultado(resultado_frame, detMatriz, True, 'Erro no DetB.')
    else:
        printResultado(resultado_frame, detMatriz, True, 'DetB : ' + str(detMatriz))
    
def comandoDetA(resultado_frame, matrizA):
    detMatriz = matrizA.detMatriz()
    
    if detMatriz == 'Erro':
        printResultado(resultado_frame, detMatriz, True, 'Erro no DetA.')
    else:
        printResultado(resultado_frame, detMatriz, True, 'DetA : ' + str(detMatriz))
    
def comandoMultMatrizes(resultado_frame, matrizA, matrizB):
    matriz_resultado = matrizA * matrizB
    
    if matriz_resultado == 'Erro':
        printResultado(resultado_frame, matriz_resultado, True, 'Erro ao multiplicar.')
    else:
        printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
    
def comandoSubtrairtMatrizes(resultado_frame, matrizA, matrizB):
    matriz_resultado = matrizA - matrizB
    
    if matriz_resultado == 'Erro':
        printResultado(resultado_frame, matriz_resultado, True, 'Erro ao subtrair.')
    else:
        printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
    
def comandoSomarMatrizes(resultado_frame, matrizA, matrizB):
    matriz_resultado = matrizA + matrizB
    
    if matriz_resultado == 'Erro':
        printResultado(resultado_frame, matriz_resultado, True, 'Erro ao somar.')
    else:
        printResultado(resultado_frame, matriz_resultado, False, 'tudo certo')
