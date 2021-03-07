# Etude des victoires en fonction du type 1 et 2

# Import des modules

import os
import pandas as pd
import numpy as np
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

Combats['Premier_Pokemon'] = Combats['Premier_Pokemon'].map(Pokemons.set_index('NUMERO')['TYPE_1_ET_2'])
Combats['Second_Pokemon'] = Combats['Second_Pokemon'].map(Pokemons.set_index('NUMERO')['TYPE_1_ET_2'])
Combats['Pokemon_Gagnant'] = Combats['Pokemon_Gagnant'].map(Pokemons.set_index('NUMERO')['TYPE_1_ET_2'])
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
list_agreg = list_agreg.drop(['Premier_Pokemon', 'Second_Pokemon'], axis=1)
print(list_agreg.groupby('Pokemon_Gagnant').agg({"POURCENTAGE_VICTOIRES": "mean"})
      .sort_values(by="POURCENTAGE_VICTOIRES", ascending=False).head(30))
