# Import des modules

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('expand_frame_repr', False)

# Analyse des fichiers

liste_fichiers = os.listdir("datas")

for fichier in liste_fichiers:
    print(fichier)

# Chargement des données pokedex

Pokemons = pd.read_csv("datas/pokedex.csv")
print(Pokemons.columns.values)
print(Pokemons.shape)
print(Pokemons.info())
print(Pokemons.head(10))

# Transformer la variable 'LEGENDAIRE' en valeur numérique (0 = FAUX, 1 = VRAI)

Pokemons['LEGENDAIRE'] = (Pokemons['LEGENDAIRE'] == 'VRAI').astype(int)
print(Pokemons['LEGENDAIRE'].head(10))

# Trouver les valeurs manquantes et les remplacer

print(Pokemons[Pokemons['NOM'].isnull()])
Pokemons['NOM'][62] = "Colossinge"

# Changer les erreurs dans le jeu de données

Pokemons['TYPE_1'].unique()
Pokemons_mask=Pokemons['TYPE_1']=='E'
filtered_pokemons = Pokemons[Pokemons_mask]
print(filtered_pokemons)  # erreur sur Azumarill avec un TYPE_1 = "E"

Pokemons['TYPE_1'][199] = "Eau"

# Chargement des données combats

Combats = pd.read_csv("datas/combats.csv")
print(Combats.columns.values)
print(Combats.shape)
print(Combats.info())
print(Combats.head(10))

premiere_position = Combats.groupby('Premier_Pokemon').count()
seconde_position = Combats.groupby('Second_Pokemon').count()

victoires = Combats.groupby('Pokemon_Gagnant').count()

list_agreg = Combats.groupby('Pokemon_Gagnant').count()
list_agreg.sort_index()

list_agreg['NBR_COMBATS'] = premiere_position.Pokemon_Gagnant + seconde_position.Pokemon_Gagnant
list_agreg['NBR_VICTOIRES'] = victoires.Premier_Pokemon

list_agreg['POURCENTAGE_VICTOIRES'] = victoires.Premier_Pokemon / (premiere_position.Pokemon_Gagnant
                                                                   + seconde_position.Pokemon_Gagnant)

# Fusionner les deux jeux de données

stats_pokedex = Pokemons.merge(list_agreg, left_on='NUMERO', right_index=True, how='left')
stats_pokedex = stats_pokedex.drop(['Premier_Pokemon', 'Second_Pokemon'], axis=1)
print(stats_pokedex.head(20))

print(stats_pokedex.describe())

# Visualisation avec matplotlib

axe_X = sns.countplot(x="TYPE_1", hue="LEGENDAIRE", data=stats_pokedex)
plt.xticks(rotation=90)
plt.xlabel('TYPE_1')
plt.ylabel('Total')
plt.title("POKEMONS DE TYPE 1")
#plt.show()

axe_X = sns.countplot(x="TYPE_2", hue="LEGENDAIRE", data=stats_pokedex)
plt.xticks(rotation=90)
plt.xlabel('TYPE_2')
plt.ylabel('Total')
plt.title("POKEMONS DE TYPE 2")
#plt.show()

# Afficher les pourcentages de victoires par type

print(stats_pokedex.groupby('TYPE_1').agg({"POURCENTAGE_VICTOIRES": "mean"}).sort_values(by="POURCENTAGE_VICTOIRES"))

# Faire ressortir un taux de victoire en fonction du type contre un autre type

