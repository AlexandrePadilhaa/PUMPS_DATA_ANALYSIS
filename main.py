import pandas as pd
from src.data_reader import read_csv_file
from src.data_analysis import (
    calculate_operation_hours,
    calculate_operation_count,
    find_max_flow,
    find_high_flow_times,
)


def main():
    file_path = "data/Dados_Operacionais.csv"
    try:
        print("Lendo o arquivo...")
        data = read_csv_file(file_path)
        print("Arquivo lido com sucesso!")

        print("\nAnalisando os dados...")
        operation_hours = calculate_operation_hours(data)
        operation_count = calculate_operation_count(data)
        max_flow = find_max_flow(data)
        high_flow_times = find_high_flow_times(data)

        print("\nResultados da análise:")
        print(f"1. Número de horas que o duto operou: {operation_hours}")
        print(f"2. Número de vezes que o duto operou: {operation_count}")
        print(f"3. Vazão máxima registrada: {max_flow:.2f} m³/h")
        print("4. Horários em que a vazão ultrapassou 1500 m³/h:")
        for time in high_flow_times:
            print(f"   - {time}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
