def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')


# def somar(a=0, b=0, c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: O primeiro valor
#     :param b: O segundo valor
#     :param c: O terceiro valor
#     :return: not return
#     """
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(2, 7)
# r3 = somar(4)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}.')


# def função(b):
#     global a
#     a = 4
#     b += 4
#     c = 2
#     print(f'A dentro recebe {a}')
#     print(f'B dentro recebe {b}')
#     print(f'C dentro recebe {c}')
#
#
# a = 2
# função(a)
# print(f'A fora recebe {a}')

# def somar(a=0, b=0, c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: O primeiro valor
#     :param b: O segundo valor
#     :param c: O terceiro valor
#     :return: not return
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
#
# somar(2, 3)
