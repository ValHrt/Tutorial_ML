# Etude des victoires en fonction du type

# Import des modules

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('expand_frame_repr', False)

# Recopie du script PokemonML1

liste_fichiers = os.listdir("datas")

for fichier in liste_fichiers:
    print(fichier)

Pokemons = pd.read_csv("datas/pokedex.csv")

Pokemons['LEGENDAIRE'] = (Pokemons['LEGENDAIRE'] == 'VRAI').astype(int)

Pokemons['NOM'][62] = "Colossinge"

Pokemons['TYPE_1'][199] = "Eau"

Pokemons['TYPE_2'] = Pokemons['TYPE_2'].replace(np.nan, '', regex=True)

Pokemons['TYPE_1_ET_2'] = Pokemons['TYPE_1'].str.cat(Pokemons['TYPE_2'], sep=" et ")
Pokemons['TYPE_1_ET_2'] = Pokemons.TYPE_1_ET_2.str.replace(r'\bet $', '', regex=True).str.strip()

print(Pokemons.head(10))

Combats = pd.read_csv("datas/combats.csv")
print(Combats.head(10))
