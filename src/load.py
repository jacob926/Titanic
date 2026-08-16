from sqlalchemy import create_engine
import pandas as pd
import os

def load_to_db(df: pd.DataFrame, db_path: str = "data/processed/database.db", table_name: str = "passengers_clean"):
    """
    Insère le DataFrame nettoyé dans une base SQL.
    """
    # S'assurer que le dossier de destination existe
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Créer le moteur SQLAlchemy (SQLite)
    engine = create_engine(f"sqlite:///{db_path}")
    
    # Charger les données dans la table (remplace la table si elle existe déjà)
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    print(f"💾 {len(df)} lignes insérées dans la base SQLite '{db_path}' (Table: '{table_name}')")