#**Clasificación de Suelos**#
### Universidad Distrital Francisco José de Caldas
### Julian David Carrillo Casas
### 20221579028
### *Teoría y Lógica de Programación*
### Carlos Arturo Gomez Jimenez

#Inputs - Valores de entrada
from FUNCIONES.Inputs import *
tamiz_4,tamiz_10,tamiz_20,tamiz_30,tamiz_40,tamiz_60,tamiz_140,tamiz_200,fondo = Inputs()

#Carta_de_Plasticidad
from FUNCIONES.Carta_Plasticidad import *
Carta_Plasticidad(tamiz_200)

#Granulometria
from FUNCIONES.Curva_Granulometrica import *
Granulometria(tamiz_4,tamiz_10,tamiz_20,tamiz_30,tamiz_40,tamiz_60,tamiz_140,tamiz_200,fondo)

#Clasificación
from FUNCIONES.Clasificacion import *
Clasificacion(tamiz_4,tamiz_200)


