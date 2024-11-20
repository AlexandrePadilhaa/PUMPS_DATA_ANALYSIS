import pandas as pd

def calculate_operation_hours(data):
    data_filtered = data[data["Vazao, descarga da EB"] > 1000]
    
    data_filtered["Horario"] = pd.to_datetime(data_filtered["Horario"], format="%H:%M:%S")
    data_filtered["Hora"] = data_filtered["Horario"].dt.hour
    
    return data_filtered["Hora"].nunique()

def calculate_operation_count(data):

    is_operating = data["Vazao, descarga da EB"] > 1000
    return (is_operating.astype(int).diff() == 1).sum()

def find_max_flow(data):

    return data["Vazao, descarga da EB"].max()

def find_high_flow_times(data):

    high_flow_times = data[data["Vazao, descarga da EB"] > 1500]["Horario"]
    return high_flow_times.tolist()

if __name__ == "__main__":
    #Teste para validação das operações
    sample_data = {
        "Horario": ["00:00:00", "00:00:01", "00:00:02", "00:00:03"],
        "Vazao, descarga da EB": [900, 1600, 1200, 800]
    }
    df = pd.DataFrame(sample_data)

    print("\nResultados")
    print(f"1. Número de horas que o duto operou: { calculate_operation_hours(df)}")
    print(f"2. Número de vezes que o duto operou: {calculate_operation_count(df)}")
    print(f"3. Vazão máxima registrada: {find_max_flow(df):.2f} m³/h")
    print(f"4. Horários em que a vazão ultrapassou 1500 m³/h:")
    for time in find_high_flow_times(df):
        print(f"   - {time}")    
