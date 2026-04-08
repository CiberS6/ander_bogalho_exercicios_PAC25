# LAB 1 - Sistema de Chat Multiusuário com Deteção de Dados Pessoais (GDPR)

## Objetivo
Desenvolver um sistema de chat multiusuário em Python capaz de detetar e bloquear dados pessoais sensíveis em conformidade com o Regulamento Geral de Proteção de Dados (**GDPR**). O sistema inclui ainda registo das tentativas de envio de dados pessoais para fins de análise de engenharia social.

## Funcionalidades Implementadas

- Comunicação cliente-servidor utilizando sockets TCP
- Suporte a múltiplos utilizadores em simultâneo (multithreading)
- Deteção automática de dados pessoais através de Expressões Regulares (regex):
  - Endereços de email
  - Números de telefone (Portugal e internacional)
  - Endereços IP
  - Nomes completos
  - Datas de nascimento
  - Números de cartão de crédito
- Bloqueio da mensagem quando são detetados dados pessoais
- Alerta ao utilizador que tentou enviar os dados
- Registo das mensagens bloqueadas num ficheiro de texto
- Notificação de entrada e saída de utilizadores no chat
- Comando `exit` para desconectar do servidor

## Arquitetura do Sistema

### Servidor (`server.py`)
- Aceita múltiplas conexões de clientes
- Gerencia cada cliente numa thread separada
- Verifica todas as mensagens em busca de dados pessoais antes de as retransmitir
- Guarda as tentativas de envio de dados pessoais no ficheiro `registros/dados_pessoais_detectados.txt`

### Cliente (`client.py`)
- Interface simples em linha de comando (CLI)
- Permite enviar e receber mensagens em tempo real
- Suporte ao comando `exit` para sair do chat

## Como Executar o Projeto

### 1. Iniciar o Servidor
Abra um terminal e execute:
```bash```
py server.py

### 2. Iniciar os Clientes
Abra vários terminais (um por utilizador) e execute em cada um:
py client.py

### 3. Utilização
Introduza o username quando solicitado
Escreva as mensagens normalmente
Se tentar enviar dados pessoais, a mensagem será bloqueada e guardada
Escreva exit para sair do chat

### Estrutura de Pastas
textLAB1-Chat-GDPR/
├── server.py
├── client.py
├── registros/
│   └── dados_pessoais_detectados.txt     ← (criado automaticamente)
└── README.md

### Tecnologias Utilizadas
- Python 3
- socket — Comunicação em rede
- threading — Suporte a múltiplos utilizadores
- re — Expressões Regulares (deteção de dados pessoais)
- os — Gestão de ficheiros e pastas
- datetime — Registo com data e hora

### Principais Funcionalidades de Deteção de Dados Pessoais
O sistema utiliza expressões regulares para identificar automaticamente informações sensíveis. Quando uma mensagem é bloqueada, é guardada no ficheiro com as seguintes informações:
- Data e hora da tentativa
- Username do utilizador
- Tipos de dados detetados
- Mensagem original

## Laboratório desenvolvido para a UC de Programação Aplicada a Cibersegurança II.