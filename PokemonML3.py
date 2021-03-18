# Appliquer les différents modèles de ML sur le df

import pandas as pd

stats_pokedex = pd.read_csv("datas/stats_pokedex.csv", delimiter='\t')
stats_pokedex = stats_pokedex.dropna(axis=0, how="any")

# Définir les variables X et y

X = stats_pokedex.iloc[:, 5:12].values
y = stats_pokedex.iloc[:, -1].values

# Découpage du jeu de données

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1234)

# Appliquer le modèle de régression linéaire

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
algorithme = LinearRegression()
algorithme.fit(X_train, y_train)

predictions = algorithme.predict(X_val)
precision_apprentissage = algorithme.score(X_train, y_train)
precision = r2_score(y_val, predictions)

print(">> ---------- REGRESSION LINÉAIRE ----------")
print(">> Precision apprentissage = "+str(precision_apprentissage))
print(">> Precision validation = "+str(precision))
print(">> -----------------------------------------")

# Appliquer le modèle de Decision Tree

from sklearn.tree import DecisionTreeRegressor
algorithme2 = DecisionTreeRegressor(random_state=1234)

algorithme2.fit(X_train, y_train)
predictions2 = algorithme2.predict(X_val)
precision2_apprentissage = algorithme2.score(X_train, y_train)
precision2 = r2_score(y_val, predictions2)

print(">> ---------- Decision Tree Regressor ----------")
print(">> Precision apprentissage = "+str(precision2_apprentissage))
print(">> Precision validation = "+str(precision2))
print(">> ---------------------------------------------")

# Appliquer le modèle de Random Forest

from sklearn.ensemble import RandomForestRegressor
algorithme3 = RandomForestRegressor(random_state=1234)

algorithme3.fit(X_train, y_train)
predictions3 = algorithme3.predict(X_val)
precision3_apprentissage = algorithme3.score(X_train, y_train)
precision3 = r2_score(y_val, predictions3)

print(">> ---------- Random Forest Regressor ----------")
print(">> Precision apprentissage = "+str(precision3_apprentissage))
print(">> Precision validation = "+str(precision3))
print(">> ---------------------------------------------")

# Sauvegarder le meilleur modèle

#import joblib
#fichier = 'Modele/modele_pokemon.mod'
#joblib.dump(algorithme3, fichier)
