def soma(* numeros):
    s = 0
    for n in numeros:
        s += n
    print(f'A soma dos valores {numeros } temos {s}')


soma(5, 4)
soma(2, 9, 4)


# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
#
# valores = [5, 9, 3, 4, 1, 6]
# dobra(valores)
# print(valores)

# def contador(*num):
#     for n in num:
#         print(f'{n} ', end='')
#     print('Fim!')
#
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(3, 6, 6, 2, 4)


# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B é igual à {s}')
#
#
# soma(b=1, a=2)
# soma(4, 5)
# soma(8, 9)


def titulo(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


titulo('CURSO EM VÍDEO')
titulo('OI')
titulo('CURSO PYTHON')
