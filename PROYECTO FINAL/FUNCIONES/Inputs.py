#Se importan las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.path as mpath

#Inputs
def Inputs():
    tamiz_4 = 51
    tamiz_10 = 8
    tamiz_20 = 16
    tamiz_30 = 14
    tamiz_40 = 15
    tamiz_60 = 32
    tamiz_140 = 25
    tamiz_200 = 52
    fondo = 12
    return tamiz_4,tamiz_10,tamiz_20,tamiz_30,tamiz_40,tamiz_60,tamiz_140,tamiz_200,fondo