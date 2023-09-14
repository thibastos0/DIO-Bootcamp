nome = "ThiAGo"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "         Olá mundo!  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

curso = "Python"

print("####" + curso + "####")
print(curso.center(14))
print(curso.center(20, "#"))

print("P-y-t-h-o-n")
print("-".join(curso))

for contador, letra  in enumerate(curso):
    print(letra, end="")
    if contador == len(curso) -1:
        break
    print("-", end="")
    
