#exercício 1
dia = input("Insira o dia da semana: ").lower()

match dia:
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case _:
        print("Dia inválido")

#exercício 2

nota = int(input("Insira a nota (0-100): "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Bom")
    case n if n >= 50:
        print("Suficiente")
    case _:
        print("Insuficiente")

#exercício 3
pedido = {"tipo": "venda", "valor": 250}

match pedido:
    case {"tipo": "compra", "valor": v}:
        print(f"Compra de {v}€")
    case {"tipo": "venda", "valor": v}:
        print(f"Venda de {v}€")
    case _:
        print("Pedido desconhecido")

#exercício 4
valor = [10, 20, 30]  # Valor a ser analisado

match valor:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case str() if valor.isdigit():
        print("String numérica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Tipo desconhecido")

#exercício 5
mensagem = input("Digite a mensagem: ").lower()

match mensagem:
    case "olá" | "ola" | "bom dia":
        print("Saudação")
    case m if m.endswith("?"):
        print("Pergunta")
    case m if "tchau" in m or "adeus" in m:
        print("Despedida")
    case _:
        print("Mensagem genérica")

#exercício 6
servidor = {"status": "ok", "tempo_resposta": 350}

match servidor:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "erro"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")

#exercício 7
produto = {"categoria": "eletrônico", "preco": 1500}

match produto:
    case {"categoria": "eletrônico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico"}:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")

#exercício 8
operacao = input("Insira a operação (soma/subtrai/multiplica/divide): ")
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

match operacao:
    case "soma":
        print(num1 + num2)
    case "subtrai":
        print(num1 - num2)
    case "multiplica":
        print(num1 * num2)
    case "divide" if num2 != 0:
        print(num1 / num2)
    case "divide":
        print("Erro: divisão por zero")
    case _:
        print("Operação inválida")

#exercício 9
requisicao = {"metodo": "POST", "conteudo": ""}

match requisicao:
    case {"metodo": "GET"}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST"}:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")

#exercício 10
jogador1 = input("Jogador 1 (pedra/papel/tesoura): ").lower()
jogador2 = input("Jogador 2 (pedra/papel/tesoura): ").lower()

match (jogador1, jogador2):
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case (j1, j2) if j1 == j2:
        print("Empate")
    case _:
        print("Jogada inválida")