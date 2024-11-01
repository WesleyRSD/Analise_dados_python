# dashboard.py
import streamlit as st
import plotly.express as px
import os
from utils.data_loader import load_data
from utils.data_analysis import calcular_kpis, receita_por_canal, receita_por_regiao, lucro_por_regiao
 
# Definir o caminho do arquivo de dados
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Vendas_Inteligencia_Mercado_Limpo.csv')
 
# Carregar e limpar dados
df = load_data(file_path)
 
# Calcular KPIs principais
receita_total, lucro_total, nps_medio = calcular_kpis(df)
 
# Exibir KPIs principais formatados
st.title("Dashboard de Inteligência de Mercado")
st.metric("Receita Total", f"R${receita_total:,.2f}")
st.metric("Lucro Total", f"R${lucro_total:,.2f}")
st.metric("NPS Médio", f"{nps_medio:.1f}")
 
# Receita por Canal de Venda
st.subheader("Receita por Canal de Venda")
receita_canal = receita_por_canal(df)
for canal, receita in receita_canal.items():
    st.write(f"{canal}: R${receita:,.2f}")
 
# Receita por Região
st.subheader("Receita por Região")
receita_regiao = receita_por_regiao(df)
for regiao, receita in receita_regiao.items():
    st.write(f"{regiao}: R${receita:,.2f}")
 
# Lucro por Região
st.subheader("Lucro por Região")
lucro_regiao = lucro_por_regiao(df)
for regiao, lucro in lucro_regiao.items():
    st.write(f"{regiao}: R${lucro:,.2f}")
 
# Gráficos Interativos
 
# Receita por Canal de Venda (Gráfico de Barras)
fig_receita_canal = px.bar(df, x="Canais_Venda", y="Receita", title="Receita por Canal de Venda", color="Canais_Venda")
st.plotly_chart(fig_receita_canal)
 
# Receita por Região (Gráfico de Barras)
fig_receita_regiao = px.bar(df, x="Regiao", y="Receita", title="Receita por Região", color="Regiao")
st.plotly_chart(fig_receita_regiao)
 
# Lucro por Região (Gráfico de Barras)
fig_lucro_regiao = px.bar(df, x="Regiao", y="Lucro_Bruto", title="Lucro Bruto por Região", color="Regiao")
st.plotly_chart(fig_lucro_regiao)