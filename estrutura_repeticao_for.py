texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #quebra de linha
    print("Executa no final do laço.")

    #ver min 13 do vídeo.