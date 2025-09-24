import pandas as pd
import os

diretorio = 'dados_futebol'

# carregando os DataFrames a partir dos arquivos CSV
df_fbref = pd.read_csv(os.path.join(diretorio, 'premier league_fbref_schedule.csv'))
df_understat = pd.read_csv(os.path.join(diretorio, 'premier league_understat_schedule.csv'))
df_understat_shots = pd.read_csv(os.path.join(diretorio, 'premier league_understat_shots.csv')) 

# Exibindo as primeiras linhas para verificar os dados
print("DataFrame FBref:")
print(df_fbref.head())
print("\nDataFrame Understat:")
print(df_understat.head())
print("\nDataFrame Understat Shots:")
print(df_understat_shots.head())

# Verificando informações e valores nulos em cada DataFrame
print("\nInformações do DataFrame FBref:")
print(df_fbref.info())
print("\nInformações do DataFrame Understat:")
print(df_understat.info())
print("\nInformações do DataFrame Understat Shots:")
print(df_understat_shots.info())