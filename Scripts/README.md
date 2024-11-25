# README : Scripts pour la Modélisation et l'Entraînement de XGBoost

Ce sous-dossier contient les scripts nécessaires pour préparer les données, entraîner le modèle **XGBoost**, et effectuer l'évaluation des performances. Voici une brève description de chaque fichier Python dans ce dossier et de leur fonction respective.

---

## **Structure du Dossier `scripts/`**

Les scripts Python suivants sont présents dans ce sous-dossier :

1. **`processing.py`** : Préparation et nettoyage des données.
2. **`final.py`** : Transformation finale des données et ajout des indicateurs techniques.
3. **`modélisation.py`** : Entraînement du modèle **XGBoost**.
4. **`XGBOOST.py`** : Entraînement du modèle **XGBoost** et évaluation des performances.
5. **`XGBOOST_model.joblib`** : Modèle **XGBoost** sauvegardé après l'entraînement.

---

## **Description des Scripts**

### **1. `processing.py`**
Ce script est responsable de la **préparation initiale des données** :
- Chargement des données brutes.
- Nettoyage des données (gestion des valeurs manquantes, suppression des anomalies).
- Conversion des colonnes nécessaires et formatage pour les étapes suivantes de traitement.

### **2. `final.py`**
Ce script prend en charge la **transformation finale des données** :
- Calcul des **rendements journaliers** à partir des prix de clôture et des prix de veille.
- Ajout des **indicateurs techniques** comme les **moyennes mobiles**, les **bandes de Bollinger**, l'**ATR**, et le **RSI**.
- **Normalisation** et **standardisation** des données pour garantir une échelle uniforme avant l'entraînement du modèle.

### **3. `modélisation.py`**
Le script **`modélisation.py`** est responsable de l'entraînement du modèle **XGBoost** :
- Séparation des données en **train** (70%) et **test** (30%).
- Entraînement du modèle **XGBoost** avec les **hyperparamètres** définis dans le fichier.
- Sauvegarde du modèle dans le fichier **`XGBOOST_model.joblib`**.

### **4. `XGBOOST.py`**
Ce script contient les étapes suivantes :
- Entraînement du modèle **XGBoost** sur les données d'entraînement.
- **Évaluation du modèle** sur les données de test, calcul des **métriques de performance** (MSE, RMSE, \(R^2\)).
- Sauvegarde des résultats d'évaluation dans **`evaluation_results.txt`**.

### **5. `XGBOOST_model.joblib`**
Ce fichier contient le modèle **XGBoost** sauvegardé après son entraînement dans **`modélisation.py`**. Il peut être utilisé pour effectuer des prédictions sans réentraîner le modèle, en utilisant la méthode **`joblib.load()`**.

---

## **Utilisation des Scripts**

1. **Exécution de `processing.py`** : Ce script prépare les données brutes pour l'analyse et les nettoie pour les étapes suivantes.
2. **Exécution de `final.py`** : Ce script transforme les données et ajoute les indicateurs techniques nécessaires pour l'entraînement du modèle.
3. **Exécution de `modélisation.py`** : Ce script entraîne le modèle **XGBoost** sur les données transformées et sauvegarde le modèle dans **`XGBOOST_model.joblib`**.
4. **Exécution de `XGBOOST.py`** : Ce script charge le modèle, évalue les performances sur les données de test et sauvegarde les résultats d'évaluation dans **`evaluation_results.txt`**.

---

## **Résultats**

- **Modèle entraîné** : Le modèle **XGBoost** est sauvegardé dans **`XGBOOST_model.joblib`** et peut être utilisé pour des prédictions futures sans avoir besoin de réentraîner le modèle.
- **Évaluation des performances** : Les résultats de l'évaluation (MSE, RMSE, \(R^2\)) sont sauvegardés dans **`evaluation_results.txt`** et fournissent un aperçu de la performance du modèle sur les données de test.

---
