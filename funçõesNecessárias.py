# for numero in numerous:
#   print(numero)
"""
def somar(a, b):
    return a + b

resultado = somar(3, 5)
print("Resultado da soma:", resultado)
"""

#usando tupla
#quando você quer garantir que os elementos não sejam modificados acidentalmente.
coordenadas = (10, 20)

#usando matriz
#úteis para armazenar informações estruturadas em linhas e colunas.
matriz = [[1, 2],
          [3, 4]]

#usando dicionario, famoso JSON
#quando precisar armazenar pares chave-valor.
pessoa = {
    "Nome": "Kaynam",
    "Idade": 28,
}
#tambem usando dict
pessoa2 = dict(Nome="Kaynam", Idade=28)

#Usando lista
#Use listas quando precisar armazenar uma coleção ordenada e mutável de elementos.
#Listas permitem adicionar, remover e modificar elementos.
number: list[int] = [1, 5, 6, 23, -0.90, 1234, 99]

numbers: list[int | float] = [99, 0.6, -0.11, 2, -0.90, 1234, 99]

number2 = sorted(number)
print('Ordenado do menor ao maior: ', number2)

number2 = sorted(number, reverse=True)
print('Ordenado do maior ao menor: ', number2)

print('__________')

number.sort()
print('Ordenado dentro da lista, Menor ao Maior: ', number)

number.sort(reverse=True)
print('Ordenado dentro da lista, Maior ao menor: ', number)





