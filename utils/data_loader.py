# data_loader.py
import pandas as pd
 
def load_data(filepath, delimiter=';'):
    """Carrega e limpa o dataset."""
    df = pd.read_csv(filepath, delimiter=delimiter)
    
    # Conversão de tipos e tratamento de valores ausentes
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'], errors='coerce')
    for col in ['Receita', 'Lucro_Bruto', 'NPS', 'Desconto', 'Custo']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # Remover linhas com datas ausentes
    df.dropna(subset=['Data_Venda'], inplace=True)
    
    return df