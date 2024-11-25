import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Chemin du fichier avec les variables calculées
file_path = r"C:\Users\HP\Desktop\MASI PRED\Data Git\Data\data_with_indicators.xlsx"

# Charger les données
print("Chargement des données transformées...")
data = pd.read_excel(file_path)

# Vérification des colonnes disponibles
print("\nColonnes disponibles :")
print(data.columns)

# ===================================================
# Étape 1 : Sélection des variables pertinentes
# ===================================================
# Définissez les caractéristiques (features) et la cible (target)
features = [
    'RENDEMENT_JOURNALIER', 'SMA', 'Bollinger_Haute', 'Bollinger_Basse',
    'RSI', 'ATR'
]  # Adaptez selon vos besoins
target = 'Volatilite'  # La volatilité est la cible

# Vérifiez si les colonnes existent
if not all(col in data.columns for col in features + [target]):
    print("Erreur : Certaines colonnes nécessaires sont absentes.")
    exit()

X = data[features]  # Caractéristiques
y = data[target]    # Cible

# ===================================================
# Étape 2 : Traitement des valeurs infinies et manquantes
# ===================================================
print("\nVérification et traitement des valeurs infinies ou manquantes...")

# Remplacer les valeurs infinies par NaN
X.replace([np.inf, -np.inf], np.nan, inplace=True)
y.replace([np.inf, -np.inf], np.nan, inplace=True)

# Vérification des valeurs infinies
print("Valeurs infinies dans X :", np.isinf(X).sum().sum())
print("Valeurs infinies dans y :", np.isinf(y).sum().sum())

# Vérification des valeurs manquantes
print("Valeurs manquantes dans X :", X.isnull().sum().sum())
print("Valeurs manquantes dans y :", y.isnull().sum().sum())

# Remplacer les NaN par la moyenne (ou une autre stratégie)
X.fillna(X.mean(), inplace=True)
y.fillna(y.mean(), inplace=True)

# Vérification après traitement
print("Valeurs manquantes dans X après traitement :", X.isnull().sum().sum())
print("Valeurs manquantes dans y après traitement :", y.isnull().sum().sum())

# ===================================================
# Étape 3 : Division des données en train/test
# ===================================================
print("\nDivision des données en ensembles d'entraînement et de test (30% pour test)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"Taille de l'ensemble d'entraînement : {X_train.shape}")
print(f"Taille de l'ensemble de test : {X_test.shape}")

# ===================================================
# Étape 4 : Normalisation des données
# ===================================================
print("\nNormalisation des données...")
scaler = StandardScaler()

# Appliquer la normalisation sur X_train et X_test
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convertir en DataFrame pour une sauvegarde claire
X_train_scaled = pd.DataFrame(X_train_scaled, columns=features)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=features)

# ===================================================
# Étape 5 : Sauvegarde des données prêtes pour la modélisation
# ===================================================
output_train_path = r"C:\Users\HP\Desktop\MASI PRED\Data Git\Data\train_data.xlsx"
output_test_path = r"C:\Users\HP\Desktop\MASI PRED\Data Git\Data\test_data.xlsx"

try:
    # Combiner les caractéristiques et la cible pour sauvegarder
    train_data = pd.concat([X_train_scaled, y_train.reset_index(drop=True)], axis=1)
    test_data = pd.concat([X_test_scaled, y_test.reset_index(drop=True)], axis=1)
    
    train_data.to_excel(output_train_path, index=False)
    test_data.to_excel(output_test_path, index=False)
    
    print(f"\nDonnées d'entraînement sauvegardées dans : {output_train_path}")
    print(f"Données de test sauvegardées dans : {output_test_path}")
except Exception as e:
    print("Erreur lors de la sauvegarde des fichiers :", e)

print("\nPréparation des données terminée.")
