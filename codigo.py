
nome = input("Digite seu nome: ")
# forma de input de um numero int.
# idade = int(input("Digite sua idade: "))


class Pessoa:  # Objeto
    def __init__(self, nome, idade):
        self.nome = nome  # aqui o self é o mesmo que o this
        self.idade = idade


# gerando objetos a partir da class pessoa
pessoa1 = Pessoa("João", 30)
print("Pessoa 1:", pessoa1.nome, pessoa1.idade)

print('__________________')

pessoa2 = Pessoa("Maria", 25)
print("Pessoa 2:", pessoa2.nome, pessoa2.idade)

print('__________________')

# Array (lista)
numeros = [11, -2, 3, 4, 5, -99, 0.4, 1, 100, 7]
nomes = ["Wallace", "João", "Maria", "Caroline", "Pedro", "Ana Heloize"]

numeros.sort(reverse=True)
print('Comando reverse, ordena resersa da lista:', numeros)
print('__________________')

numeros.sort()
print('Comando sort, ordena dentro da lista: ', numeros)

print('__________________')
nomes.append(nome)  # aqui vai adicionar o input a lista

# Acesso a elementos de uma lista
# comando sempre irá acessar o primeiro da lista.
primeiro_Numero = numeros[0]

# comando sempre irá acessar o ultimo da lista.
ultimo_Nome = nomes[-1]

print('__________________')
# comando para ordenar uma lista
nomes_Ordenados = sorted(nomes)
print('Lista ordenada. ', nomes_Ordenados)

print('__________________')
numeros_Ordenados = sorted(numeros)
print('Numeros Ordenados. ', numeros_Ordenados)

print('__________________')
numeros_Ordenados_Reversos = sorted(numeros, reverse=True)
print('Numeros Ordenados Reversos. ', numeros_Ordenados_Reversos)

nome_busca = input('Digite o nome a ser procurado. ')

if nome_busca in nomes:
    existe = True
    print(existe, ': O nome', nome_busca, 'encontrado. ')

else:
    existe = False
    print(existe, ': O nome', nome_busca, 'não encontrado.')
