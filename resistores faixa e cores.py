<<<<<<< HEAD
# calculo de resistores
while True:
    lista = {'cores':2, 'faixa':1}
    a = lista[str(input('Por cores ou por faixa?: '))]
    if a == 1:
        dados2 = {100: 'marrom', 50: 'vermelho', 15: 'laranja', 25: 'amaralo', 10: 'azul', 5: 'violeta'}
        dados = {5: 'ouro', 1: 'marrom', 2: 'vermelho', 0.5: 'verde', 0.25: 'azul', 0.1: 'violeta', 0.05: 'cinza',
                 10: 'prata'}
        b = ['preto', 'marrom', 'vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'violeta', 'cinza', 'branco']
        a = int(input('quantas faixas tem o resistor?: '))
        if a == 4:
            f = (b[int(input('qual a primeira faixa?: '))])
            g = (b[int(input('qual a segunda faixa?: '))])
            h = (b[int(input("Quantos zero na 3 faixa?: "))])
            y = (dados[float(input("Qual é a faixa 4?:+- "))])
            print(str(f))
            print(str(g))
            print(str(h))
            print(str(y))
        elif a == 5:
            f = (b[int(input('qual a primeira faixa?: '))])
            g = (b[int(input('qual a segunda faixa?: '))])
            h = (b[int(input("Quantos zero na 3 faixa?: "))])
            y = (dados[float(input("Qual é a faixa 4?:+- "))])
            j = (dados[float(input("Qual é a faixa 5?:+- "))])
            print(str(f))
            print(str(g))
            print(str(h))
            print(str(y))
            print(str(j))
        elif a == 6:
            f = (b[int(input('qual a primeira faixa?: '))])
            g = (b[int(input('qual a segunda faixa?: '))])
            h = (b[int(input("Quantos zero na 3 faixa?: "))])
            y = (dados[float(input("Qual é a faixa 4?:+- "))])
            j = (dados[float(input("Qual é a faixa 5?:+- "))])
            k = (dados2[float(input("Qual é a faixa 6?: "))])
            print(str(f))
            print(str(g))
            print(str(h))
            print(str(y))
            print(str(j))
            print(str(k))
    elif a == 2:
        dados2 = {'marrom': 100, 'vermelho': 50, 'laranja': 15, 'amarelo': 25, 'azul': 10, 'violeta': 5}
        dados = {'ouro': 0.05, 'marrom': 0.01, 'vermelho': 0.02, 'verde': 0.005, 'azul': 0.0025, 'violeta': 0.001,'cinza': 0.0005, 'prata': 10}
        b = {'preto': 0, 'marrom': 1, 'vermelho': 2, 'laranja': 3, 'amarelo': 4, 'verde': 5, 'azul': 6, 'violeta': 7, 'cinza': 8, 'branco': 9}
        a = int(input('quantas faixas?: '))
        if a == 4:
            d = (((b[str(input('qual a primeira faixa?: '))]) * 10) + (b[str(input('qual a segunda faixa?: '))])) * (10 ** (b[str(input("Quantos zero na 3 faixa?: "))]))
            c = (dados[str(input("Qual é a faixa 4?:+- "))])
            print(f'a resistencia é {d}')
            print(f'o maximo é {d + (c * d)} o minimo é {d - (c * d)}')
        elif a == 5:
            d = (((b[str(input('qual a primeira faixa?: '))]) * 100) + (
            b[str(input('qual a segunda faixa?: '))]) * 10 + (b[str(input('qual a terceira faixa?: '))])) * (10 ** (b[str(input("Quantos zero na 3 faixa?: "))]))
            c = (dados[str(input("Qual é a faixa 4?:+- "))])
            print(f'a resistencia é {d}')
            print(f'o maximo é {d + (c * d)} o minimo é {d - (c * d)}')
        elif a == 6:
            d = (((b[str(input('qual é a cor da 1 faixa?: '))]) * 100) + (b[str(input('qual é a  cor da 2 faixa?: '))]) * 10 + (b[str(input('qual é a cor da 3 faixa?: '))])) * (
                            10 ** (b[str(input("Qual é a cor da 4 faixa?: "))]))
            c = (dados[str(input("Qual é a cor da 5 faixa?: "))])
            e = (dados2[str(input('qual a cor da 6 faixa?: '))])
            print(f'a resistencia é {d} {e}ppm/k')
=======
while True:
    lista = {'cores':2, 'faixa':1}
    a = lista[str(input('Por cores ou por faixa?: '))]
    if a == 1:
        dados2 = {100: 'marrom', 50: 'vermelho', 15: 'laranja', 25: 'amaralo', 10: 'azul', 5: 'violeta'}
        dados = {5: 'ouro', 1: 'marrom', 2: 'vermelho', 0.5: 'verde', 0.25: 'azul', 0.1: 'violeta', 0.05: 'cinza',
                 10: 'prata'}
        b = ['preto', 'marrom', 'vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'violeta', 'cinza', 'branco']
        a = int(input('quantas faixas tem o resistor?: '))
        if a == 4:
            f = (b[int(input('qual a primeira faixa?: '))])
            g = (b[int(input('qual a segunda faixa?: '))])
            h = (b[int(input("Quantos zero na 3 faixa?: "))])
            y = (dados[float(input("Qual é a faixa 4?:+- "))])
            print(str(f))
            print(str(g))
            print(str(h))
            print(str(y))

        elif a == 5:
            f = (b[int(input('qual a primeira faixa?: '))])
            g = (b[int(input('qual a segunda faixa?: '))])
            h = (b[int(input("Quantos zero na 3 faixa?: "))])
            y = (dados[float(input("Qual é a faixa 4?:+- "))])
            j = (dados[float(input("Qual é a faixa 5?:+- "))])
            print(str(f))
            print(str(g))
            print(str(h))
            print(str(y))
            print(str(j))
        elif a == 6:
            f = (b[int(input('qual a primeira faixa?: '))])
            g = (b[int(input('qual a segunda faixa?: '))])
            h = (b[int(input("Quantos zero na 3 faixa?: "))])
            y = (dados[float(input("Qual é a faixa 4?:+- "))])
            j = (dados[float(input("Qual é a faixa 5?:+- "))])
            k = (dados2[float(input("Qual é a faixa 6?: "))])
            print(str(f))
            print(str(g))
            print(str(h))
            print(str(y))
            print(str(j))
            print(str(k))
    elif a == 2:
        dados2 = {'marrom': 100, 'vermelho': 50, 'laranja': 15, 'amarelo': 25, 'azul': 10, 'violeta': 5}
        dados = {'ouro': 0.05, 'marrom': 0.01, 'vermelho': 0.02, 'verde': 0.005, 'azul': 0.0025, 'violeta': 0.001,'cinza': 0.0005, 'prata': 10}
        b = {'preto': 0, 'marrom': 1, 'vermelho': 2, 'laranja': 3, 'amarelo': 4, 'verde': 5, 'azul': 6, 'violeta': 7, 'cinza': 8, 'branco': 9}
        a = int(input('quantas faixas?: '))
        if a == 4:
            d = (((b[str(input('qual a primeira faixa?: '))]) * 10) + (b[str(input('qual a segunda faixa?: '))])) * (10 ** (b[str(input("Quantos zero na 3 faixa?: "))]))
            c = (dados[str(input("Qual é a faixa 4?:+- "))])
            print(f'a resistencia é {d}')
            print(f'o maximo é {d + (c * d)} o minimo é {d - (c * d)}')
        elif a == 5:
            d = (((b[str(input('qual a primeira faixa?: '))]) * 100) + (
            b[str(input('qual a segunda faixa?: '))]) * 10 + (b[str(input('qual a terceira faixa?: '))])) * (10 ** (b[str(input("Quantos zero na 3 faixa?: "))]))
            c = (dados[str(input("Qual é a faixa 4?:+- "))])
            print(f'a resistencia é {d}')
            print(f'o maximo é {d + (c * d)} o minimo é {d - (c * d)}')
        elif a == 6:
            d = (((b[str(input('qual é a cor da 1 faixa?: '))]) * 100) + (b[str(input('qual é a  cor da 2 faixa?: '))]) * 10 + (b[str(input('qual é a cor da 3 faixa?: '))])) * (
                            10 ** (b[str(input("Qual é a cor da 4 faixa?: "))]))
            c = (dados[str(input("Qual é a cor da 5 faixa?: "))])
            e = (dados2[str(input('qual a cor da 6 faixa?: '))])
            print(f'a resistencia é {d} {e}ppm/k')
>>>>>>> d99eec27de0c22293036b9d3a1faf5ce35cd4ec8
            print(f'o maximo é {d + (c * d)} o minimo é {d - (c * d)}')
