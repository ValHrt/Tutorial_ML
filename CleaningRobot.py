# -------------------------------
# Functions
# -------------------------------

def calcul_surface_a_nettoyer(listedezones):
    surface = 0
    for zone in listedezones:
        longueur = zone.get("longueur") / 100
        largeur = zone.get("largeur") / 100
        calcul = longueur * largeur
        print(str(longueur) + " x " + str(largeur) + "= " + str(calcul))
        surface = surface + calcul
    return surface


def temps_nettoyage_en_minutes(surface, temps_nettoyage_1m2):
    return round(surface * temps_nettoyage_1m2)


# -------------------------------
# Application
# -------------------------------

# Robot's name and time to clean 1m2
parametres = ("robot_aspiro", 2)

# Use of dictionnaries to create zone
zone1 = {"longueur": 500, "largeur": 150}
zone2 = {"longueur": 309, "largeur": 480}
zone3 = {"longueur": 101, "largeur": 480}
zone4 = {"longueur": 90, "largeur": 220}

zones = [zone1, zone2, zone3, zone4]

surface = calcul_surface_a_nettoyer(zones)
print("La surface totale à nettoyer est de : " + str(surface) + "m2")

temps_estime = temps_nettoyage_en_minutes(surface, parametres[1])
print("Le temps estimé est de :" + str(temps_estime) + " minutes")

if temps_estime > 55:
    print(parametres[0]+" dit : Je pense que ça va prendre un peu de temps !")
