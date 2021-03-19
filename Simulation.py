import csv
import joblib


def recherche_pokemon(NumPokemon, Pokedex):
    infos_pokemon = []
    for pokemon in Pokedex:
        if int(pokemon[0]) == NumPokemon:
            infos_pokemon = [pokemon[0], pokemon[1], pokemon[4], pokemon[5], pokemon[6], pokemon[7], pokemon[8], pokemon[9], pokemon[10]]
            break
        return infos_pokemon


def prediction_combat(NumPokemon1, NumPokemon2, Pokedex):
    pokemon1 = recherche_pokemon(NumPokemon1, Pokedex)
    pokemon2 = recherche_pokemon(NumPokemon2, Pokedex)
    modele_prediction = joblib.load('Modele/modele_pokemon.mod')
    prediction_pokemon1 = modele_prediction.predict([[pokemon1[2], pokemon1[3], pokemon1[4], pokemon1[5], pokemon1[6], pokemon1[7], pokemon1[8]]])
    prediction_pokemon2 = modele_prediction.predict([[pokemon2[2], pokemon2[3], pokemon2[4], pokemon2[5], pokemon2[6], pokemon2[7], pokemon2[8]]])
    print("COMBAT OPPOSANT : ("+str(NumPokemon1)+") " + pokemon1[1]+" à ("+str(NumPokemon2)+") "+pokemon2[1])
    print("  "+pokemon1[1]+": "+str(prediction_pokemon1[0]))
    print("  "+pokemon2[1] + ": "+str(prediction_pokemon2[0]))
    print("")

    if prediction_pokemon1 > prediction_pokemon2:
        print(pokemon1[1].upper()+" EST LE VAINQUEUR !")
    else:
        print(pokemon2[1].upper() + " EST LE VAINQUEUR !")


with open("datas/pokedex.csv", newline='', errors='ignore') as csvfile:
    Pokedex = csv.reader(csvfile)
    next(Pokedex)
    prediction_combat(3, 6, Pokedex)
