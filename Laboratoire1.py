# Code pour plotting du laboratoire 1

import numpy as np
import matplotlib.pyplot as plt
import os

# Crée un dossier "figures" dans le même répertoire
repo_path = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(repo_path, "figures")
os.makedirs(figures_dir, exist_ok=True)

""" Mesures pour la SLED """
# Donnés @20C
data_sled_20deg = {"courant_in": np.array([0, 20, 40, 60, 80, 100, 120, 130]),
                   "tension": np.array([0.672, 0.912, 1.009, 1.108, 1.168, 1.254, 1.322, 1.343]),
                   "temperature": np.array([20, 20, 20, 20, 20.05, 20.03, 20.06, 20.04]),
                   "courant_mesure": np.array([1.3, 21.6, 41.4, 65.6, 81.4, 105.6, 125.6, 131.7]),
                   "puissance_w": np.array([4.5e-9, 3.6e-6, 39e-6, 207e-6, 421e-6, 899e-6, 1377e-6]),
                   "puissance_db": np.array([-53.1, -24.5, -14.1, -6.9, -3.75, -0.45, 1.39])}

# Donnés @10C
data_sled_10deg = {"courant_in": np.array([0, 20, 40, 60, 80, 100, 120, 130]),
                   "tension": np.array([0.682, 0.924, 1.020, 1.119, 1.177, 1.261, 1.330, 1.350]),
                   "temperature": np.array([10, 10, 10, 10, 10, 10, 10, 10]),
                   "courant_mesure": np.array([1.3, 21.6, 41.4, 65.6, 81.4, 105.6, 125.6, 131.7]),
                   "puissance_w": np.array([4.8e-9, 5.2e-6, 75e-6, 430e-6, 860e-6, 1650e-6, 2350e-6]),
                   "puissance_db": np.array([-53.1, -22.6, -11.4, -3.6, -0.6, 2.2, 3.7])}

""" Mesures pour la DFB """
# Donnés @20C
data_dfb_20deg = {"courant_in": np.array([0, 5, 10, 15, 20, 25, 30, 35]),
                  "tension": np.array([0, 0.835, 0.892, 0.930, 0.967, 1.004, 1.041, 1.078]),
                  "temperature": np.array([20.02, 20.02, 20.02, 20.03, 20.02, 20.02, 20.02, 20.02]),
                  "courant_mesure": np.array([0, 4.8, 9.8, 14.8, 19.8, 24.8, 29.8, 34.8]),
                  "puissance_w": np.array([4.8e-9, 1.3747e-6, 23e-6, 623e-6, 1201e-6, 1774e-6, 2337e-6, 2893e-6]),
                  "puissance_db": np.array([-53.1, -28.7, -16.4, -2.06, 0.8, 2.49, 3.69, 4.61])}

# Donnés @10C
data_dfb_10deg = {"courant_in": np.array([0, 5, 10, 15, 20, 25, 30, 35]),
                  "tension": np.array([0, 0.843, 0.896, 0.935, 0.974, 1.012, 1.050, 1.088]),
                  "temperature": np.array([10.02, 10.02, 10.02, 10.02, 10.02, 10.02, 10.02, 10.02]),
                  "courant_mesure": np.array([0, 4.8, 9.8, 14.8, 19.8, 24.8, 29.8, 34.8]),
                  "puissance_w": np.array([4.8e-9, 1.872e-6, 217.7e-6, 825.3e-6, 1417e-6, 2003e-6, 2586e-6, 3166e-6]),
                  "puissance_db": np.array([-53.1, -27.3, -6.62, 0.83, 1.51, 3.02, 4.13, 5.01])}

""" Plotting pour la DFB """
# @10deg
def dfb_10deg_courant_in_puissance_w() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_10deg["courant_in"], data_dfb_10deg["puissance_w"]*1e3 )
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (mW)")
    plt.show()
    return None

