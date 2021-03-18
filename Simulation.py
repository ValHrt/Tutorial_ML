import csv
import joblib


def recherche_pokemon(NumPokemon, Pokedex):
    infos_pokemon = []
    for pokemon in Pokedex:
        if int(pokemon[0]) == NumPokemon:
            infos_pokemon = [pokemon[0], pokemon[1], pokemon[4], pokemon[5], pokemon[6], pokemon[7], pokemon[8],
                             pokemon[9], pokemon[10]]
            break
        return infos_pokemon

