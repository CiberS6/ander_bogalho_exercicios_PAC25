#exercício 1
def mostrar_pares(quantidade):
    for i in range(quantidade):
        print(f"{i+1}º par: {i * 2}")

def mostrar_impares(quantidade):
    for i in range(quantidade):
        print(f"{i+1}º ímpar: {i * 2 + 1}")

mostrar_pares(30)
print()
mostrar_impares(30)

#exercício 2
def par(numero):
    return numero % 2 == 0

def classificar_numeros(quantidade):
    for i in range(quantidade):
        numero = int(input(f"Insira o {i+1}º número: "))
        if par(numero):
            print(f"O número {numero} é par")
        else:
            print(f"O número {numero} é ímpar")

classificar_numeros(10)

#exercício 3
def ler_notas(quantidade):
    soma = 0
    for i in range(quantidade):
        nota = float(input(f"Insira a nota do {i+1}º aluno: "))
        soma = soma + nota
    return soma

def calcular_media(soma, quantidade):
    return soma / quantidade

soma_notas = ler_notas(10)
media = calcular_media(soma_notas, 10)
print(f"A média das notas é: {media}")

#exercício 4
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def verificar_primo():
    numero = int(input("Insira um número inteiro: "))
    if primo(numero):
        print(f"{numero} É número primo")
    else:
        print(f"{numero} Não é número primo")

verificar_primo()

#exercício 5
def mostrar_numeros(inicio, fim):
    for i in range(inicio, fim + 1):
        print(i, end=" ")

mostrar_numeros(1, 10000)

#exercício 6
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def mostrar_primos(quantidade):
    contador = 0
    numero = 2
    print(f"Os {quantidade} primeiros números primos são:")
    while contador < quantidade:
        if primo(numero):
            print(numero, end=" ")
            contador = contador + 1
        numero = numero + 1

mostrar_primos(10)

#exercício 7
def gerar_serie(inicio, fim, passo):
    for i in range(inicio, fim + 1, passo):
        print(i, end=" ")

gerar_serie(10, 1000, 10)

#exercício 8
def gerar_serie(inicio, fim, passo):
    for i in range(inicio, fim + 1, passo):
        print(i, end=" ")

print("Primeira série:")
gerar_serie(10, 1000, 10)
print("\n")
print("Segunda série:")
gerar_serie(15, 995, 10)

#exercício 9
def validar_intervalo(numero, minimo, maximo):
    return minimo <= numero <= maximo

def ler_numero_valido(minimo, maximo):
    while True:
        numero = int(input(f"Insira um número entre {minimo} e {maximo}: "))
        if validar_intervalo(numero, minimo, maximo):
            print(f"Número válido: {numero}")
            return numero
        else:
            print("Número inválido.")

ler_numero_valido(1, 100)

#exercício 10
def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def mostrar_divisores(numero):
    divisores = encontrar_divisores(numero)
    print(f"Divisores de {numero}:")
    for d in divisores:
        print(d, end=" ")
    print(f"\nTotal de divisores: {len(divisores)}")

numero = int(input("Insira um número: "))
mostrar_divisores(numero)

#exercício 11
def gerar_padrao(linhas):
    for i in range(1, linhas + 1):
        print(str(i) * i)

gerar_padrao(5)

#exercício 12
def somar(numero):
    total = 0
    for i in range(1, numero):
        total = total + i
    return total

def subtrair_todos(numero):
    total = numero
    for i in range(1, numero):
        total = total - i
    return total

def multiplicar_todos(numero):
    total = 1
    for i in range(1, numero):
        total = total * i
    return total

def dividir_todos(numero):
    total = numero
    for i in range(1, numero):
        total = total / i
    return total

def realizar_operacoes(numero):
    contador = 0
    for i in range(1, numero):
        print(f"{numero} + {i} = {numero + i} | {numero} - {i} = {numero - i} | {numero} × {i} = {numero * i} | {numero} ÷ {i} = {numero / i}")
        contador = contador + 4
    print(f"Total de operações efetuadas: {contador}")

