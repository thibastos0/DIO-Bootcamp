while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)

print() #pular linha

for numero in range(100):
    if numero == 12:
        break

    print(numero, end=' ')

print() #pular linha

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=' ')

print() #pular linha