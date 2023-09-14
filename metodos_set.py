# union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

# intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

# difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# symmetric_difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))

# issubset (subconjunto / está contido)

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))


# isssuperset (o contrário de subconjunto / contém)

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# isdisjoint (não tem interseção)

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

# add

sorteio = {1, 23}
print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25)
print(sorteio) # repetido é ignorado

# copy

sorteio2 = sorteio.copy()
print(sorteio2)
print(id(sorteio), id(sorteio2))

# clear

sorteio2.clear()
print(sorteio2)

# discard

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)
numeros.discard(1)
numeros.discard(45) #não dá erro
print(numeros)

# pop

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.pop())
print(numeros.pop())
# print(numeros.pop(3)) não é possível definir o valor que quer retirar
print(numeros)

# remove

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
numeros.remove(0)
# print(numeros.remove(45)) -> erro, porque o valor não existe
print(numeros)

# len

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))

# in

print(1 in numeros)
print(10 in numeros)