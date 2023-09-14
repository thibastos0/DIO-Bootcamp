nome = "Thiago"
idade = 41
profissao = "ATCO"
linguagem = "Python"
saldo = 45.435

dados = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem}

# não é muito utilizado
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

#utilizando format
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {name}. Eu tenho {age} anos de idade, trabalho com {occupation} e estou matriculado no curso de {language}.".format(name=nome, age=idade, occupation=profissao, language=linguagem))

print("Usando dicionário:")
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(**dados))

# formato mais atual
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI:{PI:10.2f}") #10 -> espaços em branco.

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

print(f"Saldo: {saldo:.2f}")
print(f"Saldo: {saldo:10.1f}")