numero = int(input("Insira um número: "))
realizar_operacoes(numero)

#exercício 13
def mostrar_tabuada(numero, inicio=1, fim=10):
    print(f"\nTabuada do {numero}")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} × {i} = {resultado}")

numero = int(input("Insira um número para ver a tabuada: "))
mostrar_tabuada(numero)

#exercício 14
def mostrar_tabuada(numero, inicio=1, fim=10):
    print(f"\nTabuada do {numero}")
    for i in range(inicio, fim + 1):
        print(f"{numero} × {i} = {numero * i}")

def mostrar_todas_tabuadas(de=1, ate=100):
    for num in range(de, ate + 1):
        mostrar_tabuada(num)

mostrar_todas_tabuadas(1, 100)

#exercício 15
def mostrar_codigo_ascii(codigo):
    print(f"Código {codigo:3} = {chr(codigo)}", end="   ")

def perguntar_continuacao():
    resposta = input("\nContinuar? (S/N): ").upper()
    return resposta != 'N'

def mostrar_tabela_ascii(inicio=0, fim=255, por_vez=20):
    for i in range(inicio, fim + 1):
        mostrar_codigo_ascii(i)
        if (i + 1) % por_vez == 0:
            print()
            if not perguntar_continuacao():
                print("Programa encerrado.")
                return
            print()
    print("\nTodos os códigos ASCII exibidos!")

mostrar_tabela_ascii()

#exercício 16
def par(numero):
    return numero % 2 == 0

def valido(numero, minimo, maximo):
    return minimo <= numero <= maximo

def ler_numero_par_valido(minimo, maximo, ordem):
    while True:
        numero = int(input(f"Insira o {ordem}º número par (entre {minimo} e {maximo}): "))
        if valido(numero, minimo, maximo) and par(numero):
            return numero
        print(f"Erro: Insira um número PAR entre {minimo} e {maximo}")

def calcular_media_lista(lista):
    return sum(lista) / len(lista)

def ler_numeros_pares(quantidade, minimo, maximo):
    numeros = []
    for i in range(quantidade):
        numero = ler_numero_par_valido(minimo, maximo, i + 1)
        numeros.append(numero)
    return numeros

numeros = ler_numeros_pares(30, 1, 50)
media = calcular_media_lista(numeros)
print(f"\nMédia dos 30 números pares: {media}")

#exercício 17
def multiplo(numero, divisor):
    return numero % divisor == 0

def encontrar_multiplos_exclusivos(inicio, fim, incluir, excluir):
    resultado = []
    for i in range(inicio, fim + 1):
        if multiplo(i, incluir) and not multiplo(i, excluir):
            resultado.append(i)
    return resultado

def mostrar_lista(lista, por_linha=15):
    for i, numero in enumerate(lista, 1):
        print(numero, end=" ")
        if i % por_linha == 0:
            print()
    print(f"\nTotal de números encontrados: {len(lista)}")

multiplos = encontrar_multiplos_exclusivos(1, 1000, 5, 3)
mostrar_lista(multiplos)

#exercício 18
def soma_divisores_proprios(numero):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + i
    return soma

def perfeito(numero):
    return soma_divisores_proprios(numero) == numero

def encontrar_perfeitos(limite):
    perfeitos = []
    for i in range(1, limite + 1):
        if perfeito(i):
            perfeitos.append(i)
    return perfeitos

def mostrar_perfeitos(limite):
    perfeitos = encontrar_perfeitos(limite)
    print(f"\nNúmeros perfeitos até {limite}:")
    for p in perfeitos:
        print(p, end=" ")
    print(f"\nTotal de números perfeitos encontrados: {len(perfeitos)}")

limite = int(input("Insira até qual número procurar números perfeitos: "))
mostrar_perfeitos(limite)

