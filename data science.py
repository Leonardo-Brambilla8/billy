lista1 = list()
nome = list()
peso = list()
idade = list()
lista2 = list()
lista3 = dict()
while True:
    a = int(input('Vitoria ou derrota: ')).upper()[0]
    for c in range(0 , a):
        nome.append(str(input('nome?: ')))
        idade.append(int(input('idade ')))
        peso.append(int(input('peso: ')))
        lista1.append(nome)
        lista1.append(idade)
        lista1.append(peso)
    lista3['nome'] = nome[:]
    lista3['idade'] = idade[:]
    lista3['peso'] = peso[:]
    lista2.append(lista3.copy())
    while True:
        resp = str(input('continuar?: ')).upper()[0]
        if resp in 'SN':
            break
        print('erro')
    if resp == 'N':
        break
lista2.append(lista1)

for i in lista3.keys():
    print(i, end=' ')

print('')
for i in range(0, a):
    print(nome[i], end='     ')
    print(idade[i], end='    ')
    print(peso[i], end='     ')
    print('')
