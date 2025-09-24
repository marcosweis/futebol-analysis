# -*- coding: utf-8 -*-
import pandas as pd
from soccerdata import FBref, Understat
import time
import random
import os

def extrair_dados_com_prudencia(ligas, seasons):
    """
    Extrai dados das ligas e temporadas especificadas com pausas aleatórias.

    Args:
        ligas (dict): Dicionário com o nome da liga e a chave para as bibliotecas.
        seasons (list): Lista de temporadas a serem extraídas.

    Returns:
        dict: Um dicionário de DataFrames, com a chave sendo o nome da liga e a fonte.
    """
    print("Iniciando a extração de dados da Premier League...")
    dados_coletados = {}

    for nome_liga, key in ligas.items():
        # --- Extração com FBref ---
        try:
            print(f"\n[FBref] Extraindo dados de partidas da {nome_liga}...")
            # Inicializa a classe FBref para a Premier League
            fbref = FBref(leagues=key, seasons=seasons, no_cache=True)
            
            # Obtém os dados de partidas, que são a base para a análise
            partidas_fbref_df = fbref.read_schedule()
            
            # Adiciona os dados ao dicionário com uma chave descritiva
            dados_coletados[f"{nome_liga}_FBref_schedule"] = partidas_fbref_df
            print(f"Dados de partidas do FBref para a {nome_liga} extraídos com sucesso. Shape: {partidas_fbref_df.shape}")
        except Exception as e:
            print(f"Erro ao extrair dados de partidas do FBref para a {nome_liga}: {e}")
        
        # Pausa para prudência máxima entre as fontes
        pausa = random.randint(30, 90) # Pausa aleatória entre 30 e 90 segundos
        print(f"\nAguardando {pausa} segundos antes de extrair com o Understat...")
        time.sleep(pausa)

        # --- Extração com Understat ---
        try:
            print(f"\n[Understat] Extraindo horários e confrontos (schedule) da {nome_liga}...")
            understat = Understat(leagues=key, seasons=seasons, no_cache=True)
            
            # Extrai o schedule da Understat para obter o game_id e o confronto
            partidas_understat_df = understat.read_schedule()
            
            # Adiciona os dados ao dicionário
            dados_coletados[f"{nome_liga}_Understat_schedule"] = partidas_understat_df
            print(f"Dados de horários do Understat para a {nome_liga} extraídos com sucesso. Shape: {partidas_understat_df.shape}")
        except Exception as e:
            print(f"Erro ao extrair dados de horários do Understat para a {nome_liga}: {e}")

        pausa = random.randint(15, 45) # Pausa mais curta entre as extrações do mesmo site
        print(f"\nAguardando {pausa} segundos antes de extrair os eventos de chute...")
        time.sleep(pausa)

        try:
            print(f"\n[Understat] Extraindo eventos de chute (xG) da {nome_liga}...")
            understat = Understat(leagues=key, seasons=seasons, no_cache=True)
            
            # Obtém os eventos de chute, que são cruciais para a estratégia de apostas
            eventos_chute_df = understat.read_shot_events()
            
            # Adiciona os dados ao dicionário
            dados_coletados[f"{nome_liga}_Understat_shots"] = eventos_chute_df
            print(f"Dados de eventos de chute do Understat para a {nome_liga} extraídos com sucesso. Shape: {eventos_chute_df.shape}")
        except Exception as e:
            print(f"Erro ao extrair dados de eventos de chute do Understat para a {nome_liga}: {e}")
    
    return dados_coletados

def salvar_dados_csv(dados, diretorio="dados_futebol"):
    """
    Salva os DataFrames em arquivos CSV separados.

    Args:
        dados (dict): Dicionário de DataFrames.
        diretorio (str): Diretório para salvar os arquivos.
    """
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    print(f"\nSalvando arquivos CSV no diretório '{diretorio}'...")
    for nome_df, df in dados.items():
        if not df.empty:
            filepath = os.path.join(diretorio, f"{nome_df.lower()}.csv")
            df.to_csv(filepath, index=False)
            print(f"Dados de '{nome_df}' salvos em '{filepath}'")
        else:
            print(f"DataFrame '{nome_df}' está vazio, não será salvo.")

    print("\nExtração de dados concluída!")

if __name__ == "__main__":
    # Foco na Premier League conforme o plano
    PL_DICT = {"Premier League": "ENG-Premier League"}
    seasons = ["2020-2021", "2021-2022", "2022-2023", "2023-2024"]  # Temporadas a serem extraídas
    
    # Executa a extração
    dados_coletados = extrair_dados_com_prudencia(PL_DICT, seasons)
    
    # Salva os dados
    if dados_coletados:
        salvar_dados_csv(dados_coletados)