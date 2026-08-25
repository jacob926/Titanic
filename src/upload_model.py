import os
from huggingface_hub import HfApi

# Définir le chemin absolu vers Model.pkl à la racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "Model.pkl")

HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = "jacob926/titanic-model"  # ⚠️ Remplace par ton pseudo/repo Hugging Face

def upload_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model.pkl introuvable à l'emplacement : {MODEL_PATH}")

    if not HF_TOKEN:
        print("⚠️ HF_TOKEN non configuré. L'upload sur Hugging Face est ignoré.")
        return

    print("📤 Envoi du modèle vers Hugging Face...")
    api = HfApi()
    
    # Création du repository s'il n'existe pas encore
    api.create_repo(repo_id=REPO_ID, repo_type="model", exist_ok=True, token=HF_TOKEN)
    
    # Upload du fichier .pkl
    api.upload_file(
        path_or_fileobj=MODEL_PATH,
        path_in_repo="Model.pkl",
        repo_id=REPO_ID,
        repo_type="model",
        token=HF_TOKEN
    )
    print("✅ Modèle envoyé avec succès sur Hugging Face !")

if __name__ == "__main__":
    upload_model()