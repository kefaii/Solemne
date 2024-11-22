# -*- coding: utf-8 -*-
"""Codex1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y3cA9S864cC2oTYsWHBci7pcFl3dG9Dg
"""

import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Endpoint de la API
url = "https://restcountries.com/v3.1/all"

# Solicitud GET
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    # Extraer informacion relevante
    countries = []
    for country in data:
        countries.append({
            "Name": country.get("name",{}).get("common","N/A"),
            "Region": country.get("region","N/A"),
            "Population": country.get("population",0),
            "Area (Km)": country.get("area",0),
            "Borders Count": len(country.get("borders", [])),
            "Languages Count": len(country.get("language", {})),
            "Timezones Count": len(country.get("timezones", []))
        })
        
    # Convertir a DataFrame
    df = pd.DataFrame(countries)
   
    
    # Titulo de la Descripcion
    st.title('Sección de Descripcion')
   
    # Texto de la Descripcion
    st.text("Descripcion")

    
    # Título de la aplicación
    st.header('Aplicación Web: Datos desde una API REST')
    
    # Mostrar los primeros registros
    st.write('Datos obtenidos de la API:')
    st.write(df.head())

    
    # Titulo de calcular media, mediana, desviacion
    st.header("Seleccionar una columna específica del dataframe con un menú desplegable")

    # Mostrar columna seleccionada
    #st.write(f"Datos de la columna '{columna_seleccionada}':")
    #st.write(df[columna_seleccionada])
    
    # Crear un selectbox para seleccionar una columna
    columnas_numericas = df.select_dtypes(include=["number"]).columns.tolist()
    columna_estadistica = st.selectbox("Selecciona una columna para calcular estadisticas:", columnas_numericas) 

    # Mostrar columna seleccionada
    st.write("Datos de la columna",df[columna_estadistica])
    
    # Calcular estadisticas de la columna seleccionada
    if columna_estadistica:
        media = df[columna_estadistica].mean()
        mediana = df[columna_estadistica].median()
        desviacion = df[columna_estadistica].std()
    
    # Mostrar los resultados
    st.write(f"### Estadísticas de '{columna_estadistica}':")
    st.write(f"- **Media:** {media}")
    st.write(f"- **Mediana:** {mediana}")
    st.write(f"- **Desviación estándar:** {desviacion}")
    

    # Crear botones para ordenar columnas
    
    def ascendente(df):
        df = df.sort_values(by=columna_estadistica, ascending=True)
        return st.write(df)
        
    st.button("ascendente", on_click=ascendente(df))


    # Filtro por ID
    #id_filtro = st.slider('Filtrar por ID (entre 1 y 100)', 1, 100, 50)
    #df_filtrado = df[df['id'] <= id_filtro]
    #st.write(f"Mostrando datos donde ID <= {id_filtro}:")
    #st.write(df_filtrado)

else:
 st.error('Error al obtener los datos de la API')
