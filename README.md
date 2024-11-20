## Análise de Dados de Operação do Duto
Este projeto tem como objetivo a análise de dados operacionais de um duto utilizado no transporte de minério, rejeito e água recuperada. Ele processa um arquivo CSV com informações de sensores e transdutores instalados ao longo do duto para gerar insights operacionais.

## Requisitos
pandas==2.2.3

## Execução

Clone este repositorio e execute usando: python main.py

### Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:  
├── data  
│   └── Dados_Operacionais.csv  
├── src  
│   ├── data_reader.py          # Funções para leitura do arquivo CSV.  
│   ├── data_analysis.py        # Funções para análise dos dados.  
├── main.py                     # Arquivo principal que integra as funções e gera os resultados.  
└── README.md                   # Este arquivo com as informações do projeto.  


### Resultados

Segue exemplos de saida com os resultados encontrados:

1. Número de horas que o duto operou: 24      
2. Número de vezes que o duto operou: 9
3. Vazão máxima registrada: 1600.48 m³/h
4. Horários em que a vazão ultrapassou 1500 m³/h:
   - 00:03:36
   - 00:03:37
   - 00:03:38
   - 00:03:39
   - ...

