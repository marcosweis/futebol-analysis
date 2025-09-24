# Análise de Dados de Futebol - Premier League

Este projeto realiza análise estatística de dados da Premier League usando dados do FBref e Understat para estratégias de apostas e análise de performance.

## 📊 Sobre o Projeto

O projeto coleta e analisa dados de futebol da Premier League de múltiplas fontes:
- **FBref**: Dados de partidas e estatísticas básicas
- **Understat**: Dados avançados incluindo xG (Expected Goals) e eventos de chute

## 🗂️ Estrutura do Projeto

```
futebol-analysis/
├── dados_futebol/
│   ├── premier league_fbref_schedule.csv      # Dados de partidas do FBref (1.522 registros)
│   ├── premier league_understat_schedule.csv  # Dados de partidas do Understat (1.522 registros)
│   ├── premier league_understat_shots.csv     # Dados de eventos de chute (39.180 registros)
│   └── sample_data.csv                        # Arquivo de exemplo com estrutura dos dados
├── anlise_dados.py                            # Script principal de análise
├── extrair_dados_pl.py                        # Script para extração de dados
├── ex.py                                      # Script de exemplo/teste
└── README.md
```

## 🚀 Como Usar

### Pré-requisitos

```bash
pip install pandas soccerdata
```

### Extração de Dados

Para extrair novos dados da Premier League:

```python
python extrair_dados_pl.py
```

Este script extrai dados das temporadas 2020-2021 até 2023-2024 com pausas aleatórias para evitar bloqueios.

### Análise de Dados

Para analisar os dados coletados:

```python
python anlise_dados.py
```

## 📈 Dados Incluídos

- **Premier League FBref Schedule**: 1.522 registros de partidas com estatísticas básicas
- **Premier League Understat Schedule**: 1.522 registros de partidas com dados de xG
- **Premier League Understat Shots**: 39.180 eventos de chute com dados detalhados de xG

### Estrutura dos Dados

Os arquivos CSV contêm as seguintes colunas principais:

**Schedule (FBref/Understat):**
- `season`, `week`, `day`, `date`, `time`
- `home_team`, `away_team`
- `home_xg`, `away_xg` (Expected Goals)
- `score`, `attendance`, `venue`, `referee`

**Shots (Understat):**
- `match_id`, `minute`, `player`, `team`
- `xG` (Expected Goals do chute)
- `result` (Goal, Missed Shot, Saved Shot, etc.)
- `situation`, `shotType`, `h_a`

## 🎯 Objetivos

- Análise estatística de performance de times
- Desenvolvimento de estratégias de apostas baseadas em xG
- Identificação de padrões e tendências na Premier League
- Criação de modelos preditivos para resultados de partidas

## 📊 Fontes de Dados

- [FBref](https://fbref.com/) - Estatísticas básicas de futebol
- [Understat](https://understat.com/) - Dados avançados de xG e análise tática

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Pandas - Manipulação de dados
- SoccerData - Extração de dados de futebol
- CSV - Armazenamento de dados

## 📝 Licença

Este projeto é para fins educacionais e de pesquisa.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

**Nota**: Este projeto foi criado para análise de dados de futebol e desenvolvimento de estratégias de apostas baseadas em estatísticas avançadas.

## 🔗 Links Úteis

- [Repositório no GitHub](https://github.com/marcosweis/futebol-analysis)
- [Documentação do SoccerData](https://soccerdata.readthedocs.io/)
- [FBref - Estatísticas de Futebol](https://fbref.com/)
- [Understat - Análise de xG](https://understat.com/)