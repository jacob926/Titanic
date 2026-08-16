from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from sqlalchemy import create_engine
import os

app = FastAPI(
    title="API de Prédiction - Data & MLOps Pipeline",
    description="API FastAPI connectée au modèle Random Forest et à la base SQLite.",
    version="2.0.0"
)

# 1. Chargement du modèle entraîné
MODEL_PATH = "Model.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Le fichier Model.pkl est introuvable. Exécute d'abord src/train.py !")

model = joblib.load(MODEL_PATH)

# Connexion à la base SQLite pour sauvegarder les prédictions
DB_PATH = "sqlite:///data/processed/database.db"
engine = create_engine(DB_PATH)


# 2. Contrat d'entrée Pydantic pour l'API (validation des requêtes)
class PassengerPredictionInput(BaseModel):
    pclass: int = Field(..., ge=1, le=3, description="Classe du billet (1, 2 ou 3)")
    age: float = Field(..., ge=0, le=120, description="Âge du passager")
    fare: float = Field(..., ge=0, description="Tarif du billet")

    class Config:
        json_schema_extra = {
            "example": {
                "pclass": 3,
                "age": 22.0,
                "fare": 7.25
            }
        }


@app.get("/")
def home():
    return {
        "message": "Bienvenue sur l'API de prédiction !",
        "status": "online",
        "docs": "/docs"
    }


@app.post("/predict")
def predict(data: PassengerPredictionInput):
    try:
        # Convertir les données reçues en DataFrame Pandas
        input_data = pd.DataFrame([{
            "pclass": data.pclass,
            "age": data.age,
            "fare": data.fare
        }])
        
        # Faire la prédiction avec le modèle
        prediction = int(model.predict(input_data)[0])
        probability = float(model.predict_proba(input_data)[0][1])

        # Enregistrer la prédiction reçue dans une table SQLite de logs
        log_data = input_data.copy()
        log_data["prediction"] = prediction
        log_data["probability"] = probability
        log_data.to_sql("predictions_logs", con=engine, if_exists="append", index=False)

        return {
            "survived": prediction,
            "survival_probability": round(probability, 4),
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur de prédiction : {str(e)}")