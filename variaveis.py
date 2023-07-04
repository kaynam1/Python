"""
mult = 10.2*10
soma = 10+10
sub = 10-5
pot = 10**2

print(mult, type(mult))
print(soma, type(soma))
print(sub, type(sub))
print(pot, type(pot))


nome = input('Digite seu nome. ')
qt_letras = len(nome)

if qt_letras <= 4:
   print('Seu nome é curto. ')
elif qt_letras >= 5 and qt_letras <= 6:
   print('Seu nome é normal. ')
elif qt_letras > 6:
   print('Seu nome é muito grande. ')


hora = float(input('Digite a hora. '))

if hora <= 11:
   print('Bom dia!!')
elif hora > 11 and hora <=17:
   print('Boa tarde!! ')
elif hora >= 18 and hora <= 23:
   print('Boa noite.')
else:
    print('Numero fora do padrão de 24 horas.')



num = input("Digite o número a ser verificado. ")
resto = float(num) % 2

if not num.isnumeric():
   print('Numero não inteiro')

elif resto == 0:
   print(f'{num} É par')
else:
   print(f'{num} É impar')


num1 = float(input('Digite um número. '))
num2 = float(input('Digite outro numero. '))

try:
   num1 = float(num1)
   num2 = float(num2)

   print(f'A soma foi {num1 + num2:.2f}')
   print(f'A multiplicação foi {num1 * num2:.2f}')

except:
   print(f'Não foi possível realizar a operação com a entrada de dados.')


#Manipulando strings [] chama os indices e recorta a string
texto = 'Kaynam'
print(texto[1:3])
"""
# usando for in range e separando pares e impar
#manipulando listas

list_pares = []
list_impares = []
for loop in range(10):
    if loop % 2 == 0:
        list_pares.append(loop)
    elif loop % 2 != 0:
        list_impares.append(loop)

print(list_pares)
print(list_impares)
print('Aqui será a união da lista completa. ')

new_list = list_pares + list_impares

#new_list.extend(list_impares)
#new_list.extend(list_pares)

new_list.sort()
print(new_list)
print('__Aqui usarei as funções para inserir dados:__')

#Assim para inserir na ultima casa, o insert solicita índice
new_list.insert(len(new_list), 99)
#Assim sempre será inserido no final, sem pedir índice.
new_list.append(100)
print(new_list)

print('__Aqui usarei as funções para deletar dados:__')

#em branco irá apagar o último, essa função só deleta 1 por vez.
new_list.pop()
print(new_list)
#para um index especifico deverá se mencionado.
new_list.pop(5)
print(new_list)