#exercício 19
def gerar_fibonacci(quantidade):
    if quantidade == 0:
        return []
    if quantidade == 1:
        return [1]
    fibonacci = [1, 1]
    for i in range(2, quantidade):
        proximo = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(proximo)
    return fibonacci

def mostrar_fibonacci(quantidade, por_linha=10):
    sequencia = gerar_fibonacci(quantidade)
    print(f"Os {quantidade} primeiros números de Fibonacci:")
    for i, num in enumerate(sequencia, 1):
        print(num, end=" ")
        if i % por_linha == 0:
            print()

mostrar_fibonacci(60)

#Teste Final 1

def validar_entrada(minimo, maximo):
    while True:
        try:
            valor = int(input(f"Insira um valor entre {minimo} e {maximo}: "))
            if minimo <= valor <= maximo:
                return valor
            print(f"Erro: Valor deve estar entre {minimo} e {maximo}")
        except ValueError:
            print("Erro: Insira um número válido")

def perguntar_continuar(mensagem="Continuar? (S/N): "):
    resposta = input(mensagem).upper()
    return resposta != 'N'

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def contar_divisores(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador = contador + 1
    return contador

def perfeito(numero):
    if numero < 2:
        return False
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + i
    return soma == numero

def analisar_numero(numero):
    primo = "Sim" if primo(numero) else "Não"
    divisores = contar_divisores(numero)
    perfeito = "Sim" if perfeito(numero) else "Não"
    return primo, divisores, perfeito

def mostrar_analise_numeros():
    print("\n Análise de Números")
    valor = validar_entrada(1, 30000)
    
    contador = 0
    for i in range(valor, 0, -1):
        primo, divisores, perfeito = analisar_numero(i)
        print(f"{i:5} | Primo: {primo:3} | Divisores: {divisores:3} | Perfeito: {perfeito:3}")
        contador = contador + 1
        
        if contador % 10 == 0:
            print()
            if not perguntar_continuar():
                print("Análise interrompida.")
                return
            print()
    
    print("\nAnálise concluída")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def calculadora():
    num1 = float(input("Insira o primeiro número: "))
    operador = input("Insira a operação (+, -, *, /): ")
    num2 = float(input("Insira o segundo número: "))
    
    if operador == '+':
        resultado = somar(num1, num2)
    elif operador == '-':
        resultado = subtrair(num1, num2)
    elif operador == '*':
        resultado = multiplicar(num1, num2)
    elif operador == '/':
        resultado = dividir(num1, num2)
    else:
        resultado = "Operação inválida"
    
    print(f"Resultado: {resultado}")

def mostrar_tabuada_completa(maximo):
    print(f"\nTabuada completa até {maximo}")
    contador = 0
    
    for num in range(1, maximo + 1):
        for i in range(1, maximo + 1):
            print(f"{num} × {i} = {num * i}")
            contador = contador + 1
            
            if contador % 20 == 0:
                print()
                if not perguntar_continuar():
                    print("Tabuada interrompida.")
                    return
                print()
    
    print(f"\nTabuada completa. Total de operações: {contador}")

def menu_tabuada():
    maximo = validar_entrada(1, 1000)
    mostrar_tabuada_completa(maximo)

def menu_principal():
    while True:
        print("1 - Análise de Números")
        print("2 - Calculadora")
        print("3 - Tabuada")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            mostrar_analise_numeros()
        elif opcao == '2':
            calculadora()
        elif opcao == '3':
            menu_tabuada()
        elif opcao == '0':
            return
        else:
            print("Opção inválida")

menu_principal()

#Teste Final 2

clientes = []
proximo_numero_cliente = 1

def validar_texto(campo, minimo=1):
    while True:
        valor = input(f"Insira {campo}: ").strip()
        if len(valor) >= minimo:
            return valor
        print(f"Erro: {campo} deve ter pelo menos {minimo} caractere(s)")

def validar_telefone():
    while True:
        telefone = input("Insira o telefone: ").strip()
        if telefone.isdigit() and len(telefone) >= 9:
            return telefone
        print("Erro: Telefone deve ter pelo menos 9 dígitos")

def validar_nif():
    while True:
        nif = input("Insira o NIF: ").strip()
        if nif.isdigit() and len(nif) == 9:
            return nif
        print("Erro: NIF deve ter exatamente 9 dígitos")

def validar_compra():
    while True:
        try:
            compra = float(input("Insira o valor da compra: "))
            if compra >= 0:
                return compra
            print("Erro: Valor deve ser positivo")
        except ValueError:
            print("Erro: Insira um valor numérico")

def calcular_desconto(compra):
    if compra < 100:
        return 0
    elif compra <= 200:
        return compra * 0.05
    elif compra < 500:
        return compra * 0.10
    else:
        return compra * 0.15

def calcular_divida_final(compra):
    desconto = calcular_desconto(compra)
    return compra - desconto

def inserir_cliente():
    global proximo_numero_cliente
    
    print("\nInserir Cliente")
    
    nome = validar_texto("o nome")
    morada = validar_texto("a morada")
    telefone = validar_telefone()
    nif = validar_nif()
    compra = validar_compra()
    divida_final = calcular_divida_final(compra)
    desconto = calcular_desconto(compra)
    
    cliente = {
        'numcli': proximo_numero_cliente,
        'nomcli': nome,
        'morada': morada,
        'tel': telefone,
        'nif': nif,
        'compra': compra,
        'desconto': desconto,
        'divfin': divida_final
    }
    
    clientes.append(cliente)
    print(f"\nCliente {proximo_numero_cliente} inserido com sucesso!")
    print(f"Desconto aplicado: {desconto:.2f}€")
    print(f"Dívida final: {divida_final:.2f}€")
    
    proximo_numero_cliente = proximo_numero_cliente + 1

def mostrar_cliente(cliente):
    print("\n" + "-"*40)
    print(f"Número Cliente: {cliente['numcli']}")
    print(f"Nome: {cliente['nomcli']}")
    print(f"Morada: {cliente['morada']}")
    print(f"Telefone: {cliente['tel']}")
    print(f"NIF: {cliente['nif']}")
    print(f"Compra: {cliente['compra']:.2f}€")
    print(f"Desconto: {cliente['desconto']:.2f}€")
    print(f"Dívida Final: {cliente['divfin']:.2f}€")
    print("-"*40)

def perguntar_continuar(mensagem="Continuar? (S/N): "):
    resposta = input(mensagem).upper()
    return resposta != 'N'

def listar_clientes():
    if not clientes:
        print("\nNão existem clientes registados.")
        return
    
    print("\nListar Clientes")
    
    for cliente in clientes:
        mostrar_cliente(cliente)
        if not perguntar_continuar("Prima Enter para continuar (N para sair): "):
            return
    
    print("\nFim da listagem.")

def buscar_cliente():
    if not clientes:
        print("\nNão existem clientes registados.")
        return
    
    print("\nBuscar Cliente")
    try:
        numero = int(input("Insira o número do cliente: "))
        for cliente in clientes:
            if cliente['numcli'] == numero:
                mostrar_cliente(cliente)
                return
        print(f"Cliente {numero} não encontrado.")
    except ValueError:
        print("Erro: Insira um número válido")

def total_clientes():
    return len(clientes)

def total_dividas():
    total = 0
    for cliente in clientes:
        total = total + cliente['divfin']
    return total

def estatisticas():
    print("\nEstatísticas")
    print(f"Total de clientes: {total_clientes()}")
    print(f"Total de dívidas: {total_dividas():.2f}€")

def menu_clientes():
    while True:
        print("    Base de Dados Clientes")
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Buscar Cliente")
        print("4 - Estatísticas")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            inserir_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            buscar_cliente()
        elif opcao == '4':
            estatisticas()
        elif opcao == '0':
            print("Programa encerrado.")
            return
        else:
            print("Opção inválida!")

menu_clientes()