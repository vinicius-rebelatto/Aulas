estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[0]['uf'])

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

# pessoas['peso'] = 98.5

# del pessoas['sexo']

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# print('-=' * 15)

# for k in pessoas.keys():
#     print(k)
# print('-=' * 15)
# for v in pessoas.values():
#     print(v)
# print('-=' * 15)
# for i in pessoas.items():
#     print(i)

# for k, v in pessoas.items():
#     print(f'{k} = {v}')
