import os
import urllib.request

MODEL_PATH = "Model.pkl"
# Remplace par l'URL réelle de ton fichier stocké à distance (ex: Release GitHub, bucket S3, HuggingFace)
MODEL_URL = os.getenv("MODEL_URL", "https://github.com/jacob926/Titanic/releases/download/v1.0.0/Model.pkl")

def download_model_if_not_exists():
    if not os.path.exists(MODEL_PATH):
        print(f"📥 Téléchargement du modèle depuis : {MODEL_URL}")
        try:
            urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
            print("✅ Modèle téléchargé avec succès !")
        except Exception as e:
            print(f"❌ Erreur lors du téléchargement du modèle : {e}")
            raise e
    else:
        print("📦 Modèle déjà présent en local.")

if __name__ == "__main__":
    download_model_if_not_exists()