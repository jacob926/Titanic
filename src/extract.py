import pandas as pd
import os

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Lit le fichier de données brutes (CSV).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier brut est introuvable à l'emplacement : {file_path}")
    
    print(f"📥 Extraction des données depuis : {file_path}")
    df_raw = pd.read_csv(file_path)
    print(f"📊 Données extraites : {len(df_raw)} lignes.")
    return df_raw