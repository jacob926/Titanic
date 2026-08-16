import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    print("📦 Lecture des données nettoyées depuis la base SQLite...")
    engine = create_engine("sqlite:///data/processed/database.db")
    
    # Requête SQL pour charger les données nettoyées
    df = pd.read_sql("SELECT * FROM passengers_clean", con=engine)
    
    # Sélection des features et de la cible
    X = df[['pclass', 'age', 'fare']]
    y = df['survived']
    
    # Séparation train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entraînement du modèle
    print("🤖 Entraînement du modèle...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Évaluation
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"🎯 Précision du modèle : {accuracy * 100:.2f}%")
    
    # Sauvegarde du modèle
    joblib.dump(model, "Model.pkl")
    print("💾 Modèle sauvegardé sous 'Model.pkl'")

if __name__ == "__main__":
    train_model()