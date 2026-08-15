from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Initialisation de l'application FastAPI
app = FastAPI(
    title="API de Prédiction de Survie du Titanic",
    description="Interface MLOps pour interroger le modèle Scikit-Learn",
    version="1.0"
)

# 2. Chargement du modèle entraîné
model = joblib.load('Model.pkl')

# 3. Définition du schéma des données d'entrée (validation automatique grâce à Pydantic)
class PassengerData(BaseModel):
    pclass: int
    sex: int      # 0 pour female, 1 pour male
    age: float
    fare: float

# Route de test (page d'accueil de l'API)
@app.get("/")
def home():
    return {"message": "API opérationnelle. Allez sur /docs pour tester le modèle."}

# Route de prédiction
@app.post("/predict")
def predict_survival(passenger: PassengerData):
    # Transformation des données reçues en DataFrame Pandas
    data = pd.DataFrame([[
        passenger.pclass,
        passenger.sex,
        passenger.age,
        passenger.fare
    ]], columns=['pclass', 'sex', 'age', 'fare'])
    
    # Prédiction avec le modèle
    prediction = model.predict(data)[0]
    probabilities = model.predict_proba(data)[0]
    
    # Résultat
    status = "Survécu" if prediction == 1 else "Succombé"
    
    return {
        "prediction": int(prediction),
        "status": status,
        "probabilite_survie": float(probabilities[1])
    }