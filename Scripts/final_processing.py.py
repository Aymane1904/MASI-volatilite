import pandas as pd
import numpy as np

# Chemin du fichier transformé
file_path = r"C:\Users\HP\Desktop\MASI PRED\Data Git\Data\data_vierge_transformed.xlsx"

# Charger les données transformées
print("Chargement des données transformées...")
data = pd.read_excel(file_path)

# Vérifier les colonnes disponibles
print("Colonnes disponibles :")
print(data.columns)

# Vérifiez si les colonnes nécessaires sont présentes
required_columns = ['COURS_CLOTURE', 'COURS_PLUS_HAUT', 'COURS_PLUS_BAS', 'COURS_VEILLE']
if not all(col in data.columns for col in required_columns):
    print("Erreur : Les colonnes nécessaires sont manquantes. Assurez-vous d'avoir 'COURS_CLOTURE', 'COURS_PLUS_HAUT', 'COURS_PLUS_BAS', et 'COURS_VEILLE'.")
    exit()

# ===================================================
# Calcul des variables
# ===================================================

# Rendements journaliers (Daily Returns)
print("Calcul des rendements journaliers...")
data['RENDEMENT_JOURNALIER'] = (data['COURS_CLOTURE'] - data['COURS_VEILLE']) / data['COURS_VEILLE']

# Moyenne mobile simple (SMA)
print("Calcul des moyennes mobiles simples (SMA)...")
window = 20  # Par exemple, SMA sur 20 séances
data['SMA'] = data['COURS_CLOTURE'].rolling(window=window).mean()

# Bandes de Bollinger
print("Calcul des bandes de Bollinger...")
data['Bollinger_Haute'] = data['SMA'] + 2 * data['COURS_CLOTURE'].rolling(window=window).std()
data['Bollinger_Basse'] = data['SMA'] - 2 * data['COURS_CLOTURE'].rolling(window=window).std()

# Volatilité (Rolling Standard Deviation)
print("Calcul de la volatilité (Rolling Std)...")
data['Volatilite'] = data['COURS_CLOTURE'].rolling(window=window).std()

# RSI (Relative Strength Index)
print("Calcul du RSI...")
delta = data['COURS_CLOTURE'].diff()
gain = np.where(delta > 0, delta, 0)
loss = np.where(delta < 0, -delta, 0)
avg_gain = pd.Series(gain).rolling(window=14).mean()
avg_loss = pd.Series(loss).rolling(window=14).mean()
rs = avg_gain / avg_loss
data['RSI'] = 100 - (100 / (1 + rs))

# ATR (Average True Range)
print("Calcul de l'ATR...")
data['TR'] = np.maximum(data['COURS_PLUS_HAUT'] - data['COURS_PLUS_BAS'], 
                        np.maximum(abs(data['COURS_PLUS_HAUT'] - data['COURS_CLOTURE'].shift(1)), 
                                   abs(data['COURS_PLUS_BAS'] - data['COURS_CLOTURE'].shift(1))))
data['ATR'] = data['TR'].rolling(window=14).mean()

# ===================================================
# Sauvegarder les résultats
# ===================================================
output_path = r"C:\Users\HP\Desktop\MASI PRED\Data Git\Data\data_with_indicators.xlsx"
try:
    data.to_excel(output_path, index=False)
    print(f"Données avec variables calculées sauvegardées dans : {output_path}")
except Exception as e:
    print("Erreur lors de la sauvegarde des données :", e)

print("Calculs terminés.")
