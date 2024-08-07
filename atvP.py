#Vetores
# Exercício Fácil: Crie um vetor com os números de 1 a 10 e imprima-o


vetor = list(range(1,11))
print(vetor)

#Exercício Fácil:Crie um vetor com os números pares de 2 a 20 e imprima-o

vetor= list(range(2, 21, 2))
print(vetor)

#Exercício Médio: Calcule a soma dos elementos de um vetor com números de 1 a 100

vetor= list(range(1,101))
soma= sum(vetor)
print(soma)

#Exercício Médio: Encontre o maior e o menor valor em um vetor de números aleatórios entre 1
#e 1000, de tamanho 50

import random 

vetor= list(sample.random(1,1001, 50))
maior= max(vetor)
menor= min(vetor)
print= ('Maior:',maior "Menor:",menor)

# ou

import random 

vetor= [random.randint(1,1000) for _ in range(50)]
maior= max(vetor)
menor= min(vetor)
print('Maior:',maior, "Menor:",menor)

#Exercício Difícil: Crie um vetor com os 10 primeiros números primos

def eh_primo(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

primos = []
num = 2
while len(primos) < 10:
  if eh_primo(num):
    primos.append(num)
  num += 1
print(primos)

#Exercício Difícil: Inverta a ordem dos elementos de um vetor de tamanho 20, preenchido com
#números aleatórios

import random

vetor = [random.randint(1,100) for _ in range(20)]
vetor_invertido = vetor[::-1]
print(vetor)
print(vetor_invertido)

#Matrizes em python
#Exercício Fácil: Crie uma matriz 3x3 de 1 a 9 e imprima-a

import numpy as np
matriz =np.arange(1,10).reshape(3,3)
print(matriz)

#Exercício Fácil: Crie uma matriz identidade 4x4 e imprima-a
import numpy as np
matriz_identidade = np.eye(4)
print(matriz_identidade)

#Exercício Médio: Some duas matrizes 2x2

import numpy as np
matriz1= np.array([[1,2],[3,4]])
matriz2= np.array([[5,6],[7,8]])
matriz_soma= matriz1 + matriz2
print(matriz_soma)

#Exercício Médio: Multiplique duas matrizes 2x2

import numpy as np
matriz1= np.array([[1,2],[3,4]])
matriz2= np.array([[5,6],[7,8]])
matriz_mult= matriz1 @ matriz2
print(matriz_mult)

#ou

import numpy as np
matriz1= np.array([[1,2],[3,4]])
matriz2= np.array([[5,6],[7,8]])
matriz_mult= np.dot(matriz1, matriz2)
print(matriz_mult)

#Exercício Difícil: Calcula a transposta de uma matriz 3x3

import numpy as np
matriz= np.array([[1,2,3],[4,5,6],[7,8,9])
matriz_transposta= np.transpose(matriz)
print(matriz_transposta)

#Exercício Difícil: Calcula a determinante de uma matriz 3x3

import numpy as np
matriz= np.array([[1,2,3],[4,5,6],[7,8,9]])
determinante= np.linalg.det(matriz)
print(determinante)

#Exercício Fácil: Crie um vetor de categorias (fatores) com as 
#cores "vermelho", "Azul" e "verde"

import pandas as pd 
cores = pd.categorical(['vermelho', 'azul', 'verde'])
print(cores)

#Crie um vetor de fatores para os dias da semana e imprima-os
import pandas as pd =
cores = pd.Categorical(['segunda', 'terca', 'quarta', 'quinta', 'sexta'])
print(cores)

#Crie um vetor de fatores com as categorias "baixo", "médio" e "alto" e ordene-os
import pandas as pd 
niveis = pd.Categorical(["Baixo", "medio", "alto"], categories=["Baixo", "medio", "alto"], ordered=True)
print(niveis)

#Converta um vetor de fatores em um vetor numerico
import pandas as pd
categorias = pd.Categorical(["Baixo", "medio", "alto"], categories=["Baixo", "medio", "alto"], ordered=True)
numeros = categorias.codes
print(numeros)

#crie um vetor de fatores com as categorias "pequeno", "medio" e "grande"
import pandas as pd
tamanhos = pd.Categorical(["pequeno", "medio", "grande"], categories=["pequeno", "medio", "grande"], ordered=True)
tamanhos2 = tamanhos.rename_categories({"pequeno", "medio", "grande"})
print(tamanhos2)

#Crie um vetor de fatores com 100 elementos aleatorios 
import pandas as pd
import random
categorias = ["baixo", "medio", "alto"]
vetor = [random.choice(categorias) for _ in range(100)]
fatores = pd.Categorical(vetor, categories=categorias, ordered = True)
frequencias = pd.value_counts(fatores)
print(frequencias)

#Crie uma lista contendo os numeros de 1 a 5
lista = [1,2,3,4,5]
lista

#Adicione um elemento "6" ao final da lista
lista = [1,2,3,4,5]
lista.append(6)
print(lista)

#Remova o terceiro elemento da lista
lista = [1,2,3,4,5]
lista.pop(2)
print(lista)

#inverta a ordem dos elementos da lista
lista = [1,2,3,4,5]
lista.reverse()
print(lista)

#Crie uma lista de listas (matriz) de tamanho 3x3 e calcule a soma da cada linha
matriz = [[1,2,3], [4,5,6], [7,8,9]]
soma_linhas = [sum(linha) for linha in matriz]
print(soma_linhas)

#Tuplas
#Crie uma tupla contendo os numeROS de 1 a 5 e imprima-a
tupla= (1,2,3,4,5)
print(tupla)

#Imprima o 2 elemento
tupla= (1,2,3,4,5)
print(tupla[2])

#crie uma tupla contendo tres tuplas internas, cada uma com dois elementos
#Imprima o 2 elemento
tupla= ((1,2), (3,4), (5,6))
print(tupla)

#concatene duas tuplas (1,2,3) e (4,5,6) e imprima o resultado
lista1=(1,2,3)
lista2=(4,5,6)
lista_concatenada =(lista1,lista2)
print(lista_concatenada)

#Crie uma tupla com os elementos (1,2,3,4,5) e encontre o indice do numero 4
tplas = (1,2,3,4,5)
indice = tplas.index(4)
print(indice)

#crie um dicionario com   as   chaves "nome, ""idade", e "cidade"
dicionario= {"nome":"Ana","idade":"25","cidade":"São Paulo"}
print(dicionario)

dicionario = {"nome":"Ana","idade":"25","cidade":"São Paulo"}
dicionario["profissao"] = "engenheira"
print(dicionario)
