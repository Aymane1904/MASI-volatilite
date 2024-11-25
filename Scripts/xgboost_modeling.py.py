import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import os

# Chemin des fichiers de données
train_path = r"C:\Users\HP\Desktop\MASI PRED\Data Git\Data\train_data.xlsx"
test_path = r"C:\Users\HP\Desktop\MASI PRED\Data Git\Data\test_data.xlsx"

# Charger les données
print("Chargement des données...")
train_data = pd.read_excel(train_path)
test_data = pd.read_excel(test_path)

# Séparer les caractéristiques (X) et la cible (y)
X_train = train_data.drop(columns=['Volatilite'])  # Caractéristiques
y_train = train_data['Volatilite']  # Cible

X_test = test_data.drop(columns=['Volatilite'])  # Caractéristiques
y_test = test_data['Volatilite']  # Cible

# Configuration et entraînement du modèle XGBoost
print("\nConfiguration et entraînement du modèle XGBoost...")

# Ajustement des hyperparamètres
model = xgb.XGBRegressor(
    alpha=0.1,                # Régularisation légère pour éviter le surajustement
    colsample_bytree=0.5,     # 50% d'échantillonnage des colonnes par arbre
    learning_rate=0.05,       # Réduction du taux d'apprentissage pour plus de précision
    max_depth=6,              # Profondeur légèrement augmentée pour capturer plus de complexité
    n_estimators=500,         # Augmenter le nombre d'arbres pour un meilleur ajustement
    subsample=0.9,            # 90% d'échantillonnage des lignes pour plus de robustesse
    random_state=42           # Graine pour la reproductibilité
)

# Entraîner le modèle
model.fit(X_train, y_train)

# Prédire les résultats sur l'ensemble de test
print("\nPrédiction sur l'ensemble de test...")
y_pred = model.predict(X_test)

# Évaluation du modèle
print("\nÉvaluation des performances du modèle...")
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Afficher les résultats
print("=== Résultats ===")
print(f"Mean Squared Error (MSE): {mse:.8f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.8f}")
print(f"Mean Absolute Error (MAE): {mae:.8f}")
print(f"Coefficient of Determination (R^2): {r2:.8f}")

# Sauvegarder le modèle
print("\nSauvegarde du modèle...")
model_dir = r"C:\Users\HP\Desktop\MASI PRED\Model"
model_path = os.path.join(model_dir, "xgboost_model_optimized.pkl")

if not os.path.exists(model_dir):
    os.makedirs(model_dir)
    print(f"Dossier créé : {model_dir}")

joblib.dump(model, model_path)
print(f"Modèle sauvegardé dans : {model_path}")

# Importance des caractéristiques
print("\nAffichage de l'importance des caractéristiques...")
xgb.plot_importance(model, importance_type='weight')
import matplotlib.pyplot as plt
plt.title("Importance des caractéristiques")
plt.show()
