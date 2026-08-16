import pandas as pd
from src.quality import PassengerSchema

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et transforme les données brutes.
    """
    df_clean = df.copy()

    # 1. Normalisation des noms de colonnes (minuscules)
    df_clean.columns = [col.lower() for col in df_clean.columns]

    # 2. Traitement des valeurs manquantes (Imputation)
    # Remplacer les âges manquants par la médiane
    median_age = df_clean['age'].median()
    df_clean['age'] = df_clean['age'].fillna(median_age)

    # Remplacer les tarifs manquants par la médiane
    median_fare = df_clean['fare'].median()
    df_clean['fare'] = df_clean['fare'].fillna(median_fare)

    # Remplacer le port d'embarquement manquant
    df_clean['embarked'] = df_clean['embarked'].fillna('Unknown')

    # 3. Supprimer les doublons
    df_clean = df_clean.drop_duplicates()

    return df_clean


def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valide chaque ligne du DataFrame avec Pydantic.
    Isole les lignes valides et rejette les lignes corrompues.
    """
    valid_records = []
    errors_count = 0

    records = df.to_dict(orient='records')
    
    for row in records:
        try:
            # Reconversion pour Pydantic
            validated_row = PassengerSchema(
                passenger_id=row['passengerid'],
                survived=row['survived'],
                pclass=row['pclass'],
                sex=row['sex'],
                age=row['age'],
                fare=row['fare'],
                embarked=row['embarked']
            )
            valid_records.append(validated_row.model_dump())
        except Exception as e:
            errors_count += 1
            # En Data Engineering, on log de préférence les lignes rejetées dans une table d'erreurs

    print(f"✅ Validation terminée : {len(valid_records)} lignes valides, ⚠️ {errors_count} lignes rejetées.")
    return pd.DataFrame(valid_records)