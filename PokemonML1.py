# Import des modules

import os
import numpy as np
import pandas as pd

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

# Chargement des données combats

Combats = pd.read_csv("datas/combats.csv")
print(Combats.columns.values)
print(Combats.shape)
print(Combats.info())
print(Combats.head(10))

premiere_position = Combats.groupby('Premier_Pokemon').count()
seconde_position = Combats.groupby('Second_Pokemon').count()

total_combats = premiere_position+seconde_position
print(total_combats)
