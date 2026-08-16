# import pandas as pd
# from evidently import Report
# from evidently.presets import DataDriftPreset

# reference_data = pd.read_csv('train.csv')[['Pclass', 'Sex', 'Age', 'Fare']]
# current_data = pd.read_csv('train.csv')[['Pclass', 'Sex', 'Age', 'Fare']].sample(100, random_state=42)

# report = Report(metrics=[DataDriftPreset()])
# report.run(reference_data=reference_data, current_data=current_data)
# report.save_html("rapport_data_drift.html")

# print("Rapport généré avec succès !")


#####     Adapter à seaborn

import seaborn as sns
from evidently import Report
from evidently.presets import DataDriftPreset

# 1. Charger les données de référence via Seaborn
reference_data = sns.load_dataset('titanic')[['pclass', 'sex', 'age', 'fare']].dropna()

# 2. Simuler des données reçues en production (avec une modification sur les tarifs)
current_data = reference_data.sample(100, random_state=42).copy()
current_data['fare'] = current_data['fare'] * 1.5

# 3. INITIALISER l'objet Report (L'étape manquante)
report = Report(metrics=[DataDriftPreset()])

# 4. Exécuter le rapport de Data Drift (Récupérer le résultat de l'évaluation)
my_eval = report.run(reference_data=reference_data, current_data=current_data)

# 5. Exporter le tableau de bord en HTML depuis l'objet d'évaluation
my_eval.save_html("rapport_data_drift.html")
print("Rapport de Data Drift généré avec succès : rapport_data_drift.html")

