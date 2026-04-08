import re
import os
from datetime import datetime

base_path = os.path.join("Resoluções", "regex", "ficheiros")
os.makedirs(base_path, exist_ok=True)

dados_txt = os.path.join(base_path, "dados.txt")
conteudo_dados = """Nome: Ana Costa, Email: ana.costa@gmail.com, Telemóvel: 912345678
Nome: João Silva, Email: joao_silva@empresa.pt, Telemóvel: 914-567-123
Nome: Marta Reis, Email: marta.reis@escola.edu, Telemóvel: 210 987 654
Nome: Pedro, Email: pedro123@hotmail.com, Telemóvel: 968123456"""

with open(dados_txt, "w", encoding="utf-8") as f:
    f.write(conteudo_dados)

# Exercício 1: Ler o ficheiro
with open(dados_txt, "r", encoding="utf-8") as f:
    conteudo = f.read()
print("=== Exercício 1: Ler o ficheiro ===")
print(conteudo)

# Exercício 2: Encontrar todos os emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', conteudo)
print("\n=== Exercício 2: Encontrar todos os emails ===")
for email in emails:
    print(email)

# Exercício 3: Encontrar todos os números de telemóvel
padrao_tel = r'\b(?:\d{9}|\d{3}-\d{3}-\d{3}|\d{3}\s?\d{3}\s?\d{3})\b'
telemoveis = re.findall(padrao_tel, conteudo)
print("\n=== Exercício 3: Encontrar todos os números de telemóvel ===")
for tel in telemoveis:
    print(tel)

# Exercício 4: Extrair apenas os nomes
nomes = re.findall(r'Nome:\s*([^,]+)', conteudo)
print("\n=== Exercício 4: Extrair apenas os nomes ===")
for nome in nomes:
    print(nome.strip())

# Exercício 5: Guardar os dados extraídos num novo ficheiro
extraidos_txt = os.path.join(base_path, "extraidos.txt")
with open(dados_txt, "r", encoding="utf-8") as f:
    linhas = f.readlines()

with open(extraidos_txt, "w", encoding="utf-8") as f:
    for linha in linhas:
        nome = re.search(r'Nome:\s*([^,]+)', linha)
        email = re.search(r'Email:\s*([\w\.-]+@[\w\.-]+\.\w+)', linha)
        tel = re.search(r'Telemóvel:\s*([\d\s-]+)', linha)
        if nome and email and tel:
            nome_limpo = nome.group(1).strip()
            email_limpo = email.group(1).strip()
            tel_limpo = re.sub(r'[\s-]', '', tel.group(1).strip())
            f.write(f"{nome_limpo} | {email_limpo} | {tel_limpo}\n")
print("\n=== Exercício 5: Guardar os dados extraídos num novo ficheiro ===")
print("Ficheiro extraidos.txt criado.")

# Exercício 6: Validar emails que terminam em .pt
emails_pt = [e for e in emails if e.endswith('.pt')]
print("\n=== Exercício 6: Validar emails que terminam em .pt ===")
for e in emails_pt:
    print(e)

registos_txt = os.path.join(base_path, "registos.txt")
conteudo_registos = """Nome: Maria Gomes | NIF: 123456789 | Data: 01/09/2025 | Código Postal: 1000-001 | Site: https://www.exemplo.pt
Nome: Rui Silva | NIF: 987654321 | Data: 15/08/2024 | Código Postal: 4000-123 | Site: http://empresa.com
Nome: Carla Dias | NIF: 192837465 | Data: 22/12/2023 | Código Postal: 3000-456 | Site: https://escola.edu"""

with open(registos_txt, "w", encoding="utf-8") as f:
    f.write(conteudo_registos)

# Exercício 7: Extrair todos os NIFs (9 dígitos)
nifs = re.findall(r'NIF:\s*(\d{9})', conteudo_registos)
print("\n=== Exercício 7: Extrair todos os NIFs ===")
for nif in nifs:
    print(nif)

# Exercício 8: Extrair datas no formato DD/MM/AAAA
datas = re.findall(r'Data:\s*(\d{2}/\d{2}/\d{4})', conteudo_registos)
print("\n=== Exercício 8: Extrair datas ===")
for d in datas:
    print(d)

# Exercício 9: Extrair códigos postais portugueses
codigos_postais = re.findall(r'Código Postal:\s*(\d{4}-\d{3})', conteudo_registos)
print("\n=== Exercício 9: Extrair códigos postais ===")
for cp in codigos_postais:
    print(cp)

# Exercício 10: Extrair apenas os domínios dos sites
dominios = re.findall(r'Site:\s*https?://(?:www\.)?([^/\s]+)', conteudo_registos)
print("\n=== Exercício 10: Extrair domínios dos sites ===")
for dom in dominios:
    print(dom)

# Exercício 11: Validar se todos os NIFs começam com um dígito válido
print("\n=== Exercício 11: Validar NIFs ===")
for nif in nifs:
    status = "VÁLIDO" if nif[0] in "123568" else "INVÁLIDO"
    print(f"{nif} → {status}")

# Exercício 12: Criar um ficheiro resumo.txt
resumo_txt = os.path.join(base_path, "resumo.txt")
with open(resumo_txt, "w", encoding="utf-8") as f:
    for linha in conteudo_registos.strip().split('\n'):
        nome = re.search(r'Nome:\s*([^|]+)', linha)
        nif = re.search(r'NIF:\s*(\d{9})', linha)
        data = re.search(r'Data:\s*(\d{2}/\d{2}/\d{4})', linha)
        cp = re.search(r'Código Postal:\s*(\d{4}-\d{3})', linha)
        site = re.search(r'Site:\s*https?://(?:www\.)?([^/\s]+)', linha)
        if nome and nif and data and cp and site:
            f.write(f"{nome.group(1).strip()} | {nif.group(1)} | {data.group(1)} | {cp.group(1)} | {site.group(1)}\n")
print("\n=== Exercício 12: Criar ficheiro resumo.txt ===")
print("Ficheiro resumo.txt criado.")

# Exercício 13: Encontrar registos com datas anteriores a 2025
print("\n=== Exercício 13: Registos com datas anteriores a 2025 ===")
for linha in conteudo_registos.strip().split('\n'):
    data_match = re.search(r'Data:\s*(\d{2}/\d{2}/\d{4})', linha)
    if data_match:
        data_obj = datetime.strptime(data_match.group(1), "%d/%m/%Y")
        if data_obj.year < 2025:
            print(linha.strip())