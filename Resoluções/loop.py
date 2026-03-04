#exercício 1
for i in range(30):
    print(f"{i+1}º par: {i * 2}")
print()
for i in range(30):
    print(f"{i+1}º ímpar: {i * 2 + 1}")

#exercício 2
for i in range(10):
    numero = int(input(f"Insira o {i+1}º número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

#exercício 3
soma = 0

for i in range(10):
    nota = float(input(f"Insira a nota do {i+1}º aluno: "))
    soma = soma + nota

media = soma / 10
print(f"A média das notas é: {media}")

#exercício 4
numero = int(input("Insira um número inteiro: "))

if numero < 2:
    print(f"{numero} Não é número primo")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"{numero} É número primo")
    else:
        print(f"{numero} Não é número primo")

#exercício 5
for i in range(1, 10001):
    print(i, end=" ")

#exercício 6
def nprimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

contador = 0
numero = 2

print("Os 10 primeiros números primos são:")
while contador < 10:
    if nprimo(numero):
        print(numero, end=" ")
        contador = contador + 1
    numero = numero + 1

#exercício 7
for i in range(10, 1001, 10):
    print(i, end=" " if i < 1000 else "\n")

#exercício 8
for i in range(10, 1001, 10):
    print(i, end=" ")
print("\n")

for i in range(15, 1000, 10):
    print(i, end=" ")
#exercício 9
while True:
    numero = int(input("Insira um número entre 1 e 100: "))
    if 1 <= numero <= 100:
        print(f"Número válido: {numero}")
        break
    else:
        print("Número inválido.")

#exercício 10
numero = int(input("Insira um número: "))
contador = 0

print(f"Divisores de {numero}:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i, end=" ")
        contador = contador + 1

print(f"\nTotal de divisores: {contador}")

#exercício 11
for i in range(1, 6):
    print(str(i) * i)

#exercício 12
numero = int(input("Insira um número: "))
soma_total = 0
sub_total = numero
mult_total = 1
div_total = numero
contador = 0

for i in range(1, numero):
    soma_total = soma_total + i
    sub_total = sub_total - i
    mult_total = mult_total * i
    div_total = div_total / i
    contador = contador + 4  # 4 operações por iteração
    print(f"{numero} + {i} = {numero + i} | {numero} - {i} = {numero - i} | {numero} × {i} = {numero * i} | {numero} ÷ {i} = {numero / i}")

print(f"Total de operações efetuadas: {contador}")

#exercício 13
numero = int(input("Insira um número para ver a tabuada: "))

print(f"\nTabuada do {numero} ")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i} = {resultado}")

#exercício 14
for numero in range(1, 101):
    print(f"\nTabuada do {numero}")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")

#exercício 15
for i in range(0, 256):
    print(f"Código {i:3} = {chr(i)}", end="   ")
    if (i + 1) % 20 == 0:
        print()
        resposta = input("\nContinuar? (S/N): ").upper()
        if resposta == 'N':
            print("Programa encerrado.")
            break
        print()
else:
    print("\nTodos os 256 códigos ASCII exibidos!")

#exercício 16
soma = 0
contador = 0

while contador < 30:
    numero = int(input(f"Insira o {contador+1}º número par (entre 1 e 50): "))
    if 1 <= numero <= 50 and numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
    else:
        print("Erro: Insira um número PAR entre 1 e 50")

media = soma / 30
print(f"\nMédia dos 30 números pares: {media}")

#exercício 17
contador = 0

for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
        print(i, end=" ")
        contador = contador + 1
        if contador % 15 == 0:
            print()

print(f"\nTotal de números encontrados: {contador}")

#exercício 18
limite = int(input("Insira até qual número procurar números perfeitos: "))
def nperfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i
    return soma == n

contador = 0

print(f"\nNúmeros perfeitos até {limite}:")

for i in range(1, limite + 1):
    if nperfeito(i):
        print(i, end=" ")
        contador = contador + 1

print(f"\nTotal de números perfeitos encontrados: {contador}")

#exercício 19
a = 1
b = 1

print(a, end=" ")
print(b, end=" ")

for i in range(58):
    proximo = a + b
    print(proximo, end=" ")
    a = b
    b = proximo
    if (i + 3) % 10 == 0:
        print()
