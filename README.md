## Participants
```text
471H-TOL RANDRIANAMBINININA Jacob Bless
449H-TOL MILAMANA Darcy
481H-TOL RAZAFIMAMONJY Fanomezantsoa Heurio Fortunat
493H-TOL TATIANA Volasoa Gisèle
499H-TOL TSIMAGNEFEDRAZA Solomon
```


# Titanic MLOps Prediction API

Pipeline MLOps de bout en bout pour la prédiction de survie des passagers du Titanic. Ce projet intègre l'ingestion de données (ETL), l'entraînement de modèles de Machine Learning avec `scikit-learn`, le stockage distant des artefacts sur **Hugging Face Hub**, une API d'inférence haute performance avec **FastAPI**, et un conteneur **Docker** prêt pour la production.

---

## Architecture du Projet

```text
[ Données Brutes CSV ] 
       │
       ▼ (ETL & SQLite)
[ Base SQLite (data/processed/database.db) ]
       │
       ▼ (src/train.py)
[ Entraînement Random Forest ] ──(Upload)──► [ Hugging Face Hub (Model Registry) ]
                                                        │
                                                        ▼ (Download au démarrage)
[ Conteneur Docker / Render ] ─────────────► [ API FastAPI (Inférence) ]
```

## Structure du Projet

```text
titanic-mlops/
│
├── data/
│   ├── raw/                  # Données brutes (Titanic-Dataset.csv)
│   └── processed/            # Base de données SQLite (database.db)
│
├── src/
│   ├── train.py              # Script d'entraînement et évaluation du modèle
│   └── upload_model.py       # Gestionnaire de synchronisation avec Hugging Face
│
├── .gitignore                # Fichiers exclus de Git (venv, Model.pkl, db)
├── Dockerfile                # Configuration du conteneur de production
├── entrypoint.sh             # Script d'initialisation du conteneur
├── main.py                   # Application FastAPI (Point d'entrée de l'API)
├── requirements.txt          # Dépendances Python du projet
└── README.md                 # Documentation du projet
```

## Installation et Configuration Locale
1. Cloner le dépôt et configurer l'environnement virtuel
git clone [https://github.com/jacob926/Titanic.git](https://github.com/jacob926/Titanic.git)
cd Titanic

# Créer et activer l'environnement virtuel
python -m venv .venv
# Sur Windows (PowerShell) :
.venv\Scripts\Activate
# Sur Linux / Mac :
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# 2. Configurer les variables d'environnement
sur windows (powerShell)
```text
$env:HF_TOKEN="hf_votre_token_hugging_face"
```
sur Linux
```text
export HF_TOKEN="hf_votre_token_hugging_face"
```

## Utilisation
# Étape 1 : Exécuter le pipeline d'entraînement et l'upload
Ce script lit la base SQLite, entraîne le modèle RandomForestClassifier, sauvegarde localement Model.pkl et l'envoie automatiquement sur Hugging Face :
```text
python src/train.py
```
# Étape 2 : Lancer l'API FastAPI en local
```text
uvicorn main:app --reload --port 8000
```

L'API est accessible localement sur http://127.0.0.1:8000. Tu peux tester les endpoints interactifs via la documentation Swagger sur http://127.0.0.1:8000/docs.


## Déploiement (Docker & Render)
Le projet est configuré pour un déploiement continu conteneurisé :
1. Le **Dockerfile** installe l'environnement et copie les sources.
2. **entrypoint.sh** orchestre le lancement.
3. L'API récupère dynamiquement le modèle depuis Hugging Face au démarrage via **hf_hub_download.**

## Stack Technique
```text
Langage : Python 3.12
Machine Learning : Scikit-Learn (Random Forest)
Base de données / ETL : SQLAlchemy, SQLite, Pandas
Model Registry : Hugging Face Hub (huggingface_hub, joblib)
API Web : FastAPI, Uvicorn, Pydantic
DevOps : Docker, Render, Git/GitHub
```
