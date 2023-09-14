# criando dics

pessoa1 = {"nome": "Thiago", "idade": 41}

pessoa2 = dict(nome="Guilherme", idade=28)

pessoa1["telefone"] = "3333-1234"

print(pessoa1)
print(pessoa2)

# acessando valores
print(pessoa1["nome"])
print(pessoa1["idade"])
print(pessoa1["telefone"])

pessoa1["nome"] = "Maria"
pessoa1["idade"] = 18
pessoa1["telefone"] = "9988-1781"

print(pessoa1)

# dicionários aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovana", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}

print(contatos["giovanna@gmail.com"]["telefone"])
print(contatos["melaine@gmail.com"]["extra"]["a"])

# iterar dicionários

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)