def dfb_10deg_courant_in_tension() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_10deg["courant_in"], data_dfb_10deg["tension"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Tension (V)")
    plt.show()
    return None

def dfb_10deg_courant_in_puissance_db() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_10deg["courant_in"], data_dfb_10deg["puissance_db"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (dB)")
    plt.show()
    return None

# @20deg
def dfb_20deg_courant_in_puissance_w() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_20deg["courant_in"], data_dfb_20deg["puissance_w"]*1e3 )
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (mW)")
    plt.show()
    return None

def dfb_20deg_courant_in_tension() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_20deg["courant_in"], data_dfb_20deg["tension"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Tension (V)")
    plt.show()
    return None

def dfb_20deg_courant_in_puissance_db() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_20deg["courant_in"], data_dfb_20deg["puissance_db"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (dB)")
    plt.show()
    return None


""" Plotting pour la SLED """
# @10deg
def sled_10deg_courant_in_puissance_w() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_10deg["courant_in"], data_sled_10deg["puissance_w"]*1e3 )
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (mW)")
    plt.show()
    return None

def sled_10deg_courant_in_tension() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_10deg["courant_in"], data_sled_10deg["tension"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Tension (V)")
    plt.show()
    return None

def sled_10deg_courant_in_puissance_db() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_10deg["courant_in"], data_sled_10deg["puissance_db"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (dB)")
    plt.show()
    return None

# @20deg
def sled_20deg_courant_in_puissance_w() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_20deg["courant_in"], data_sled_20deg["puissance_w"]*1e3 )
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (mW)")
    plt.show()
    return None

def sled_20deg_courant_in_tension() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_20deg["courant_in"], data_sled_20deg["tension"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Tension (V)")
    plt.show()
    return None

def sled_20deg_courant_in_puissance_db() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_20deg["courant_in"], data_sled_20deg["puissance_db"])
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (dB)")
    plt.show()
    return None


""" Plotting pour le rapport """

def plot_courbes_vi_sled() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_20deg["courant_in"], data_sled_20deg["tension"], 'k:', label="SLED à 20 degrés C")
    plt.plot(data_sled_10deg["courant_in"], data_sled_10deg["tension"], 'k', label="SLED à 10 degrés C")
    plt.xlabel("Courant (mA)")
    plt.ylabel("Tension (V)")
    plt.legend()
    plt.savefig(os.path.join(figures_dir, "courbe_vi_sled.png"), dpi=300, bbox_inches='tight')
    plt.show()
    return None

def plot_courbes_vi_dfb() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_20deg["courant_in"], data_dfb_20deg["tension"], 'k:', label="DFB à 20 degrés C")
    plt.plot(data_dfb_10deg["courant_in"], data_dfb_10deg["tension"], 'k', label="DFB à 10 degrés C")
    plt.xlabel("Courant (mA)")
    plt.ylabel("Tension (V)")
    plt.legend()
    plt.savefig(os.path.join(figures_dir, "courbe_vi_dfb.png"), dpi=300, bbox_inches='tight')
    plt.show()
    return None

def plot_courbes_pi_sled() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_sled_20deg["courant_in"][0:-1], data_sled_20deg["puissance_w"]*1e3, 'k:',label="SLED à 20 degrés C")
    plt.plot(data_sled_10deg["courant_in"][0:-1], data_sled_10deg["puissance_w"]*1e3, 'k',label="SLED à 10 degrés C")
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (mW)")
    plt.legend()
    plt.savefig(os.path.join(figures_dir, "courbe_pi_sled.png"), dpi=300, bbox_inches='tight')
    plt.show()
    return None

def plot_courbes_pi_dfb() -> None:
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(data_dfb_20deg["courant_in"], data_dfb_20deg["puissance_w"]*1e3, 'k:', label="DFB à 20 degrés C")
    plt.plot(data_dfb_10deg["courant_in"], data_dfb_10deg["puissance_w"]*1e3, 'k', label="DFB à 10 degrés C")
    plt.xlabel("Courant (mA)")
    plt.ylabel("Puissance (mW)")
    plt.legend()
    plt.savefig(os.path.join(figures_dir, "courbe_pi_dfb.png"), dpi=300, bbox_inches='tight')
    plt.show()
    return None

"""
Pour le rapport il faut reproduire toutes les courbes du fabricant de la dernière page du protocole. 

Dans un même graphique :
- toutes les courbes V-I pour chaque température (SLED). -- OK
- toutes les courbes P-I pour chaque température (SLED). -- OK
- toutes les courbes V-I pour chaque température (DFB).  -- OK
- toutes les courbes P-I pour chaque température (DFB).  -- OK
"""

#dfb_10deg_courant_in_puissance_w()
#dfb_10deg_courant_in_puissance_db()
#dfb_10deg_courant_in_tension()


# Afficher courbes V-I pour la SLED à 10deg et 20deg
plot_courbes_vi_sled()
# Afficher courbes P-I pour la SLED à 10deg et 20deg
plot_courbes_pi_sled()
# Afficher courbes V-I pour la DFB à 10deg et 20deg
plot_courbes_vi_dfb()
# Afficher courbes P-I pour la DFB à 10deg et 20deg
plot_courbes_pi_dfb()