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