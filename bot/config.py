from os import environ
from dotenv import load_dotenv

load_dotenv()


class BotConfig:

    API_URL = environ.get("SERVER_URL")  # Ex: http://localhost:8080
    SESSION = environ.get("SESSION_NAME")  # Ex: BOT
    TOKEN = environ.get("AUTHENTICATION_API_KEY")  # Sua chave de autenticação
    ALERT_NUMBER = environ.get("ALERT_NUMBER")
    URL = f"{API_URL}/message/sendText/{SESSION}"
    HEADERS = {
        "apikey": TOKEN,
        "Content-Type": "application/json"
    }
    NUMERO_NAMORADA = environ.get("TARGET_NUMBER")
