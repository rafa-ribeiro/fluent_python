
# Sequência mutável -> List
l = [1, 2, 3]
print(l)
print(id(l))

l *= 2
print(l)
print(id(l))


# Sequência Imutável -> Tuple
t = (1, 2, 3)
print(t)
print(id(t))

t *= 2
print(t)
print(id(t))


r = (1, 2, [30, 40])

r[2] += [50, 60]
print(r)
