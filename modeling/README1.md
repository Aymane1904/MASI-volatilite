# Modélisation du Risque Financier de l'Indice MASI avec XGBoost

Ce dossier contient les fichiers et les résultats liés à la modélisation du **risque financier de l'indice MASI** (Moroccan All Shares Index) à l'aide du modèle **XGBoost**, un algorithme de **Machine Learning** particulièrement efficace pour les séries temporelles financières.

L'objectif du modèle est de prédire la **volatilité de l'indice MASI**, un indicateur clé de la Bourse de Casablanca. Nous avons utilisé différentes techniques pour transformer, nettoyer, et modéliser les données afin de prédire les fluctuations futures de l'indice.

---

## **Structure du Dossier**

Le dossier `modeling/` contient les éléments suivants :

1. **`train_data.xlsx`** : Données d'entraînement transformées et prêtes pour l'entraînement du modèle.
2. **`test_data.xlsx`** : Données de test utilisées pour évaluer les performances du modèle.
3. **`xgboost/`** : 
   - **`xgboost_model.pkl`** : Modèle XGBoost sauvegardé après l'entraînement.
   - **`evaluation_results.txt`** : Résumé des performances du modèle (MSE, RMSE, \(R^2\)).
4. **Scripts Python** :
   - **`data_preparation.py`** : Préparation des données avant l'entraînement du modèle.
   - **`modeling_xgboost.py`** : Entraînement et évaluation du modèle XGBoost.
   - **`visualization.py`** (facultatif) : Visualisation des résultats et des performances du modèle.

---

## **Objectifs du Modèle**

Le modèle développé dans ce projet vise à prédire la **volatilité de l'indice MASI** en utilisant les données historiques de l'indice et divers **indicateurs techniques** comme les moyennes mobiles, les bandes de Bollinger, l'ATR, le RSI, etc.

Les étapes principales incluent :
1. **Préparation des données** : Nettoyage et transformation des données.
2. **Entraînement du modèle** : Utilisation du modèle **XGBoost** pour prédire la volatilité.
3. **Évaluation du modèle** : Mesure de la performance avec des métriques standard.

---

## **Préparation des Données**

Les données utilisées dans ce projet ont été transformées et nettoyées pour être prêtes à l'entraînement du modèle.

1. **Nettoyage des données** :
   - Les valeurs manquantes ont été traitées par **remplissage avec la moyenne**.
   - Les anomalies et valeurs extrêmes ont été identifiées et gérées pour éviter le biais.
   
2. **Transformation des données** :
   - Calcul des **rendements journaliers**, des **moyennes mobiles**, des **bandes de Bollinger**, du **RSI**, et de l'**ATR**.
   - Les données ont été **normalisées** et **standardisées** pour garantir que toutes les caractéristiques aient une échelle similaire.

---

## **Division des Données : 70% Entraînement, 30% Test**

Les données ont été séparées en deux ensembles :
- **70% des données** ont été utilisées pour l'**entraînement** du modèle.
- **30% des données** ont été utilisées pour tester et **évaluer** les performances du modèle.

Cette division est essentielle pour garantir que le modèle peut **généraliser** et qu'il ne soit pas trop spécifique aux données d'entraînement.

---

## **Réglage des Hyperparamètres**

Le modèle **XGBoost** comporte plusieurs hyperparamètres qui influencent directement sa performance. Nous avons ajusté ces hyperparamètres pour maximiser la performance tout en évitant le surapprentissage.

### **Hyperparamètres principaux réglés**

- **`learning_rate` (eta)** : 0.1
  - Un taux d'apprentissage relativement faible pour assurer un apprentissage progressif sans surapprentissage.
- **`max_depth`** : 5
  - Profondeur des arbres pour éviter un modèle trop complexe et susceptible de surajuster les données.
- **`n_estimators`** : 100
  - Nombre d'arbres dans le modèle.
- **`subsample`** : 0.8
  - Fraction des données utilisées pour chaque arbre, afin de réduire le risque de surapprentissage.
- **`colsample_bytree`** : 0.8
  - Fraction des caractéristiques utilisées pour chaque arbre.
- **`alpha` (L1 regularization)** : 0.5
  - Aide à éviter un surapprentissage en régularisant les poids des variables.
- **`lambda` (L2 regularization)** : 1.0
  - Rôle similaire à `alpha` pour régulariser les poids du modèle.
- **`gamma`** : 0
  - Ce paramètre contrôle la complexité des arbres.

### **Méthodologie de Réglage des Hyperparamètres**

Les hyperparamètres ont été ajustés via une **recherche empirique**, combinée avec une **validation croisée K-fold (K=5)** pour évaluer les performances du modèle de manière robuste. Cela a permis de s'assurer que le modèle ne surapprend pas et qu'il généralise bien aux nouvelles données.

---

## **Entraînement du Modèle XGBoost**

Une fois les hyperparamètres définis, le modèle **XGBoost** a été entraîné sur les **données d'entraînement** (70% des données). Le processus a inclus :
- La création des arbres de décision sur les caractéristiques transformées.
- L'ajustement des paramètres pour maximiser la précision de la prédiction de la volatilité.

Le modèle a été sauvegardé sous le nom de **`xgboost_model.pkl`** pour une utilisation future.



