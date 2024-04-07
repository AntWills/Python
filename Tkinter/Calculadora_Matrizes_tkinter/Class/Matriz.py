import scipy.linalg as la
import numpy as np

class Matriz:
    def __init__(self, numLinha, numColuna):
        self.numLinha = numLinha
        self.numColuna = numColuna
        self.matriz = []
        
        i = 0
        while(i < numLinha):
            linha = []
            self.matriz.append(linha)
            j = 0
            while(j < numColuna):
                self.matriz[i].append(float(0))
                j += 1
            i += 1
        pass
    
    def __add__(self, other):
        if self.numLinha != other.numLinha or self.numColuna != other.numColuna:
            print('Erro na soma')
            return 'Erro'
        
        nova_matriz = []
        for i in range(self.numLinha):
            nova_linha = []
            for j in range(self.numColuna):
                nova_linha.append(self.matriz[i][j] + other.matriz[i][j])
            nova_matriz.append(nova_linha)
            
        matriz = Matriz(self.getNumLinha(), self.getNumColuna())
        matriz.setElementos(nova_matriz)
        
        return matriz

    def __sub__(self, other):
        if self.numLinha != other.numLinha or self.numColuna != other.numColuna:
            print('Erro na soma')
            return 'Erro'
        
        nova_matriz = []
        for i in range(self.numLinha):
            nova_linha = []
            for j in range(self.numColuna):
                nova_linha.append(self.matriz[i][j] - other.matriz[i][j])
            nova_matriz.append(nova_linha)
        
        matriz = Matriz(self.getNumLinha(), self.getNumColuna())
        matriz.setElementos(nova_matriz)
        
        return matriz
    
    def __mul__(self, outra):
        if self.numColuna != outra.numLinha:
            return 'Erro'
        resultado = Matriz(self.numLinha, outra.numColuna)

        for i in range(resultado.numLinha):
            for j in range(resultado.numColuna):
                produto = 0
                for k in range(self.numColuna):
                    produto += self.matriz[i][k] * outra.matriz[k][j]
                resultado.matriz[i][j] = produto

        return resultado
    
    def detMatriz(self):
        if self.numLinha == self.numColuna:
            return la.det(self.matriz)
        return 'Erro'
    def inversa(self):
        matriz = Matriz(self.numLinha, self.numColuna)
        matriz.setElementos(np.round(la.inv(self.matriz), decimals=5))
        
        return matriz 

    def transposta(self):
        resultado = Matriz(self.numColuna, self.numLinha)
        for i in range(self.numColuna):
            for j in range(self.numLinha):
                resultado.setItem(self.matriz[j][i], i, j)
        return resultado
    
    def resolverSistemaEquacao(self, matriz):
        if self.numLinha != self.numColuna:
            return 'erro'
        if matriz.getNumLinha() != self.numLinha:
            return 'erro'
        if matriz.getNumColuna() != 1:
            return 'erro'
        
        matrizB = matriz.getMatriz()
        matrizA = self.matriz.copy()
        
        self._converterTriangularSuperior_(matrizA, matrizB)
        
        matriz_res = Matriz(self.numLinha, 1)
        matriz_res.setElementos(self._resolverTriangularSuperior_(matrizA, matrizB))
        return matriz_res
        
    def _converterTriangularSuperior_(self, matrizA, matrizB):
        iteracao = 0
        while(iteracao < self.numLinha):
            
            linha = self._getLinhaMaiorNum_(matrizA, iteracao)
            self._trocarLinhas_(matrizA, matrizB, iteracao+1, linha)
            
            divisor = matrizA[iteracao][iteracao]
            linha = iteracao+1
            while(linha < self.numLinha):
                multiplicador = -1*(matrizA[linha][iteracao]/divisor)
                j = iteracao
                while(j < self.numColuna):
                    matrizA[linha][j] = matrizA[linha][j] + multiplicador*matrizA[iteracao][j]
                    j += 1
                matrizB[linha][0] = matrizB[linha][0] + multiplicador * matrizB[iteracao][0]
                linha += 1
            iteracao += 1
        pass
    def _resolverTriangularSuperior_(self, matrizA, matrizB):
        Xn = []
        
        soma = 0.0
        i = self.numLinha - 1
        while(i >= 0):
            if len(Xn) == 0:
                Xn.append([matrizB[i][0]/matrizA[i][i]])
            else:
                j = 0
                quantXn = len(Xn)
                while(j < quantXn):
                    soma += matrizA[i][self.numColuna-j-1] * Xn[j][0]
                    j += 1
                Xn.append([(matrizB[i][0]-soma)/matrizA[i][i]])
            soma = 0.0
            i -= 1
        return list(reversed(Xn))
    def _trocarLinhas_(self, matrizA, matrizB, i1, i2):
        if i1 == i2:
            return
        
        i1 -= 1
        i2 -= 1

        if 0 <= i1 < len(matrizA) and 0 <= i2 < len(matrizA):
            linha_auxiliar_A = matrizA[i1].copy()
            linha_auxiliar_B = matrizB[i1].copy()
            
            matrizA[i1] = matrizA[i2]
            matrizA[i2] = linha_auxiliar_A
            
            matrizB[i1] = matrizB[i2]
            matrizB[i2] = linha_auxiliar_B
        else:
            print("Índices fora dos limites.")
    
    def _getLinhaMaiorNum_(self, matriz, itere):
        i = itere
        maiorLinha = itere
        while(i < self.numLinha):
            if moduloNum(matriz[i][itere]) > moduloNum(matriz[maiorLinha][itere]):
                maiorLinha = i
            i += 1
        
        return maiorLinha + 1
    def setElementos(self, matriz):
        self.matriz = matriz
    def setItem(self, item, linha, coluna):
        self.matriz[linha][coluna] = item
    def imprimir(self):
        i = 0
        while(i < self.numLinha):
            j = 0
            while(j < self.numColuna):
                print(self.matriz[i][j], end=" ")
                j += 1
            print()
            i += 1
    def getMatriz(self):
        return self.matriz
    def getNumLinha(self):
        return self.numLinha
    def getNumColuna(self):
        return self.numColuna
    
def gerar_matriz_magica(tamanho):
    matriz = [[0] * tamanho for _ in range(tamanho)]
    
    numero = 1
    i = 0
    j = tamanho // 2

    while numero <= tamanho * tamanho:
        matriz[i][j] = numero
        numero += 1
        ant_i = i
        ant_j = j
        
        i -= 1
        j += 1

        if i < 0:
            i = tamanho - 1
        if j == tamanho:
            j = 0
        if matriz[i][j] != 0:
            i = ant_i+1
            j = ant_j
    matriz_res = Matriz(tamanho, tamanho)
    matriz_res.setElementos(matriz)
    return matriz_res
    
def moduloNum(num):
    if num >= 0:
        return num
    return -1 * num