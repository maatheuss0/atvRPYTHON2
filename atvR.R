#Vetores
# Exercício Fácil: Crie um vetor com os números de 1 a 10 e imprima-o

vetor <- 1:10
print(vetor)

#Exercício Fácil:Crie um vetor com os números pares de 2 a 20 e imprima-o

vetor <- seq(2, 20, by= 2)
print(vetor)

#Exercício Médio: Calcule a soma dos elementos de um vetor com números de 1 a 100

vetor<- 1:101
soma<-sum(vetor)
print(soma)

#Exercício Médio: Encontre o maior e o menor valor em um vetor de números aleatórios entre 1
#e 1000, de tamanho 50

vetor <- sample(1:1000, 50, replace = TRUE)
maior <- max(vetor)
menor <- min(vetor)
print(paste("Maior:",maior, "Menor:",menor))

#Exercício Difícil: Crie um vetor com os 10 primeiros números primos
def eh_primo(n):
  if n == 1: return False
for i in range(2, int(n**0.5) + 1):
  if n%i == 0: 
  return False
return True

vetor_primos = []
num = 2
while len(vetor_primos) < 10:
  if e_primo(num):
  vetor_primos.append(num)
num += 1

print(vetor_primos)

# ou

eh_primo <- function(n) {
  if(n<=1) {
    return(FALSE)
  }
  for(i in 2:sqrt(n)) {
    if (n %% i == 0){
      return(FALSE)
    }
  }
  return(TRUE)
}

primos <- c()
num <- 2
while(length(primos)<10){
  if(eh_primo(num)){
    primos <- c(primos, num)
  }
  num <- num + 1
}

#Exercício Difícil: Inverta a ordem dos elementos de um vetor de tamanho 20, preenchido com
#números aleatórios

vetor <- sample(1:100, 20, replace = TRUE)
vetor_invertido <- rev(vetor)
print(vetor_invertido)

#Matrizes em R
#Exercício Fácil: Crie uma matriz 3x3 de 1 a 9 e imprima-a
matriz <- matrix(1:9, nrow = 3, ncol = 3) #nrow: numero de linhas ncol: numero de colunas
print(matriz)

#Exercício Fácil: Crie uma matriz identidade 4x4 e imprima-a
matriz_identidade <- diag(4)
print(matriz_identidade)

#Exercício Médio: Some duas matrizes 2x2

matriz1 <- matrix(c(1,2,3,4), nrow = 2, ncol = 2)
matriz2 <- matrix(c(5,6,7,8), nrow = 2, ncol = 2)
matriz_soma <- matriz1 + matriz2
print(matriz_soma)

#Exercício Médio: Multiplique duas matrizes 2x2

matriz1 <- matrix(c(1,2,3,4), nrow = 2, ncol = 2)
matriz2 <- matrix(c(5,6,7,8), nrow = 2, ncol = 2)
matriz_mult <- matriz1 %*% matriz2
print(matriz_mult)

#Exercício Difícil: Calcula a transposta de uma matriz 3x3

matriz1 <- matrix(1:9), nrow = 3, ncol = 3)
matriz_transposta <- t(matriz)
print(matriz_transposta)

#Exercício Difícil: Calcula a determinante de uma matriz 3x3

matriz <- matrix(1:9, nrow = 3, ncol = 3)
determinante <- det(matriz)
print(determinante)

#Fatores em python
cores <- factor(c("Vermelho", "Azul", "Verde"))
print(cores)

#Crie um vetor de fatores para os dias da semana e imprima-os
semana <- factor(c('segunda', 'terca', 'quarta', 'quinta', 'sexta'))
print(semana)

#Crie um vetor de fatores com as categorias "baixo", "médio" e "alto" e ordene-os
niveis <- factor(c("Baixo", "medio", "alto"), levels = c("Baixo", "medio", "alto"), ordered=TRUE)
print(niveis)

#Converta um vetor de fatores em um vetor numerico
categorias <- factor(c("Baixo", "medio", "alto"), levels = c("Baixo", "medio", "alto"), ordered=TRUE)
numeros <- as.numeric(categorias)
print(numeros)

#crie um vetor de fatores com as categorias "pequeno", "medio" e "grande"
tamanhos <- factor(c("Pequeno", "Medio", "Grande"), levels = c("Pequeno", "Medio", "Grande"), ordered=TRUE)
levels(tamanhos)[levels(tamanhos) == "Pequeno"] <- "Extra pequeno"
print(tamanhos)

#Crie um vetor de fatores com 100 elementos aleatorios 
set.seed(123)
categorias <- c("baixo", "medio", "alto")
vetor <- sample(categorias, 100, replace=TRUE)
fatores <- factor(vetor, levels = categorias, ordered=TRUE)
frequencias <- table(fatores)
print(frequencias)

#Lista em R
lista <- list(1,2,3,4,5)
print(lista)

#Adicione um elemento "6" ao final da lista
lista <- list(1,2,3,4,5)
lista[[6]] <- 6
print(lista)

#Remova o terceiro elemento da lista
lista <- list(1,2,3,4,5)
lista <- lista[-3]
print(lista)

#inverta a ordem dos elementos da lista
lista <- list(1,2,3,4,5)
lista_invertida <- rev(lista)
print(lista_invertida)

#Crie uma lista de listas (matriz) de tamanho 3x3 e calcule a soma da cada linha
matriz <- list(c(1,2,3), c(4,5,6), c(7,8,9))
soma_linhas <- sapply(matriz, sum)
print(soma_linhas)

#Tuplas
#Crie uma tupla contendo os numeROS de 1 a 5 e imprima-a
tupla <- list(1,2,3,4,5)
print(tupla)

#Imprima o 2 elemento
tupla <- list(1,2,3,4,5)
print(tupla[[3]])

#crie uma tupla contendo tres tuplas internas, cada uma com dois elementos
#Imprima o 2 elemento
tupla <-  list(list(1,2), list(3,4), list(5,6))
print(tupla)

#concatene duas tuplas (1,2,3) e (4,5,6) e imprima o resultado
lista1 <- list(1,2,3)
lista2 <- list(4,5,6)
lista_concatenada <- c(lista1,lista2)
print(lista_concatenada)

#Crie uma tupla com os elementos (1,2,3,4,5) e encontre o indice do numero 4
tuplas <- list(1,2,3,4,5)
indice <- which(unlist(lista) == 4)
print(indice)

#crie um dicionario com   as   chaves "nome, ""idade", e "cidade"
dicionario <- list(nome="Ana",idade=25,cidade="São Paulo")
print(dicionario)

dicionario = list(nome="Ana",idade=25,cidade="São Paulo")
dicionario$profissao = "engenheira"
print(dicionario)