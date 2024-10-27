# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:07:48 2024

@author: Arian
"""

import pandas as pd
import numpy as np

datos = pd.read_csv('living.csv')
print(datos.info())
print(datos.head)

nro_filas = datos.shape[0]  
nro_columnas = datos.shape[1]  
print("Número de Filas:", nro_filas)
print("Número de Columnas:", nro_columnas)

costo_vid_prom = datos["Cost of living, 2017"].mean()
print("Costo de vida promedio:", costo_vid_prom)

pais_costo_vida_mayor = datos.loc[datos["Cost of living, 2017"].idxmax(), ["Countries", "Cost of living, 2017"]]
print("País con el costo de vida más alto:", pais_costo_vida_mayor["Countries"], "-", pais_costo_vida_mayor["Cost of living, 2017"])

pais_costo_vida_menor = datos.loc[datos["Cost of living, 2017"].idxmin(), ["Countries", "Cost of living, 2017"]]
print("País con el costo de vida más bajo:", pais_costo_vida_menor["Countries"], "-", pais_costo_vida_menor["Cost of living, 2017"])

cost_vida_peru = datos[datos["Countries"] == "Peru"][["Cost of living, 2017", "Global rank"]]
if not cost_vida_peru.empty:
    print("Costo de vida en Perú:", cost_vida_peru["Cost of living, 2017"].values[0])
    print("Ranking de Perú:", cost_vida_peru["Global rank"].values[0])
else:
    print("No se encontró información para Perú")
    
top_10_vida_alto = datos.nlargest(10, "Cost of living, 2017")[["Countries", "Cost of living, 2017"]]

top_10_vida_bajo = datos.nsmallest(10, "Cost of living, 2017")[["Countries", "Cost of living, 2017"]]

cost_vida_america = datos[datos["Continent"] == "America"][["Countries", "Cost of living, 2017"]]
