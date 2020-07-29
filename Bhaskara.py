#!/bin/env python3.7
#
# Projeto: Bhaskara
# Autor: Mac Brener - Askaryd
# Data: 24/07/2020
#

print('Programa para calcular equações do 2º Grau.\n')
print('Estrutura da função do segundo grau: \nax² + bx + c = 0\n')

try:
    try:
        a = float(input('Digite o valor de a: '))
        b = float(input('Digite o valor de b: '))
        c = float(input('Digite o valor de c: '))

    except ValueError:
        print('\nDigite somente números reais.')
        exit(1)

    delta = ((b) ** 2) + ((-4) * (a) * (c))
    x_positivo = (b * (-1) + delta ** (1 / 2)) / (2 * a)
    x_negativo = (b * (-1) - delta ** (1 / 2)) / (2 * a)

except ZeroDivisionError:
    x = int((c) * (-1) / (b))
    print('\nx = {}'.format(x))
    exit(0)

print('\nEquação: {}x² {}x {} = 0'.format(a, b, c))

if b == 0 and c == 0:
    print('\nNão existem raízes reais.')
    exit(0)

if delta > 0:
    print('''
    Valor de Delta: {}\n
    Possui duas raízes reais distintas.\n
    x' = {:.2f}
    x" = {:.2f}'''.format(delta, x_positivo, x_negativo))

elif delta == 0:
    print('''
    Valor de Delta: {}\n
    Possui duas raízes reais iguais.\n
    x' = x" = {:.2f}'''.format(delta, x_positivo))

elif delta < 0:
    print('''\
    Não possui raízes reais.
    x = 0''')
