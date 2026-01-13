import requests
import json
import schedule
import time
from datetime import datetime
from random import choice
from os import environ
from config import BotConfig


def load_messages_templates():
    try:
        with open("./templates.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def send_message(number, message):
    """Envia uma mensagem de texto via Evolution API usando o payload simples."""

    # Payload ajustado que resolveu o erro 400 Bad Request
    data = {
        "number": number,
        "text": message,  # Endpoint /sendText espera o texto no nível raiz
        "options": {
            "delay": 1000,
            "presence": "composing"
        }
    }
    print(data)
    try:
        print(BotConfig)
        print(BotConfig.URL)
        print(BotConfig.HEADERS)
        response = requests.post(BotConfig.URL, headers=BotConfig.HEADERS,
                                 data=json.dumps(data), timeout=10)
        if response.status_code == 200 or response.status_code == 201:
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Mensagem enviada para {number}")
        else:
            # Inclui a resposta completa para fácil diagnóstico
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ❌ Erro ao enviar: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ❌ ERRO: Falha de conexão com a Evolution API.")
    except Exception as e:
        print(f"❌ Erro geral durante o envio: {e}")


def reminder(hour):
    r = {
        "07:00": f"Bom dia {choice(load_messages_templates())}! ☀️ Lembre-se de tomar seus remédios e beber bastante água 🧊!",
        "09:55": f"{choice(load_messages_templates())}, está quase na hora do seu remédio, não se esqueça de tomar eles, eu te amo ❤",
        "13:30": f"Já almoçou {choice(load_messages_templates())}? Saiba que você é muito importante pra mim ",
        "21:00": f"Boa noite {choice(load_messages_templates())}!  Está quase na hora de dormir e de tomar os remédios. Te amo! 🌙",
    }
    send_message(BotConfig.NUMERO_NAMORADA, r.get(hour))


# 4. AGENDAMENTO DIÁRIO
# Agenda as funções para rodar todos os dias nos horários corretos.
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Bot de Lembretes Agendado e Rodando...")
print("-" * 50)

schedule.every().day.at("07:00").do(reminder, "07:00")

schedule.every().day.at("10:55").do(reminder, "09:55")

schedule.every().day.at("13:53").do(reminder, "13:30")

schedule.every().day.at("21:00").do(reminder, "21:00")

schedule.every().day.at("21:55").do(reminder, "09:55")

send_message(BotConfig.ALERT_NUMBER, "Bot iniciando")

# 5. LOOP PRINCIPAL
while True:
    # Verifica se alguma tarefa agendada deve ser executada
    schedule.run_pending()
    # Espera 1 segundo antes de checar novamente (para não consumir muita CPU)
    time.sleep(1)
