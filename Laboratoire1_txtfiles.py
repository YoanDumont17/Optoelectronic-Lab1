# Code pour afficher les spectres de l'OSA du labo 1

import numpy as np
import matplotlib.pyplot as plt
import os


""" 
Fichiers du labo :

1 - 20deg SLED :
    - file 538 à 545
    - début du file name : 1350-1650_Real Time_1_(file number)

2 - 10deg SLED :
    - file 530 à 537
    - début du file name : 1350-1650_Real Time_1_(file number)
    
3 - 20deg DFB :
    - file 600 à 607 (attention 30 mA = file 607, 35 mA = file 606)
    - début du file name : 1541-1560_Real Time_1_(file number)
    
4 - 10deg DFB :
    - file 609 à 616 
    - début du file name : 1541-1560_Real Time_1_(file number)
"""

# Fonction « open » prend le path d'où le python code roule et non C:\

def data_text_en_array(string_path: str, lignes_a_skip: int) -> list:
    """
    Fonction extrêmement boboche pour format un fichier .txt

    Argument :
        - Path vers le fichier .txt (un string)
        - Lignes à skip

    Retourne :
        - Liste contenant des sous liste de dim 2. list[0] = wvl, list[1] = dbm

    """

    wvl, dbm = [], []

    with open(string_path, "r") as f:
        data = [ligne.strip("\n") for ligne in f.readlines()] # Enlève les \n
        ligne_depart_data = lignes_a_skip # Tous les .txt ont leur data qui start à la ligne 102
        ligne_index = 0

        for ligne in data: # On veut seulement les données, pas le header
            if ligne_index < ligne_depart_data:
                ligne_index += 1
                continue
            elif ligne_index < (len(data) - 3): # Les dernières lignes des .txt sont toutes vides
                ligne_reformatted = ligne.strip("\t")
                data_wavelength = float(ligne_reformatted[0:7].replace(",", "."))
                data_dbm = float(ligne_reformatted[9:].replace(",", "."))
                wvl.append(data_wavelength)
                dbm.append(data_dbm)
                ligne_index += 1

    return wvl, dbm

# Premier test de fichier :
for i in range(7):
    file_number = 542
    wavelength, power_dbm = data_text_en_array(f"SLED/20 deg/1350-1650_Real Time_1_{file_number}.txt", 102)
    #print(wavelength, power_dbm)

    plt.plot(wavelength, power_dbm)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Power (dBm)")
    plt.show()

