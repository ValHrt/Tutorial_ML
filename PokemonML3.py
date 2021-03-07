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
precision = r2_score(y_val, predictions)

print(">> ---------- REGRESSION LINÉAIRE ----------")
print(">> Precision = "+str(precision))
print(">> -----------------------------------------")
