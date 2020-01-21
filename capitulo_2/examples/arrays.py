from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))

print(floats[-1])  # Acessa o último elemento de floats

fp = open('floats.bin', 'wb')
floats.tofile(fp)  # Salva o array em um arquivo binário
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)  # Lê os dez milhões de números do arquivo
fp.close()
print(floats2[-1])

