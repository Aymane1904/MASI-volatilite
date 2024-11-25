# Données pour l'analyse et la modélisation de la volatilité de l'indice MASI

Ce dossier contient l'ensemble des données utilisées et générées au cours du projet visant à modéliser la volatilité de l'indice MASI à l'aide de techniques avancées de Machine Learning. Chaque étape de la transformation des données est documentée pour garantir la traçabilité et la reproductibilité des résultats.

---

## **Structure du dossier**

Le dossier `data/` est organisé en plusieurs sous-dossiers pour refléter les étapes méthodologiques de préparation des données :

1. **`raw/`** : Données brutes.
2. **`cleaned/`** : Données nettoyées.
3. **`transformed/`** : Données standardisées et normalisées, prêtes pour la modélisation.
4. **`indicators/`** : Données enrichies avec des indicateurs techniques.

---

## **Description des sous-dossiers**

### **1. raw/**
Ce sous-dossier contient les **données brutes** récupérées directement depuis des sources fiables, sans aucune modification ni traitement.

- **Source des données :**
  Les données ont été extraites du site officiel de la Bourse de Casablanca.

- **Contenu :**
  - `raw_data.xlsx` : Inclut les colonnes suivantes :
    - `SEANCE` : Date de la séance.
    - `INDICE` : Nom de l'indice.
    - `COURS_CLOTURE` : Prix de clôture.
    - `COURS_PLUS_HAUT` : Prix le plus haut atteint pendant la séance.
    - `COURS_PLUS_BAS` : Prix le plus bas atteint pendant la séance.
    - `COURS_OUVERTURE` : Prix d'ouverture.
    - `COURS_VEILLE` : Prix de clôture de la séance précédente.
    - `VARIATION` : Variation du prix de clôture par rapport à la séance précédente.

---

**Note sur la Taille des Données:** 
En raison de la taille importante des données, qui couvrent la période de 2008 à 2023, seules des parties échantillons des données ont été fournies dans ce projet. Ces échantillons couvrent des périodes représentatives, assurant ainsi la pertinence et l'exactitude des analyses sans inclure l'intégralité du dataset.

Pour accéder aux données complètes, vous pouvez vous référer à la source originale de la Bourse de Casablanca ou me contacter pour plus d'informations.

---

### **2. cleaned/**
Ce sous-dossier contient les données après le **nettoyage**, étape essentielle pour garantir leur qualité et leur pertinence pour l'analyse.

- **Étapes de nettoyage appliquées :**

   - **Détection des valeurs aberrantes (outliers)** :
     - Utilisation de la méthode des IQR (Interquartile Range) pour identifier les valeurs en dehors de \( [Q1 - 1.5*IQR, Q3 + 1.5*IQR] \).
     - Exemple : Élimination des variations de cours > 20% en une seule journée (erreurs fréquentes dans les données historiques).

   - **Traitement des données manquantes** :
     - Remplacement par interpolation linéaire pour les séries temporelles.
     - Suppression des lignes lorsque les données manquantes dépassent 20% d'une observation.

###  **Nettoyage Avancé**
   - **Suppression des doublons** :
     - Identification basée sur la date et les indicateurs clés (cours et volume).

   - **Formatage des dates** :
     - Uniformisation des formats de date en `YYYY-MM-DD` pour une manipulation cohérente.

- **Contenu :**
  - `cleaned_data.xlsx` : Les mêmes colonnes que dans les données brutes, mais nettoyées et prêtes pour l'enrichissement ou la transformation.

---

### **3. transformed/**
Ce sous-dossier contient les données après **standardisation** et **normalisation**, deux étapes essentielles pour préparer les données à la modélisation.

- **Étapes de transformation appliquées :**
  1. **Standardisation :**
     - Les données quantitatives ont été centrées autour de leur moyenne avec un écart-type de 1.
     - Utilisation de la méthode `StandardScaler`.
  2. **Normalisation :**
     - Chaque valeur a été ramenée à une échelle uniforme pour garantir une pondération équitable lors de l'entraînement des modèles.
     - Appliquée à toutes les caractéristiques pertinentes.

- **Pourquoi la transformation ?**
  - Ces transformations assurent une convergence plus rapide et une meilleure performance des modèles de Machine Learning, notamment XGBoost, qui est sensible aux différences d'échelle entre les variables.

- **Contenu :**
  - `transformed_data.xlsx` :
    - Données standardisées et normalisées, prêtes pour la modélisation.

---

### **4. indicators/**
Ce sous-dossier contient les données enrichies avec des **indicateurs techniques**, qui jouent un rôle clé dans l'analyse de la volatilité.

 - **Indicateurs de volatilité** :
     - Calcul de l’écart-type des variations journalières sur une fenêtre mobile de 15 jours.
- **Indicateurs techniques ajoutés :**
  1. **Moyenne Mobile Simple (SMA)** :
     - Fournit une moyenne des prix de clôture sur une période donnée.
  2. **Bandes de Bollinger** :
     - Calculées à partir de la SMA, elles donnent une idée de la volatilité et des niveaux de surachat ou survente.
  3. **RSI (Relative Strength Index)** :
     - Indicateur de momentum pour évaluer la vitesse et l'amplitude des mouvements des prix.
  4. **ATR (Average True Range)** :
     - Mesure de la volatilité quotidienne moyenne.

- **Contenu :**
  - `data_with_indicators.xlsx` :
    - Données enrichies, contenant les colonnes d'origine ainsi que les indicateurs techniques calculés.

---

## **Méthodologie de préparation des données**

1. **Nettoyage initial :**
   - Identification et correction des données manquantes et aberrantes.
2. **Standardisation et normalisation :**
   - Centrage et réduction des variables quantitatives.
   - Mise à l'échelle uniforme des caractéristiques.
3. **Enrichissement des données :**
   - Calcul d'indicateurs techniques pour capturer la volatilité et les dynamiques de marché.

Chaque étape a été réalisée en respectant les standards de qualité des données, garantissant ainsi leur pertinence pour la modélisation.

---

## **Objectif des données**

Ces données constituent la base de l'analyse et de la modélisation du risque financier de l'indice MASI. Elles permettent :
1. **D'analyser les dynamiques historiques de l'indice.**
2. **De développer des modèles prédictifs robustes pour anticiper la volatilité.**
3. **De tester et évaluer les performances des algorithmes, notamment XGBoost.**

---

## **Utilisation des fichiers**

1. **Pour visualiser les données brutes :**
   Accédez au sous-dossier `raw/`.
2. **Pour effectuer une analyse statistique :**
   Utilisez les données nettoyées disponibles dans `cleaned/`.
3. **Pour la modélisation et le Machine Learning :**
   - Les fichiers transformés (`transformed/`) et enrichis (`indicators/`) sont recommandés.

---

## **Contact**

Pour toute question ou clarification concernant les données, veuillez me contacter via GitHub ou e-mail.
