# copy
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovana", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

copia = contatos.copy()

copia["guilherme@gmail.com"] = {"nome": "Gui"}
copia["giovanna@gmail.com"] = {"nome": "Giovanna"}

print(contatos["guilherme@gmail.com"])
print(copia["guilherme@gmail.com"])
print(contatos["giovanna@gmail.com"])
print(copia["giovanna@gmail.com"])


# clear

copia.clear()

print(copia)

# fromkeys

contatos2 = {}

contatos2 = dict.fromkeys(["nome", "telefone"])
print(contatos2)

contatos2 = dict.fromkeys(["nome", "telefone"], "vazio")
print(contatos2)

contatos2.fromkeys(["nome", "telefone"], "não funciona")
print(contatos2)

# get, quando não tem certeza se a chave existe.

# print(contatos["chave"]) RETONA KEYERROR

print(contatos.get("chave"))

print(contatos.get("chave", {})) # valor default, caso a chave não exista.

print(contatos.get("guilherme@gmail.com", {}))

# items - lista de tuplas. Útil no comando for

print(contatos.items())

print(30*'=')

# keys - para descobrir as chaves do dicionáiro

resultado = contatos.keys()
print(resultado)

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())

# pop

copia = contatos.copy()

resultado = copia.pop("guilherme@gmail.com")
print(resultado)

resultado = copia.pop("guilherme@gmail.com", {}) # retorna {} porque não encontrou mais a chave. Se não colocar valor padrão irá dar erro.
print(resultado)

# popitem para retirar os itens na sequência. se estiver vazio o dict retorna um erro.

resultado = copia.popitem()
print(resultado)
resultado = copia.popitem()
print(resultado)
resultado = copia.popitem()
print(resultado)
# resultado = copia.popitem() -> dicionário está vazio
# print(resultado)

# setdefault

copia = contatos.copy()
print(50*'=')
copia["giovanna@gmail.com"].setdefault("nome", "Giovana") # não faz nada porque a chave nome já existe
print(copia)
print(50*'=')
copia["giovanna@gmail.com"].setdefault("idade", 28) # adiciona a chave idade com valor default
print(copia)

print() # pulando linha
# update

contatos.update({"guilherme@gmail.com": {"nome": "Gui", "telefone": "3333-2221"}}) # caso a chave exista, atualiza
print(contatos)
print(50*'=')
contatos.update({"thibastos@email.com": {"nome": "Thiago", "telefone": "5555-5555"}}) # caso a chave não exista, é inserido novo item
print(contatos)

# values - retona apenas os valores, sem chaeves.

print() #pula linha
print(contatos)

# in

resultado = "guilherme@gmail.com" in contatos
print(resultado)

resultado = "megu@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]
print(resultado)

# del

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos)

cont = {"idioma": "pt-br", "pais": "Brasil"}
print(cont["pais"])