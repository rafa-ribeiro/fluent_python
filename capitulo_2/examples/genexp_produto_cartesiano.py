# Exemplo de utilização de Expressão geradora para aplicar um produto cartesiano de duas listas.
# A vantagem da genexp em relação a uma listcomps, por exemplo, é que a listcomp itera as duas listas gerando a terceira
# lista em memória que é do tamanho da len(lista_1) x len(list_2).

# Ao usar a genexp, o for que itera sobre tshirt é alimentado a partir da expressão geradora, assim como não precisamos
# criar uma terceira lista e armazenar em memória, a genexp se torna mais adequada nesse caso por evitar armazenamento
# desnecessário em memória.


colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in (f"({c}, {s})" for c in colors for s in sizes):
    print(tshirt)
