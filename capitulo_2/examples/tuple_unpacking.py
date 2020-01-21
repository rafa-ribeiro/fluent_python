import os


# Desempacotando a tupla nas variáveis
city, year, pop, chg, area = ('São Paulo', '2019', '2000000', '0.66', '10000')


traveler_ids = [('USA', '356781'), ('BRA', '231459'), ('ESP', '461637')]

# Desempacotando a tupla nas variáveis do for, a tupla que não vou utilizar vai para "_"
for country, _ in traveler_ids:
    print(country)

for _, country_id in traveler_ids:
    print(country_id)


# função split do os retorna uma tupla com (path, lastpath)
_, filename = os.path.split('/home/rafael/workspace/teste.py')
print(filename)


# Desempacotamento de tupla com atribuição paralela:
a, b, *rest = range(10)
print(a, b, rest)

print(f"rest SEM o asterisco é do tipo {type(rest)}")

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)
