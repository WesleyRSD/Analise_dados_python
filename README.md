# Data Analytics Dashboard 📊

Este é um projeto de **Dashboard de Inteligência de Mercado** desenvolvido em Python usando **Streamlit** para visualização e análise de dados de vendas e clientes. O objetivo deste projeto é fornecer insights valiosos sobre vendas, desempenho regional, satisfação do cliente e outras métricas de negócio, utilizando dados fictícios para demonstração.

## Funcionalidades 🚀

- **Análise de Vendas**: Visualize a receita total, lucro bruto e o NPS médio.
- **Receita e Lucro por Região e Canal de Venda**: Compare a performance entre diferentes regiões e canais (online e loja física).
- **Perfil do Cliente**: Analise o perfil demográfico dos clientes e o impacto das ações de marketing no NPS.
- **Análise Temporal**: Acompanhe as métricas de receita e lucro ao longo do tempo, identificando sazonalidade e tendências.
- **Filtros Interativos**: Explore os dados aplicando filtros por região, canal de venda e categoria de produto.

## Estrutura do Projeto 📂

data-analytics-dashboard/
├── data/                           # Diretório com o dataset
│   └── Vendas_Inteligencia_Mercado_Sintetico.csv
├── dashboards/                     # Diretório com o código do dashboard
│   └── dashboard.py                # Arquivo principal do Streamlit para o dashboard
├── notebooks/                      # Diretório com o notebook de exploração de dados
│   └── data_exploration.ipynb      # Notebook para análise exploratória e limpeza de dados
├── utils/                          # Diretório com módulos auxiliares
│   ├── data_loader.py              # Script para carregar e limpar dados
│   └── data_analysis.py            # Script com funções de cálculo de KPIs e métricas
├── README.md                       # Arquivo de documentação do projeto
└── requirements.txt                # Arquivo com as dependências do projeto


## Requisitos 🛠️

Antes de rodar o projeto, você precisa instalar as dependências. Recomendo criar um ambiente virtual para manter as dependências isoladas.

### Instalando as Dependências

Use o comando abaixo para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

Dependências Principais
Python 3.8+
Streamlit - Para construir o dashboard
Pandas - Para manipulação e análise de dados

Executando o Dashboard 🚀
1.Navegue até o diretório do projeto no terminal.
2.Execute o seguinte comando para iniciar o Streamlit e abrir o dashboard no navegador:
streamlit run dashboards/dashboard.py
3.Acesse o dashboard no seu navegador no endereço: http://localhost:8501

Como Usar o Dashboard 🖥️

O dashboard permite que você explore os dados e visualize insights chave:

KPIs Principais: Exibe a receita total, lucro bruto e o NPS médio.
Filtros Interativos: Selecione regiões, canais de venda e categorias de produto para refinar a análise.
Gráficos Interativos: Visualize a receita e o lucro por região e canal, além de outras análises visuais.

Dataset 🗃️
O dataset utilizado é um conjunto de dados fictício gerado para fins de demonstração, contendo as seguintes colunas:

Data_Venda: Data da venda
**Produto e Categoria_Produto: Nome e categoria do produto
**Regiao e Canais_Venda: Região e canal de venda (online ou loja física)
**Quantidade, Preco_Unitario, Desconto: Quantidade vendida, preço unitário e desconto aplicado
**Cliente_ID, Cliente_Idade, Cliente_Sexo: Informações demográficas dos clientes
**Receita, Custo e Lucro_Bruto: Valores calculados com base nas vendas

Próximos Passos 🔄
**Implementar novas visualizações, como análise de devoluções e fidelidade de clientes.
**Expandir o dashboard com previsões de vendas e análises mais avançadas.
**Integrar dados reais de um sistema de CRM ou ERP para análises mais aprofundadas.

Licença 📄
Este projeto é disponibilizado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.



