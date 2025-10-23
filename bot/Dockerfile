# Seu Dockerfile atual
FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache tzdata # Instala o banco de dados de fusos horários (necessário no Alpine)
RUN pip install --no-cache-dir -r requirements.txt

# --- ADICIONE ESTAS DUAS LINHAS ---
ENV TZ America/Sao_Paulo
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# -----------------------------------

COPY . .
CMD ["python", "app.py"]