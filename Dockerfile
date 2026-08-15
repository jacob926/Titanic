# 1. Utiliser une image Python officielle et légère
FROM python:3.10-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier la liste des dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier le reste des fichiers du projet (main.py, Model.pkl, etc.)
COPY . .

# 5. Exposer le port sur lequel FastAPI va tourner
EXPOSE 8000

# 6. Commande pour démarrer le serveur FastAPI dans le conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]