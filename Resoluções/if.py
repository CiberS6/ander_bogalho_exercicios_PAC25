#exercício 1
segundos = int(input("Insira o tempo em segundos: "))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos_restantes = resto % 60
print(f"{horas} hora, {minutos} minuto e {segundos_restantes} segundos")

#exercício 2
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"Maior: {maior}")
print(f"Menor: {menor}")

#exercício 3
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 < num2:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
else:
    print(f"Crescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")

#exercício 4
saldo = float(input("Insira o saldo inicial: "))
cheque = float(input("Insira o valor do cheque: "))

if cheque <= saldo:
    saldo = saldo - cheque
    print(f"Cheque descontado, saldo: {saldo}")
else:
    print("Cheque não pode ser descontado. Saldo insuficiente.")

#exercício 5
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        meio = num1
        maior = num2
    else:
        meio = num2
        maior = num1

print(f"Crescente: {menor}, {meio}, {maior}")
print(f"Decrescente: {maior}, {meio}, {menor}")

#exercício 6
nome = input("Insira o nome do cliente: ")
compra = float(input("Insira o valor da compra: "))

if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

total = compra - desconto

print(f"Nome: {nome}")
print(f"Compra: {compra}€")
print(f"Desconto: {desconto}€")
print(f"Total a pagar: {total}€")

#exercício 7
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
print(f"Média: {media}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#exercício 8
notas = []

for i in range(10):
    nota = float(input(f"Insira a nota do aluno {i+1}: "))
    notas.append(nota)

soma = 0

for nota in notas:
    soma = soma + nota

media = soma / 10
acima_media = 0

for nota in notas:
    if nota >= media:
        acima_media = acima_media + 1

print(f"Média: {media}")
print(f"Alunos com a nota igual ou acima da média: {acima_media}")

#exercício switch
mes = int(input("Insira um número de 1 a 12: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Erro: Número inválido. Insira um número de 1 a 12.")

#exercício loop
pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Insira o {i+1}º número: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")