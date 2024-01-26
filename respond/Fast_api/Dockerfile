# image de base avec Python
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/api

# Copier le script FastAPI et ses dépendances dans le conteneur
COPY fastapi.py .
COPY requirements.txt .

# Installer les dépendances nécessaires 
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application FastAPI écoute
EXPOSE 8000

# Commande pour lancer l'application FastAPI
CMD ["uvicorn", "fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
