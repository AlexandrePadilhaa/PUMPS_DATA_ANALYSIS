import pandas as pd

def read_csv_file(file_path):

    try:
        data = pd.read_csv(file_path, sep=";", encoding="utf-8")
        #print("Colunas encontradas no arquivo:", data.columns)
        return data

    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        raise RuntimeError(f"Ocorreu um erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    #Teste para validação das operações
    try:
        file_path = "data/Dados_Operacionais.csv" 
        df = read_csv_file(file_path)
        print(df.head())
    except Exception as e:
        print(e)
