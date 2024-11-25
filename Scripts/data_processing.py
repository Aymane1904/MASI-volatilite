import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os

# =======================================
# Configuration des chemins de fichiers
# =======================================
# Chemin du fichier d'entrée
input_file = "../data/Data_vierge.xlsx"
# Chemin du fichier de sortie
output_file = "../data/data_vierge_transformed.xlsx"


# =======================================
# Chargement des données
# =======================================
def load_data(file_path):
    """Charge le fichier Excel dans un DataFrame."""
    try:
        print("Chargement des données...")
        data = pd.read_excel(file_path)
        print("Données chargées avec succès !")
        return data
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        exit()
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        exit()

# =======================================
# Nettoyage des données
# =======================================
def clean_data(data):
    """
    Effectue le nettoyage des données :
    1. Traitement des valeurs manquantes.
    2. Suppression des doublons.
    3. Traitement des valeurs aberrantes.
    """
    print("\n=== Nettoyage des données ===")

    # 1. Traitement des valeurs manquantes
    print("Traitement des valeurs manquantes...")
    data.fillna(data.mean(numeric_only=True), inplace=True)

    # 2. Suppression des doublons
    print("Suppression des doublons...")
    before_dedup = data.shape[0]
    data = data.drop_duplicates()
    after_dedup = data.shape[0]
    print(f"Nombre de doublons supprimés : {before_dedup - after_dedup}")

    # 3. Traitement des valeurs aberrantes
    print("Traitement des valeurs aberrantes...")
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((data[col] < lower_bound) | (data[col] > upper_bound)).sum()
        print(f"  - {col}: {outliers} valeurs aberrantes corrigées.")
        data[col] = np.where(data[col] < lower_bound, lower_bound, data[col])
        data[col] = np.where(data[col] > upper_bound, upper_bound, data[col])

    return data

# =======================================
# Normalisation des données
# =======================================
def normalize_data(data):
    """
    Normalise les colonnes numériques avec MinMaxScaler.
    """
    print("\n=== Normalisation des données ===")
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    scaler = MinMaxScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    print("Normalisation effectuée.")
    return data

# =======================================
# Sauvegarde des données
# =======================================
def save_data(data, file_path):
    """
    Sauvegarde le DataFrame dans un fichier Excel.
    """
    try:
        data.to_excel(file_path, index=False)
        print(f"\nDonnées nettoyées et transformées sauvegardées avec succès : {file_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données : {e}")
        exit()

# =======================================
# Pipeline principal
# =======================================
if __name__ == "__main__":
    print("=== Lancement du pipeline de nettoyage des données ===")

    # Étape 1 : Charger les données
    data = load_data(input_file)

    # Étape 2 : Nettoyer les données
    data_cleaned = clean_data(data)

    # Étape 3 : Normaliser les données
    data_normalized = normalize_data(data_cleaned)

    # Étape 4 : Sauvegarder les données nettoyées
    save_data(data_normalized, output_file)

    print("\n=== Pipeline terminé avec succès ===")
