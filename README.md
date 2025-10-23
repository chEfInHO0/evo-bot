# 🤖 Evolution API Scheduler Bot

[![GitHub Actions Status](https://github.com/chEfInHO0/evo-bot/actions/workflows/deploy.yml/badge.svg)](https://github.com/chEfInHO0/evo-bot/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Feito com Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

## 🚀 Visão Geral do Projeto

Este projeto é uma solução completa e robusta para a **automação de envio de mensagens agendadas via WhatsApp**, utilizando a Evolution API (Baileys) orquestrada com Docker Compose.

Desenvolvido para fins de portfólio, demonstra competência na integração de microsserviços, gerenciamento de ambientes, programação assíncrona com agendamento (`schedule`) e práticas de CI/CD (GitHub Actions) para deploy contínuo.

### 🎯 Habilidades Demonstradas

* **Docker & Docker Compose:** Orquestração de 4 serviços (`evolution-api`, `PostgreSQL`, `Redis`, `Python Bot`) em uma rede interna.
* **Comunicação entre Containers:** Uso de nomes de serviço (`http://evolution-api:8080`) para comunicação segura e eficiente dentro da rede Docker.
* **Automação e Agendamento:** Desenvolvimento de um bot em Python que executa tarefas agendadas em horários específicos, garantindo a entrega de lembretes.
* **CI/CD (GitHub Actions):** Configuração de um pipeline para *build* automático da imagem Docker do Bot e deploy via SSH no servidor remoto.
* **Tratamento de Fuso Horário:** Configuração do `Dockerfile` para garantir que o agendamento no container utilize o fuso horário correto (`America/Sao_Paulo`).

---

## 🛠️ Stack Tecnológica

* **Orquestração:** Docker & Docker Compose (v3.9)
* **API de Mensageria:** Evolution API (`atendai/evolution-api:latest`)
* **Bot:** Python (com as bibliotecas `requests`, `schedule` e `python-dotenv`)
* **Banco de Dados:** PostgreSQL (Persistência da Evolution API)
* **Cache:** Redis (Cache da Evolution API)
* **Deploy:** GitHub Actions (CI/CD)

---

## 📂 Estrutura do Projeto

```

.
├── .env
├── docker-compose.yml
├── LICENSE
├── README.md
├── bot/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── .github/
└── workflows/
└── deploy.yml

````

---

## ⚙️ Configuração e Instalação Local

Para rodar o projeto localmente:

### 1. Pré-requisitos

* Docker e Docker Compose instalados.

### 2. Configurar o Arquivo `.env`

Crie o arquivo `.env` na raiz do projeto com as suas credenciais. O ponto mais crítico é a URL interna e as chaves de segurança:

```env
# --- Configurações da Evolution API ---
AUTHENTICATION_API_KEY=sua_chave_secreta_aqui
SESSION_NAME=MinhaSessaoLembretes
SERVER_URL=http://evolution-api:8080 # CRÍTICO: Nome do serviço Docker

# --- Configurações do PostgreSQL ---
POSTGRES_USER=evo_user
POSTGRES_PASSWORD=evo_pass
POSTGRES_DB=evo_db
````

### 3\. Executar o Stack Docker

Suba todos os serviços, forçando a reconstrução do Bot para garantir o fuso horário correto:

```bash
docker-compose up -d --build
```

### 4\. Conectar a Instância

1.  Acesse a Evolution API no seu navegador: `http://localhost:8080/manager/`.
2.  Escaneie o QR Code com o WhatsApp no seu celular.
3.  Quando o status estiver `Connected`, o bot estará pronto para enviar as mensagens agendadas.

### 5\. Monitorar os Logs

Acompanhe o que o bot está fazendo em tempo real:

```bash
docker logs bot -f
```

-----

## ☁️ Pipeline de Deploy (GitHub Actions)

O deploy para um servidor remoto (VPS) é gerenciado automaticamente pelo GitHub Actions.

O pipeline realiza os seguintes passos em cada `push` para a branch `main`:

1.  **Build & Push:** Constrói a imagem Docker do Bot e a envia para o Docker Hub (ou Container Registry).
2.  **Acesso SSH:** Usa a `SSH_PRIVATE_KEY` (configurada como Secret) para estabelecer uma conexão segura com a VPS.
3.  **Sincronização:** Envia o `docker-compose.yml` (ajustado para puxar a imagem do Hub) e o `.env` para o diretório de destino.
4.  **Execução Remota:** Executa `docker-compose up -d --force-recreate` na VPS, garantindo que o novo código do Bot seja rapidamente implantado.

> **Nota:** As credenciais da VPS e do Docker Hub são gerenciadas com segurança usando **GitHub Secrets**.

-----

## 👤 Autor

**Luccas Elias de Almeida dos Santos**

  * [[LinkedIn](https://www.linkedin.com/in/luccas-santos-3a86b31a6/)]
  * [[GitHub](https://github.com/chEfInHO0)]

<!-- end list -->
