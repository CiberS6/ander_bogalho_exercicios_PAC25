import re
import json
import os

base_path = os.path.join("Resoluções", "regex", "ficheiros")
os.makedirs(base_path, exist_ok=True)

# Criar dados.json
dados_json_path = os.path.join(base_path, "dados.json")
dados_json = [
  {
    "nome": "Ana Costa",
    "email": "ana.costa@gmail.com",
    "nif": "123456789",
    "telemovel": "912345678",
    "site": "https://www.anacosta.pt"
  },
  {
    "nome": "João Silva",
    "email": "joao_silva@empresa.com",
    "nif": "987654321",
    "telemovel": "914-567-123",
    "site": "http://joaosilva.com"
  },
  {
    "nome": "Marta Dias",
    "email": "marta.dias@escola.edu",
    "nif": "192837465",
    "telemovel": "210 987 654",
    "site": "https://marta.edu"
  }
]

with open(dados_json_path, "w", encoding="utf-8") as f:
    json.dump(dados_json, f, indent=2, ensure_ascii=False)

# Exercício 1: Ler o ficheiro JSON
with open(dados_json_path, "r", encoding="utf-8") as f:
    dados = json.load(f)
print("=== Exercício 1: Ler o ficheiro JSON ===")
print("Ficheiro JSON lido com sucesso.")

# Exercício 2: Validar emails com regex
padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
print("\n=== Exercício 2: Validar emails com regex ===")
for pessoa in dados:
    status = "VÁLIDO" if re.match(padrao_email, pessoa["email"]) else "INVÁLIDO"
    print(f"{pessoa['email']} → {status}")

# Exercício 3: Extrair domínios dos sites
print("\n=== Exercício 3: Extrair domínios dos sites ===")
for pessoa in dados:
    dominio = re.search(r'https?://(?:www\.)?([^/]+)', pessoa["site"])
    if dominio:
        print(dominio.group(1))

# Exercício 4: Validar NIFs com regex
print("\n=== Exercício 4: Validar NIFs com regex ===")
for pessoa in dados:
    nif = pessoa["nif"]
    status = "VÁLIDO" if re.match(r'^[123568]\d{8}$', nif) else "INVÁLIDO"
    print(f"{nif} → {status}")

# Exercício 5: Guardar apenas os registos válidos num novo ficheiro JSON
registos_validos = []
for pessoa in dados:
    email_ok = bool(re.match(padrao_email, pessoa["email"]))
    nif_ok = bool(re.match(r'^[123568]\d{8}$', pessoa["nif"]))
    tel_limpo = re.sub(r'[\s-]', '', pessoa["telemovel"])
    tel_ok = len(tel_limpo) == 9 and tel_limpo.isdigit()
    
    if email_ok and nif_ok and tel_ok:
        registos_validos.append(pessoa)

validos_json_path = os.path.join(base_path, "validos.json")
with open(validos_json_path, "w", encoding="utf-8") as f:
    json.dump(registos_validos, f, indent=2, ensure_ascii=False)
print("\n=== Exercício 5: Guardar registos válidos ===")
print(f"{len(registos_validos)} registos válidos guardados em validos.json")

# Exercício 6: Criar um ficheiro .txt com as keys nome e email
nome_email_path = os.path.join(base_path, "nome_email.txt")
with open(nome_email_path, "w", encoding="utf-8") as f:
    for pessoa in dados:
        f.write(f"{pessoa['nome']} | {pessoa['email']}\n")
print("\n=== Exercício 6: Criar ficheiro com nome e email ===")
print("Ficheiro nome_email.txt criado.")