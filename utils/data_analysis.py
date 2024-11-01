# data_analysis.py
def calcular_kpis(df):
    """Calcula os KPIs principais."""
    receita_total = df['Receita'].sum()
    lucro_total = df['Lucro_Bruto'].sum()
    nps_medio = df['NPS'].mean()
    return receita_total, lucro_total, nps_medio
 
def receita_por_canal(df):
    """Calcula a receita por canal de venda."""
    return df.groupby("Canais_Venda")['Receita'].sum()
 
def receita_por_regiao(df):
    """Calcula a receita por região."""
    return df.groupby("Regiao")['Receita'].sum()
 
def lucro_por_regiao(df):
    """Calcula o lucro bruto por região."""
    return df.groupby("Regiao")['Lucro_Bruto'].sum()