#Se importan las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.path as mpath

def Granulometria(tamiz_4,tamiz_10,tamiz_20,tamiz_30,tamiz_40,tamiz_60,tamiz_140,tamiz_200,fondo):
#Clasificación del suelo
    if 0 < tamiz_200:
        print("Suelo fino")
        print()

        #Tabla granulometrica
        variables = {'Tamices':['N°4', 'N°10', 'N°20', 'N°30','N°40', 'N°60', 'N°140', 'N°200','Fondo'],
                'Tamaño de las partículas [mm]':['4.75', '2', '0.85','0.60', '0.425', '0.25', '0.106', '0.075','0'],
                '% Pasa':[tamiz_4,tamiz_10,tamiz_20,tamiz_30,tamiz_40,tamiz_60,tamiz_140,tamiz_200,fondo]}
        
        Curva_granulometrica = pd.DataFrame(variables)
        grafica = print(Curva_granulometrica)
        #Se crean los ejes de la curva granulometrica
        Curva_granulometrica_x = ([4.75, 2, 0.850, 0.60, 0.425, 0.250, 0.106, 0.075, 0])
        Curva_granulometrica_y = ([tamiz_4,tamiz_10,tamiz_20,tamiz_30,tamiz_40,tamiz_60,tamiz_140,tamiz_200,fondo])

        plt.figure(figsize=(14, 4)) 
        plt.plot(Curva_granulometrica_x,Curva_granulometrica_y,linestyle='-', marker='o', color='c', fillstyle='none',label='Granulometía del suelo') 
        f = interp1d(Curva_granulometrica_y, Curva_granulometrica_x)
        plt.title("Curva Granulométrica",fontsize=10)
        plt.xlabel('Diámetro de la partícula (mm)')
        plt.ylabel('% pasa acumulado')
        plt.legend() 
        plt.xscale('log')
        plt.grid(which="both")
        plt.ylim(0,100) 
        plt.grid(color='k',lw='0.1',ls='-')
        plt.show()
        
    else:
        print("Suelo fino")
