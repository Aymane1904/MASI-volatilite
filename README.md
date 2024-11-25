# MASI-volatilité - Prédiction du Risque Financier de l'Indice MASI à l'Aide de l'Intelligence Artificielle

## Contexte

La volatilité des marchés financiers représente un risque majeur pour les investisseurs et les institutions financières, et prédire cette volatilité est essentiel pour une gestion optimale des risques. Ce projet a pour objectif principal de prédire la volatilité de l'indice **MASI** (Moroccan All Shares Index) de la **Bourse de Casablanca** en utilisant des techniques avancées de **Machine Learning**. L'algorithme **XGBoost** est particulièrement utilisé pour sa capacité à traiter des volumes massifs de données et à s'adapter aux fluctuations complexes du marché.

Le **MASI** est un indice boursier qui reflète la performance globale des entreprises cotées en bourse à Casablanca. En raison de sa sensibilité aux influences économiques mondiales, nationales, ainsi qu’aux fluctuations des matières premières, la volatilité de cet indice constitue un défi important pour les investisseurs.

## Problématique de Recherche

Les marchés financiers sont souvent caractérisés par une forte volatilité, rendant les décisions d'investissement particulièrement complexes et risquées. L’indice **MASI**, qui regroupe les entreprises cotées à la **Bourse de Casablanca**, reflète la performance économique du pays. Cependant, cet indice est également influencé par une multitude de facteurs économiques, géopolitiques et de marchés mondiaux, ce qui contribue à des fluctuations importantes dans ses valeurs.

La **problématique de recherche** que ce projet cherche à résoudre est la suivante :
> **Comment prédire la volatilité de l’indice MASI afin de mieux anticiper les risques financiers et d’offrir des stratégies d’investissement plus adaptées ?**

En d'autres termes, cette étude cherche à répondre à la question de savoir si l’utilisation de **modèles d'apprentissage automatique**, comme **XGBoost**, peut apporter une meilleure précision dans la prévision des périodes de forte volatilité de l'indice MASI par rapport aux méthodes traditionnelles de gestion des risques. La réponse à cette question pourrait transformer la manière dont les investisseurs évaluent et réagissent à la volatilité des marchés marocains.

Les objectifs de cette recherche sont :
1. Développer un modèle prédictif de volatilité basé sur des données historiques de l’indice MASI.
2. Analyser l’impact des indicateurs techniques comme **RSI**, **ATR**, et **Moyenne Mobile** dans l’amélioration des prédictions.
3. Comparer les performances du modèle d'apprentissage automatique avec les méthodes classiques de gestion des risques financiers.



Les hypothèses principales de la recherche sont :
1. Les modèles d'IA, notamment **XGBoost**, surpassent les approches traditionnelles en termes de précision prédictive et de réactivité.
2. L'intégration d'indicateurs techniques tels que **RSI**, **ATR**, et **Bollinger Bands** améliore les performances du modèle.
3. L'adoption de l'IA dans la prédiction des risques financiers permet des stratégies d'investissement plus réactives et plus robustes.


## Méthodologie

### 1. **Collecte des Données**

Les données utilisées dans ce projet proviennent de l'indice **MASI** et comprennent des variables telles que les prix d'ouverture, de clôture, le plus haut, le plus bas, ainsi que des indicateurs techniques calculés sur la base des données historiques. Ces données ont été obtenues à partir de sources financières fiables.

### 2. **Préparation des Données**

Les données ont été préparées en plusieurs étapes :
- **Nettoyage des Données :** Elimination des valeurs manquantes et des outliers.
- **Transformation des Données :** Calcul des rendements et ajout des indicateurs techniques.
- **Normalisation et Standardisation :** Pour permettre une meilleure comparaison entre les variables.

### 3. **Modélisation**

Nous avons utilisé **XGBoost**, un modèle de **gradient boosting** reconnu pour sa capacité à traiter de grandes quantités de données tout en évitant le sur-apprentissage grâce à la régularisation. L’optimisation des hyperparamètres a été réalisée en utilisant une recherche sur grille pour ajuster des paramètres comme le **learning_rate**, le **nombre d'arbres**, et la **profondeur des arbres**.

### 4. **Évaluation du Modèle**

Le modèle a été évalué sur la base des **métriques suivantes** :
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² (Coefficient de détermination)**

Les résultats montrent que le modèle XGBoost a un **R² de 0.93**, ce qui indique une excellente capacité à prédire la volatilité de l'indice MASI. De plus, les indicateurs techniques ont été fortement corrélés avec la volatilité, ce qui confirme leur pertinence dans le modèle.

### 5. **Optimisation des Hyperparamètres**

Les principaux hyperparamètres optimisés incluent :
- **Learning Rate** : Ajuste la vitesse d’apprentissage du modèle.
- **Number of Estimators (n_estimators)** : Détermine le nombre d'arbres dans le modèle.
- **Max Depth** : Contrôle la profondeur maximale de chaque arbre.

## Résultats

L'algorithme **XGBoost** a démontré une performance remarquable dans la prédiction de la volatilité de l'indice MASI, surpassant les méthodes traditionnelles. Les résultats ont été validés par des **scores de validation croisée**, avec un **R² de 0.93**, ce qui confirme l’efficacité du modèle dans un environnement de marché volatile. Les **indicateurs techniques** ont joué un rôle crucial dans l'amélioration de la précision des prédictions.

Les visualisations suivantes illustrent les résultats obtenus :
- **Résidu Courbe** : Montre les résidus du modèle pour vérifier la qualité de l'ajustement.
- **Distribution des Résidus** : Permet d'évaluer la normalité des erreurs de prédiction.
- **Prédictions vs Réel** : Graphique comparant les prédictions du modèle et les valeurs réelles observées.

## Conclusion

Cette étude démontre que l'intégration des **techniques d'intelligence artificielle** et, spécifiquement, de **XGBoost**, dans l'analyse et la prédiction des risques financiers, offre des outils puissants pour les investisseurs. Le modèle développé permet non seulement de prédire plus efficacement la volatilité de l'indice MASI, mais aussi de proposer des stratégies d'investissement plus réactives et informées, basées sur des données.

Les résultats suggèrent que l'utilisation de **l'intelligence artificielle** dans la gestion des risques financiers est une approche incontournable pour améliorer la prise de décision dans un environnement de marché de plus en plus complexe et volatile.

## Contact

Si vous avez des questions concernant ce projet ou souhaitez en savoir plus, vous pouvez me contacter via [GitHub](https://github.com/Aymane1904) ou par e-mail.

---

### **Explication de la Structure du README :**
1. **Introduction générale** : Présentation succincte du contexte du projet.
2. **Objectifs et hypothèses** : Définition des objectifs du projet et des hypothèses de recherche.
3. **Méthodologie** : Explication détaillée de la collecte, préparation et modélisation des données.
4. **Résultats** : Présentation des résultats obtenus, avec les performances du modèle et les visualisations.
5. **Conclusion** : Résumé des principales conclusions et de l'impact de l'IA dans la gestion des risques financiers.

---

