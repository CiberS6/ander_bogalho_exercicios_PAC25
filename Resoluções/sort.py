# exercício 1
palavras = ["banana", "uva", "abacaxi", "laranja"]

n = len(palavras)
for i in range(n):
    for j in range(0, n - i - 1):
        if palavras[j] > palavras[j + 1]:
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print(palavras)

# exercício 2
palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

n = len(palavras)
for i in range(n):
    for j in range(0, n - i - 1):
        if palavras[j].lower() < palavras[j + 1].lower():
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print(palavras)

# exercício 3
palavra = "algoritmo"
letras = list(palavra)

n = len(letras)
for i in range(n):
    for j in range(0, n - i - 1):
        if ord(letras[j]) > ord(letras[j + 1]):
            letras[j], letras[j + 1] = letras[j + 1], letras[j]

resultado = "".join(letras)
print(resultado)

# exercício 4
palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contar_minusculas(p):
    count = 0
    for char in p:
        if 'a' <= char <= 'z':
            count += 1
    return count

n = len(palavras)
for i in range(n):
    for j in range(0, n - i - 1):
        if contar_minusculas(palavras[j]) > contar_minusculas(palavras[j + 1]):
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print(palavras)

# exercício 5
palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
grupos = {}

# Agrupamento
for p in palavras:
    inicial = p[0]
    if inicial not in grupos:
        grupos[inicial] = []
    grupos[inicial].append(p)

# Ordenação manual de cada grupo
for letra in grupos:
    lista = grupos[letra]
    n_lista = len(lista)
    for i in range(n_lista):
        for j in range(0, n_lista - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(grupos)
