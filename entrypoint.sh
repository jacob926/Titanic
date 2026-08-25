#!/bin/sh
set -e

echo "🚀 Initialisation du conteneur..."

# 1. Télécharger le modèle s'il manque
python src/download_model.py

# 2. Exécuter le pipeline si nécessaire
python main_pipeline.py

# 3. Lancer FastAPI
echo "🌐 Démarrage de FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 8000