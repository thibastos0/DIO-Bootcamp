
# Criação
frutas = []
print(frutas)

frutas = ["maca", "laranja", "uva", "pera"]
print(frutas)

letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

# Acesso direto

print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-3])

# Listas aninhadas

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# Fatiamento

letra_curso = ["p", "y", "t", "h", "o", "n"]

print(letra_curso[2:])
print(letra_curso[:2])
print(letra_curso[1:3])
print(letra_curso[0:3:2])
print(letra_curso[::])
print(letra_curso[::-1])

# Iterar listas
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Usando a função enumerate()

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de listas

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

impares = [numero for numero in numeros if numero % 2 != 0]

print(impares)

# modificando os valores

quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

print(quadrado)

dobro = [numero*2 for numero in numeros]

print(dobro)

