#exercício 1
alunos = [
    {"nome": "Maria", "idade": 20, "curso": "Engenharia"},
    {"nome": "Pedro", "idade": 22, "curso": "Informática"},
    {"nome": "Ana",   "idade": 19, "curso": "Medicina"}
]

for aluno in alunos:
    print(f"nome: {aluno['nome']}")
    print(f"idade: {aluno['idade']}")
    print(f"curso: {aluno['curso']}")

#exercício 2
carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}

print(carro['modelo'])
print(carro.get('modelo'))

#exercício 3
produto = {}

produto["nome"] = "Telemóvel"
produto["preço"] = 1500
produto["stock"] = 30

del produto["stock"]
print(produto)

#exercício 4
utilizador = {'nome': 'Carlos', 'idade': 28}

if "email" in utilizador:
    print("Email encontrado:", utilizador["email"])
else:
    print("Email não encontrado.")

#exercício 5
palavra = input("Insira uma palavra: ").lower()
contagem = {}

for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)

#exercício 6
vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
total = sum(vendas.values())

print(f"Total de vendas do trimestre: {total}")

#exercício 7
d = {'a': 1, 'b': 2, 'c': 3}
invertido = {}

for chave, valor in d.items():
    invertido[valor] = chave

print(invertido)

#exercício 8
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

combinado = d1.copy()
combinado.update(d2)
print(combinado)

#exercício 9
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for aluno, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{aluno}: {media:.1f}")

#exercício 10
frase = input("Insira uma frase: ").lower()
palavras = frase.split()

contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)

