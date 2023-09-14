frutas = ("laranja", "pera", "uva",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple ([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

# acessar os valores

print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-3])

# matriz
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# fatiamento

tupla = ("p","y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

# iteração

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

# Usando a função enumerate()

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")