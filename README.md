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

