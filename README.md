[🇧🇷 Versão em Português](./README.pt-BR.md)

# 🤖 Evolution API Scheduler Bot

[![GitHub Actions Status](https://github.com/chEfInHO0/evo-bot/actions/workflows/deploy.yml/badge.svg)](https://github.com/chEfInHO0/evo-bot/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

## 🚀 Project Overview

This project is a complete and robust solution for **automating scheduled WhatsApp message delivery**, using the Evolution API (Baileys) orchestrated with Docker Compose.

Developed as a portfolio project, it demonstrates strong skills in microservice integration, environment management, asynchronous programming with scheduling (`schedule`), and CI/CD practices (GitHub Actions) for continuous deployment.

### 🎯 Demonstrated Skills

- **Docker & Docker Compose:** Orchestration of 4 services (`evolution-api`, `PostgreSQL`, `Redis`, `Python Bot`) within an internal network.
- **Inter-Container Communication:** Using service names (`http://evolution-api:8080`) for secure and efficient communication within Docker.
- **Automation & Scheduling:** A Python bot that executes scheduled tasks at specific times, ensuring timely message delivery.
- **CI/CD (GitHub Actions):** Automated pipeline for building the bot's Docker image and deploying it via SSH to a remote server.
- **Timezone Handling:** Configured `Dockerfile` to ensure container scheduling uses the correct timezone (`America/Sao_Paulo`).

---

## 🛠️ Tech Stack

- **Orchestration:** Docker & Docker Compose (v3.9)  
- **Messaging API:** Evolution API (`atendai/evolution-api:latest`)  
- **Bot:** Python (`requests`, `schedule`, and `python-dotenv`)  
- **Database:** PostgreSQL (Evolution API persistence)  
- **Cache:** Redis (Evolution API cache)  
- **Deploy:** GitHub Actions (CI/CD)

---

## 📂 Project Structure

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

## ⚙️ Local Setup & Installation

To run this project locally:

### 1. Prerequisites

- Docker and Docker Compose installed.

### 2. Configure the `.env` File

Create an `.env` file in the project root with your credentials.  
The most critical values are the internal API URL and authentication keys.

```env
# --- Evolution API ---

# Global authentication key. CHANGE THIS VALUE.
# Auth API Key
AUTHENTICATION_API_KEY="YOUR_API_KEY"  # recommended -> openssl rand -hex 32

# Server URL (optional for local testing, keep it here anyway)
SERVER_URL=http://evolution-api:8080

ALERT_NUMBER=""  # (55DDD9XXXXXXXX) will receive a message when the bot starts
TARGET_NUMBER="" # (55DDD9XXXXXXXX) will receive the scheduled messages

SESSION_NAME="YOUR_SESSION_NAME_ON_EVO"

# --- Database ---
DATABASE_ENABLED=true
DATABASE_PROVIDER=postgresql

POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
POSTGRES_DB=POSTGRES_DB

# postgresql://<user>:<password>@<service_name>:<port>/<db_name>
DATABASE_CONNECTION_URI=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@evo_postgres:5432/${POSTGRES_DB} # evo_postgres (docker container)
````

### 3. Run the Docker Stack

Start all services, forcing a rebuild to ensure timezone configuration is applied:

```bash
docker-compose up -d --build
```

### 4. Connect the Instance

1. Open the Evolution API manager in your browser: `http://localhost:8080/manager/`
2. Scan the QR Code with your WhatsApp mobile app.
3. Once the status shows `Connected`, the bot will be ready to send scheduled messages.

### 5. Monitor Logs

Watch bot activity in real time:

```bash
docker logs evolution_api -f
```

---

## ☁️ Deployment Pipeline (GitHub Actions)

Deployment to a remote server (VPS) is managed automatically via GitHub Actions.

The pipeline performs the following steps on each `push` to the `main` branch:

1. **Build & Push:** Builds the bot’s Docker image and pushes it to Docker Hub (or another container registry).
2. **SSH Access:** Uses `SSH_PRIVATE_KEY` (stored as a Secret) to securely connect to the VPS.
3. **Sync:** Uploads the updated `docker-compose.yml` (configured to pull the image from the registry) and `.env` to the target directory.
4. **Remote Execution:** Runs `docker-compose up -d --force-recreate` on the VPS to redeploy the updated bot image seamlessly.

> **Note:** VPS and Docker Hub credentials are securely managed using **GitHub Secrets**.

---

## 👤 Author

**Luccas Elias de Almeida dos Santos**

* [LinkedIn](https://www.linkedin.com/in/luccas-santos-3a86b31a6/)
* [GitHub](https://github.com/chEfInHO0)
