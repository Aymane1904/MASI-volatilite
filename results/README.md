# 📊 Prédiction du Risque Financier de l'Indice MASI

Ce dépôt contient les résultats complets et leur analyse détaillée issus de l'étude :  
**Prédiction du risque financier de l’indice MASI à l’aide de l’intelligence artificielle**.  
Cette étude met en avant l’utilisation du modèle **XGBoost** pour anticiper les fluctuations de volatilité de l’indice MASI.

---

## 🌟 Objectifs
1. **Évaluer la performance** de l'algorithme XGBoost par rapport aux méthodes traditionnelles de prédiction.
2. **Comprendre la dynamique de la volatilité** pour améliorer la gestion des risques financiers.
3. **Fournir des recommandations** sur l'utilisation de l'intelligence artificielle dans les stratégies financières.

---

## 🚀 Résultats et Interprétation

### 📈 Métriques de Performance
Les performances du modèle XGBoost sont évaluées à l'aide des métriques suivantes :
| **Métrique**               | **Valeur**                   | **Interprétation**                                   |
|----------------------------|-----------------------------|-----------------------------------------------------|
| **MSE (Mean Squared Error)** | `0.00018097`                | Une erreur quadratique moyenne très faible, montrant la précision du modèle. |
| **RMSE (Root Mean Squared Error)** | `0.01345`              | Faibles écarts entre les valeurs réelles et prédites. |
| **MAE (Mean Absolute Error)** | `0.00671`                | Les erreurs absolues moyennes sont négligeables.    |
| **R² (Coefficient de Détermination)** | `0.93`         | Le modèle explique 93 % de la variance des données. |

#### Interprétation des résultats :
- Les métriques montrent une capacité exceptionnelle à prédire la volatilité avec précision.
- Quelques **divergences mineures** peuvent être attribuées à des fluctuations imprévues dans les données d'entrée.

---

### 🔍 Analyse Visuelle et Discussion

#### 1. Comparaison des Volatilités Réelles et Prédites
- Les prédictions du modèle suivent de près les valeurs réelles.
- Les **pics et creux** sont bien capturés, indiquant une bonne compréhension des tendances du marché.
- **Écarts mineurs** : Ces divergences mettent en lumière la complexité de certains comportements de marché que le modèle pourrait affiner.

#### 2. Distribution des Résidus
- **Symétrie autour de zéro** : Indique une absence de biais systématique.
- **Distribution normale** : Confirme que les erreurs sont bien réparties, ce qui est une caractéristique souhaitable pour des prédictions fiables.

#### 3. Scores de Validation Croisée (R²)
- La stabilité des scores (autour de 0.93) confirme la généralisation efficace du modèle sur des données non vues.
- Une **légère variance** observée sur certains plis pourrait nécessiter une amélioration des données d'entraînement.

#### 4. Courbe des Résidus
- Les résidus sont largement concentrés autour de zéro, mais des **valeurs aberrantes** sont présentes.
- Ces anomalies pourraient provenir de fluctuations extrêmes ou de limitations dans la modélisation.

---

## 💡 Conclusions et Recommandations

### Conclusions
1. **Performance globale excellente** :
   - XGBoost surpasse les méthodes traditionnelles avec des prédictions précises et fiables.
   - Les erreurs sont bien réparties et faibles, indiquant une bonne robustesse du modèle.
2. **Robustesse face à la volatilité** :
   - Le modèle capture efficacement les tendances principales de volatilité, même dans des scénarios complexes.
3. **Limites observées** :
   - Quelques valeurs aberrantes suggèrent une optimisation possible pour les scénarios extrêmes.

### Recommandations
1. **Optimiser les hyperparamètres** :
   - Approfondir l'analyse pour affiner les paramètres du modèle.
2. **Renforcer le prétraitement des données** :
   - Gérer les anomalies et intégrer davantage de données historiques pour une meilleure représentativité.
3. **Explorer des approches hybrides** :
   - Combiner XGBoost avec d'autres modèles (par exemple, réseaux neuronaux) pour des performances accrues.

