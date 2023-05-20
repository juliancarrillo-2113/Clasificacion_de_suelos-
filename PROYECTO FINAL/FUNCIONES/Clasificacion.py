#Se importan las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.path as mpath

def Clasificacion(tamiz_4,tamiz_200):
    if tamiz_200 < 50:
        if tamiz_4 > 50: # Arenas
            if tamiz_200 <= 5: 
                print("Grava bien graduada (GW) o Grava pobremente graduada (GP)")
            elif 5 < tamiz_200 <= 12:
                print("Combinación de Gravas")
            else:
                print("Grava limosa (GM) o Grava arcillosa (GC)")
        else:
            if tamiz_200 <= 5:
                print("El suelo es una arena bien graduada (SW) o pobremente graduada (SP)")
            elif 5 < tamiz_200 <= 12:
                print("El suelo es una combinación de arenas")
            else:
                print("El suelo es una arena limosa (SM) o arcillosa (SC)")

