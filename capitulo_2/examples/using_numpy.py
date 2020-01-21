import numpy  # Necessário instalação: Linux -> sudo apt-get install python-numpy python-scipy

a = numpy.arange(12)  # Inicializa a com inteiro de 0 a 11

type(a)

a.shape()
# Retorna (12, ) -> Indica que é um array de 1 dimensão contendo 12 elementos


a.shape = 3, 4
# Altera a estrutura de a -> Agora a possui duas dimensões, 3x4, 3 linhas e 4 colunas


a[:, 1]  # Obtém um array contendo todos os elementos da coluna 1


a.transpose()