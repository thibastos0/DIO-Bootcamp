# append()

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

# clear()

lista.clear()

print(lista)

# copy()

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

# count()

print("=================================")

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# extend()

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print (linguagens)

# index() - retorna índice da primeira ocorrência encontrada.

linguagens = ["python", "java", "c", "java", "csharp"]

print(linguagens.index("java")) 
print(linguagens.index("python"))

# pop ()

linguagens.pop()
linguagens.pop()
linguagens.pop()
linguagens.pop(0)

print(linguagens) # sobra só "java"

# remove() - remove a primeira ocorrência encontrada.

linguagens = ["python", "js", "c", "java", "c"]

linguagens.remove("c")

print(linguagens)

# reverse

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)

# sort()

linguagens = ["python", "js", "c", "java", "csharp"]

l1 = linguagens.copy()
l2 = linguagens.copy()
l3 = linguagens.copy()
l4 = linguagens.copy()

l1.sort()
print("l1: ", l1)

l2.sort(reverse=True)
print("l2: ", l2)

l3.sort(key=lambda x:len(x))
print("l3: ", l3)

l4.sort(key=lambda x: len(x), reverse=True)
print("l4: ", l4)

# len()

print(len(linguagens))

# sorted()

print("sorted tamanho: ", sorted(linguagens, key=lambda x: len(x)))

print("sorted tamanho e invertido: ", sorted(linguagens, key=lambda x: len(x), reverse=True))

print("sorted sem firula: ", sorted(linguagens))
