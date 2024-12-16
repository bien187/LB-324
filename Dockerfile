# Verwende ein offizielles Python-Image als Basis
FROM python:3.10-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die lokalen Projektdateien in das Arbeitsverzeichnis im Container
COPY . /app

# Installiere die notwendigen Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Setze die Umgebungsvariable, um den Flask-Server zu starten
ENV FLASK_APP=main.py

# Exponiere den Port 5000, da Flask standardmäßig auf diesem läuft
EXPOSE 5000

# Befehl zum Starten der App
CMD ["python", "main.py"]