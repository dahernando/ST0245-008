'''
Implementacion del codigo
para la lectura de datos
'''

#Importa la libreria pandas que nos permite leer el archivo
import pandas as pd
#Lectura de datos
try:
    archivo = pd.read_csv('TESTlite.csv',sep=';')
    print(archivo)
#  Lanza una excepcion caso de error
except Exception as e:
    print("Ocurrio el error", e)
