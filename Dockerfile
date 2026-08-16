# 1. Image de base Python légère
FROM python:3.12-slim

# 2. Définition du répertoire de travail dans le conteneur
WORKDIR /app

# 3. Empêcher Python d'écrire des fichiers .pyc et forcer l'affichage immédiat des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Installation des dépendances système de base si nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copie de l'intégralité du projet dans le conteneur
COPY . .

# 7. Création explicite des dossiers de données s'ils n'existent pas
RUN mkdir -p data/raw data/processed

# 8. Exposition du port de l'API FastAPI
EXPOSE 8000

# 9. Lancement automatique du pipeline ETL, de l'entraînement et enfin de l'API FastAPI
CMD python main_pipeline.py && python src/train.py && uvicorn main:app --host 0.0.0.0 --port 8000