# image de base avec Python
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/scraping

# Copier le script de scraping et ses dépendances dans le conteneur
COPY scraping.py .
COPY requirements.txt .

# Installer les dépendances nécessaires 
RUN pip install -r requirements.txt

# Commande pour exécuter le script de scraping
CMD ["python", "scraping.py"]
