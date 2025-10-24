import requests
import json
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
from os import environ
from random import choice

# 1. Carrega variáveis do arquivo .env
load_dotenv()

API_URL = environ.get("SERVER_URL")  # Ex: http://localhost:8080
SESSION = environ.get("SESSION_NAME")  # Ex: BOT
TOKEN = environ.get("AUTHENTICATION_API_KEY")  # Sua chave de autenticação
ALERT_NUMBER = environ.get("ALERT_NUMBER")

MOR = [
    "meu amor ❤",
    "paixão da minha vida 💟",
    "razão do meu viver 💗",
    "✨ minha fada vampiresca  ✨",
    "minha princesa ❣",
    "meu xuxu 🌹",
    "meu chocolate branco 🍫",
    "meu moranguinho do amor 🍓",
    "meu pão de alho 🥖🧄",
    "meu docinho de coco 🥥",
    "minha batata frita 🍟",
    "minha hello kitty 😻",
    "minha gostosa 🔥"
]


url = f"{API_URL}/message/sendText/{SESSION}"
HEADERS = {
    "apikey": TOKEN,
    "Content-Type": "application/json"
}

# 2. CONFIGURAÇÕES DO LEMBRETE
# ----------------------------------------------------------------------------------
# !!! IMPORTANTE: SUBSTITUA PELO NÚMERO CORRETO (55DDD9XXXXXXXX)
NUMERO_NAMORADA = environ.get("TARGET_NUMBER")
# ----------------------------------------------------------------------------------


def enviar_mensagem(numero, texto):
    """Envia uma mensagem de texto via Evolution API usando o payload simples."""

    # Payload ajustado que resolveu o erro 400 Bad Request
    data = {
        "number": numero,
        "text": texto,  # Endpoint /sendText espera o texto no nível raiz
        "options": {
            "delay": 1000,
            "presence": "composing"
        }
    }

    try:
        response = requests.post(url, headers=HEADERS,
                                 data=json.dumps(data), timeout=10)

        if response.status_code == 200:
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Mensagem enviada para {numero}")
        else:
            # Inclui a resposta completa para fácil diagnóstico
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ❌ Erro ao enviar: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ❌ ERRO: Falha de conexão com a Evolution API.")
    except Exception as e:
        print(f"❌ Erro geral durante o envio: {e}")


# 3. FUNÇÕES DE AGENDAMENTO ESPECÍFICAS
# Você pode criar uma função para cada dose
def lembrete_manha():
    """Lembrete de Remédio da Manhã (8:00)"""
    texto = f"Bom dia {choice(MOR)}! ☀️ Lembre-se de tomar seus remédios e beber bastante água 🧊!"
    enviar_mensagem(NUMERO_NAMORADA, texto)


def lembrete_remedio():
    texto = f"{choice(MOR)}, está quase na hora do seu remédio, não se esqueça de tomar eles, eu te amo ❤"
    enviar_mensagem(NUMERO_NAMORADA, texto)


def lembrete_almoco():
    """Lembrete de Remédio do Almoço (12:30)"""
    texto = f"Já almoçou {choice(MOR)}? Saiba que você é muito importante pra mim "
    enviar_mensagem(NUMERO_NAMORADA, texto)


def lembrete_noite():
    """Lembrete de Remédio da Noite (22:00)"""
    texto = f"Boa noite {choice(MOR)}!  Está quase na hora de dormir e de tomar os remédios. Te amo! 🌙"
    enviar_mensagem(NUMERO_NAMORADA, texto)


# 4. AGENDAMENTO DIÁRIO
# Agenda as funções para rodar todos os dias nos horários corretos.
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Bot de Lembretes Agendado e Rodando...")
print("-" * 50)


schedule.every().day.at("07:00").do(lembrete_manha)

schedule.every().day.at("10:55").do(lembrete_remedio)

schedule.every().day.at("13:30").do(lembrete_almoco)

schedule.every().day.at("22:00").do(lembrete_noite)

schedule.every().day.at("22:55").do(lembrete_remedio)

enviar_mensagem(ALERT_NUMBER, "Bot iniciando")

# 5. LOOP PRINCIPAL
while True:
    # Verifica se alguma tarefa agendada deve ser executada
    schedule.run_pending()
    # Espera 1 segundo antes de checar novamente (para não consumir muita CPU)
    time.sleep(1)
