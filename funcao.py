# declarando funções com e sem parâmetros

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Thiago")
exibir_mensagem_2("Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

# retornando valores
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero +1

    return antecessor, sucessor # retorno em tupla. Valor imutável.

def func_3():
    print("Olá munndo")

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3()) #retun NONE

# argumento nomeado

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1B34")
# salvar_carro("Palio", 1999, "Fiat", "ABC-1B34") -> bagunça
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1B34")
# salvar_carro(modelo="Palio", marca="Fiat", ano=1999, placa="ABC-1B34") -> não bagunça
salvar_carro(**{"modelo": "Palio", "marca": "Fiat", "ano": 1999, "placa": "ABC-1B34"})

# Args e kargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"\n{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 15 de Setembro de 2023.",
    "Zen of Python", 
    "Beatiful is better than ugly.", 
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one—and preferably only one—obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea—let's do more of those!",
    autor="Tim Peter", ano=1999)

# parâmetros especais
# position only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"Carro inserido com sucesso! {modelo}/{ano}/{placa}/{marca}/{motor}/{combustivel}")

criar_carro("Palio", 1999, "ABC-1B34", marca="Fiat", motor="1.0", combustivel="Gasolina")
# a função abaixo também funciona, sem erro, porque não é obrigatório. Keyword é opcional
criar_carro("Palio", 1999, "ABC-1B34", "Fiat", "1.0", "Gasolina")
# a função abaixo não funciona, porque não é possível passar com keyword argumentos definido como "por posição".
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1B34", marca="Fiat", motor="1.0", combustivel="Gasolina")

# parâmetros especais
# keyword only

def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(f"Carro inserido com sucesso! {modelo}/{ano}/{placa}/{marca}/{motor}/{combustivel}")

criar_carro2(modelo="Celta", ano=2000, placa="DEF-1D34", marca="Chevrolet", motor="1.0", combustivel="Gasolina")

# a função abaixo retorna erro por não ter usado keyword
# criar_carro2("Celta", 2000, "DEF-1D34", "Chevrolet", "1.0", "Gasolina")

# parâmetros especais
# híbrido

def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(f"Carro inserido com sucesso! {modelo}/{ano}/{placa}/{marca}/{motor}/{combustivel}")

criar_carro3("Palio", 1999, "ABC-1B34", marca="Fiat", motor="1.0", combustivel="Gasolina")
# função abaixo não funciona, porque argumento por posição é obrigatório antes "/"
# criar_carro3(modelo="Palio", ano=1999, placa="ABC-1B34", marca="Fiat", motor="1.0", combustivel="Gasolina")

def criar_carro4(modelo, ano, /, placa, marca, *, motor, combustivel):
    print(f"Carro inserido com sucesso! {modelo}/{ano}/{placa}/{marca}/{motor}/{combustivel}")

# placa e marca estão entre "/" e "*" e ficaram opcionais (por posição ou keyword)
criar_carro4("Celta", 2000, placa="DEF-1D34", marca="Chevrolet", motor="1.0", combustivel="Gasolina")
# uma vez definido por posição ou keyword, todos os argumentos entre "/" e "*" devem seguir a mesma regra
criar_carro4("Celta", 2000, "DEF-1D34", "Chevrolet", motor="1.0", combustivel="Gasolina")

# objetos de primeira classe - é possível atribuir funções a variáveis, passá-las como parâmetro para outras funções, usá-las como valores em estruturas de dados (lista, tupla etc.) e usar como valor de retorno para uma função (closures)
print(40*"=") 

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def exibir_resultado(a, b, funcao, operacao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} {operacao} {b} = {resultado}")

exibir_resultado(10, 10, somar, "+") #funcão passada como argumento
exibir_resultado(10, 10, subtrair, "-")

op = somar # função atribuída como variável
print(op(1,23))

# escopo local e escopo global - NÃO É UMA BOA PRÁTICA

salario = 2000

def salario_bonus(bonus, lista):
    global salario # se comentar essa linha, teremos um erro na execução

    copia = lista.copy() # não altera
    copia.append(10)
    
    lista.append(2) # altera por causa da referência na memória

    print(f"lista copia = {copia}")
    print(f"lista na funcao = {lista}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista) #2500
print(salario_com_bonus)
print(f"lista fora da funcao = {lista}")