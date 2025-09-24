import pandas as pd
import os

diretorio = 'dados_futebol'

df_fbref = pd.read_csv(os.path.join(diretorio, 'premier league_fbref_schedule.csv'))
df_understat = pd.read_csv(os.path.join(diretorio, 'premier league_understat_schedule.csv'))
df_understat_shots = pd.read_csv(os.path.join(diretorio, 'premier league_understat_shots.csv'))


try:
    df_fbref = pd.read_csv(os.path.join(diretorio, 'premier league_fbref_schedule.csv'))
    df_understat = pd.read_csv(os.path.join(diretorio, 'premier league_understat_schedule.csv'))
    df_understat_shots = pd.read_csv(os.path.join(diretorio, 'premier league_understat_shots.csv'))

    print("Arquivos CSV carregados com sucesso!")
except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado. {e}")
        print(f"Certifique-se de que os arquivos 'premier league_fbref_schedule.csv', 'premier league_understat_schedule.csv' e 'premier league_understat_shots.csv' estão no diretório '{diretorio}'.")


df_fbref.info()
df_understat.info()
df_understat_shots.info()