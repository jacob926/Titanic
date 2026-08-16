from src.extract import extract_data
from src.transform import clean_data, validate_dataframe
from src.load import load_to_db

def run_pipeline():
    print("🚀 --- DÉMARRAGE DU PIPELINE ETL --- 🚀")
    
    # 1. EXTRACT
    raw_csv_path = "data/raw/Titanic-Dataset.csv" # Assure-toi que ton fichier source est ici
    df_raw = extract_data(raw_csv_path)
    
    # 2. TRANSFORM
    print("🧹 Nettoyage des données...")
    df_cleaned = clean_data(df_raw)
    
    # 3. DATA QUALITY (Validation Pydantic)
    print("🔍 Validation du contrat de données...")
    df_validated = validate_dataframe(df_cleaned)
    
    # 4. LOAD
    print("💾 Enregistrement dans la base de données analytique...")
    load_to_db(df_validated)
    
    print("🎉 --- PIPELINE ETL EXÉCUTÉ AVEC SUCCÈS --- 🎉")

if __name__ == "__main__":
    run_pipeline()