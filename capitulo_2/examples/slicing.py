s = 'bicycle'
print(s[::3])

print(s[::-1])

print(s[::-2])

print(s[2::2])

# s[a:b:c]
# Em que:
# - a -> É o indíce de start
# - b -> É o indíce de stop
# - c -> É o salto ou pulo que o fatiamento usará


l = list(range(10))
print(l)

l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

# A partir do indíce 3, substitui andando de 2 em 2 indíces
l[3::2] = [11, 22]
print(l)

l[2:5] = [100]
print(l)
