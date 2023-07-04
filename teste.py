
# Forma de input de um número int.
# Idade = int(input("Digite sua idade: "))
name = input("Digite seu nome: ")

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
nomes = ["Wallace", "João", "Maria", "Caroline", "Pedro", "Ana Heloíze"]

numeros.sort(reverse = True)
print('Comando reverse, ordena reversa da lista:', numeros)
print('__________________')

numeros.sort()
print('Comando sort, ordena dentro da lista: ', numeros)

print('__________________')
nomes.append(name)  # aqui vai adicionar o input a lista

# Acesso a elementos de uma lista
# comando sempre irá acessar o primeiro da lista.
primeiro_Numero = numeros[0]

# comando sempre irá acessar o último da lista.
ultimo_Nome = nomes[-1]

print('__________________')
# comando para ordenar uma lista
nomes_Ordenados = sorted(nomes)
print('Lista ordenada. ', nomes_Ordenados)

print('__________________')
numeros_Ordenados = sorted(numeros)
print('Números Ordenados. ', numeros_Ordenados)

print('__________________')
numeros_Ordenados_Reversos = sorted(numeros, reverse=True)
print('Números Ordenados Reversos. ', numeros_Ordenados_Reversos)

nome_busca = input('Digite o nome a ser procurado. ')

if nome_busca in nomes:
    existe = True
    print(existe, ': O nome', nome_busca, 'encontrado. ')

else:
    existe = False
    print(existe, ': O nome', nome_busca, 'não encontrado.')
