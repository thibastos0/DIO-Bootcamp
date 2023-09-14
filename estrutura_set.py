# criando conjuntos

lista = [1, 2, 3, 1, 3, 4]

conjunto_numero = set(lista)
print(conjunto_numero)

conjunto_letras = set("abacaxi")
print(conjunto_letras)

conjunto_carros = set(("palio", "gol", "celta", "palio",))
print(conjunto_carros)

linguagens = {"python", "java", "python"}
print(linguagens) # remove valor duplicado

# acessando os dados
# é necessário converter o set para list

numeros = {1, 2, 3, 2}

# print(numeros[0]) -> não é possível acessar o set diretamente

numeros = list(numeros) # convertendo para lista

print(numeros[0]) # agora é possível acessar

# iteração é possível

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# Usando a função enumerate()

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

