import pandas as pd
import streamlit as st
import seaborn as sns   
import matplotlib.pyplot as plt
import numpy as np
import gdown


def params_graph():
    sns.set_theme()
    plt.rcParams['figure.figsize'] = (6, 3) # Tamanho da figura
    plt.rcParams['axes.titlesize'] = 10 # Tamanho do título
    plt.rcParams['axes.labelsize'] = 8 # Tamanho do rótulo
    plt.rcParams['xtick.labelsize'] = 7 # Tamanho do rótulo do eixo x
    plt.rcParams['ytick.labelsize'] = 7 # Tamanho do rótulo do eixo y
    plt.rcParams['legend.fontsize'] = 8 # Tamanho da legenda
    plt.rcParams['lines.markersize'] = 4 # Tamanho dos marcadores

    return None

def read_drive(file_id):
    url = f'https://drive.google.com/uc?id={file_id}'

    output = 'orders_cleaned.csv'
    gdown.download(url, output, quiet=False)
    df = pd.read_csv(output)

    return df

def filters(df):
    
    st.sidebar.header('Filtros')

    # Filtro por UF
    lista_estados = df['customer_state'].sort_values().unique()
    estados_selecionado = st.sidebar.multiselect('Selecione um Estado',options=lista_estados, default=lista_estados)

    # Filtro por status pedido
    lista_status = df['order_status'].sort_values().unique()
    status_selecionado = st.sidebar.multiselect('Selecione um Status', options=lista_status, default=lista_status)

    # filtro de data
    periodo = df['order_purchase_year_month'].unique()
    data_selecionado = st.sidebar.multiselect('Selecione os períodos (Mês/Ano)', options=periodo, default=periodo)

    customer_df_filtered = df[(ordersDF['customer_state'].isin(estados_selecionado)) & 
                              (ordersDF['order_status'].isin(status_selecionado)) & 
                              (ordersDF['order_purchase_year_month'].isin(periodo))]
    
    seller_df_filtered = df[(ordersDF['seller_state'].isin(estados_selecionado)) &
                            (ordersDF['order_status'].isin(status_selecionado)) &
                           (ordersDF['order_purchase_year_month'].isin(periodo))]


    return customer_df_filtered, seller_df_filtered

def big_numbers(df1, df2):
    total_vendas = df1['total_price'].sum()
    total_customers = df1['customer_id'].nunique()
    total_sellers = df2['seller_id'].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric('Total de Vendas', f'R$ {total_vendas:,.2f}')
    col2.metric('Total de Clientes', f"{total_customers:,.0f}")
    col3.metric('Total de Vendedores', f"{total_sellers:,.0f}")

    st.divider()

    melhor_vendedor = df2[['seller_id', 'total_price']].groupby('seller_id').sum().sort_values('total_price', ascending=False)
    col4, col5 = st.columns(2)
    col4.metric('Melhor Vendedor:', melhor_vendedor.index[0])
    col5.metric('Valor total de itens vendidos:', melhor_vendedor['total_price'][0])

    cliente_especial= df1[['customer_unique_id', 'total_price']].groupby('customer_unique_id').sum().sort_values('total_price', ascending=False)
    col6, col7 = st.columns(2)
    col6.metric('Cliente Especial:', cliente_especial.index[0])
    col7.metric('Valor total de itens pedidos:', cliente_especial['total_price'][0])

    st.divider()

    return None

def overview(df1, df2):
    
    col1, col2, col3 = st.columns(3)
    vendas_estado = df1[['customer_state', 'total_price']].groupby('customer_state').sum().reset_index()

    fig1, ax1 = plt.subplots()
    sns.barplot(data=vendas_estado, x='customer_state', y='total_price', ax=ax1)
    ax1.set_title('Total de Vendas por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Total de Vendas R$')
    col1.pyplot(fig1)

    clientes_estado = df1[['customer_state', 'customer_unique_id']].groupby('customer_state').nunique().reset_index()

    fig2, ax2 = plt.subplots()
    sns.barplot(data=clientes_estado, x='customer_state', y='customer_unique_id', ax=ax2)
    ax2.set_title('Total de Clientes por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Total de Clientes')
    col2.pyplot(fig2)

    vendedores_estado = df2[['seller_state', 'seller_id']].groupby('seller_state').nunique().reset_index()

    fig3, ax3 = plt.subplots()
    sns.barplot(data=vendedores_estado, x='seller_state', y='seller_id', ax=ax3)
    ax3.set_title('Total de Vendedores por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Total de Vendedores')
    col3.pyplot(fig3)
    
    return None

def temporal_visions(df1, df2):

    col1 ,col2, col3 = st.columns(3)

    dfax1 = df1[['order_purchase_year_month', 'total_price']].groupby('order_purchase_year_month').sum().reset_index()
    fig1, ax1 = plt.subplots()
    sns.lineplot(data=dfax1, x='order_purchase_year_month', y='total_price', ax=ax1)
    ax1.set_title(f'Total de Vendas por Mês/Ano')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Total de Vendas R$')
    plt.xticks(rotation=60)
    col1.pyplot(fig1)

    dfax2 = df1[['order_purchase_year_month', 'customer_unique_id']].groupby('order_purchase_year_month').nunique().reset_index()
    fig2, ax2 = plt.subplots()
    sns.lineplot(data=dfax2, x='order_purchase_year_month', y='customer_unique_id', ax=ax2)
    ax2.set_title(f'Total de Clientes por Mês/Ano')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Total de Clientes')
    plt.xticks(rotation=60)
    col2.pyplot(fig2)

    dfax3 = df2[['order_purchase_year_month', 'seller_id']].groupby('order_purchase_year_month').nunique().reset_index()
    fig3, ax3 = plt.subplots()
    sns.lineplot(data=dfax3, x='order_purchase_year_month', y='seller_id', ax=ax3)
    ax3.set_title(f'Total de Vendedores no Estado por Mês/Ano')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Total de Vendedores')
    plt.xticks(rotation=60)
    col3.pyplot(fig3)

def rfm_analysis(df):

    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    data_atual = df['order_purchase_timestamp'].max()
    
    # Calcular as métricas RFM
    rfm = df.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': lambda x: (data_atual - x.max()).days,  # Recência
        'order_id': 'count',  # Frequência (número de pedidos)
        'total_price': 'sum'  # Monetização (valor total gasto)
    }).reset_index()

    # Renomear colunas
    rfm.columns = ['customer_unique_id', 'Recência', 'Frequência', 'Monetização']

    rfm['R_rank'] = (rfm['Recência'].rank(pct=True) * 4 + 1).astype(int)
    rfm['F_rank'] = (rfm['Frequência'].rank(pct=True) * 4 + 1).astype(int)
    rfm['M_rank'] = (rfm['Monetização'].rank(pct=True) * 4 + 1).astype(int)

    # Score final RFM (soma das pontuações)
    rfm['RFM_Score'] = rfm['R_rank'] + rfm['F_rank'] + rfm['M_rank']

    # Exibir top clientes
    top_clientes = rfm.sort_values(by='RFM_Score', ascending=False).head(10)

    col1, col2, col3 = st.columns(3)
    col1.metric("🔄 Média de Recência (dias)", f"{rfm['Recência'].mean():.0f}")
    col2.metric("📈 Média de Frequência", f"{rfm['Frequência'].mean():.1f}")
    col3.metric("💰 Média de Monetização", f"R$ {rfm['Monetização'].mean():,.2f}")

    st.divider()

    st.markdown("""
                ## 🎯 O que é o Score RFM?
                O **Score RFM** é uma métrica que classifica os clientes com base no seu comportamento de compra:

                - **🔄 Recência (R):** Quantos dias se passaram desde a última compra? *(Menor = Melhor)*
                - **📈 Frequência (F):** Quantas compras o cliente fez? *(Maior = Melhor)*
                - **💰 Monetização (M):** Quanto dinheiro o cliente gastou? *(Maior = Melhor)*

                Cada cliente recebe uma pontuação de **1 a 4** em cada métrica, e o **Score RFM** é a soma dessas três notas.  

                🔵 **Clientes com Score alto (10-12):** São os mais valiosos! 🎉  
                🟡 **Clientes com Score médio (6-9):** Compram ocasionalmente.  
                🔴 **Clientes com Score baixo (3-5):** Podem estar inativos.  

                A tabela abaixo mostra os **Top 10 Clientes** com maior Score RFM. 👇
                """)

    st.write("### 🏆 **Top 10 Clientes por Score RFM**")

    st.dataframe(top_clientes[['customer_unique_id', 'Recência', 'Frequência', 'Monetização', 'RFM_Score']],hide_index=True)

    st.subheader("🔻 10 Piores Clientes (Menor Engajamento)")

    worst_clientes = rfm.sort_values(by='RFM_Score', ascending=True).head(10)

    st.dataframe(worst_clientes[['customer_unique_id', 'Recência', 'Frequência', 'Monetização', 'RFM_Score']], hide_index=True)

    st.divider()
    
    st.subheader("Análise Gráfica das métricas de RFM")
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    rfm['Frequência_log'] = np.log1p(rfm['Frequência'])
    rfm['Monetização_log'] = np.log1p(rfm['Monetização'])

    sns.histplot(rfm['Recência'], bins=20, kde=True, ax=axes[0])
    axes[0].set_title("Distribuição da Recência (Dias)")
    
    sns.histplot(rfm['Frequência'], kde=True, ax=axes[1])
    axes[1].set_title("Distribuição da Frequência (Nº de Pedidos)")
    
    sns.histplot(rfm['Monetização_log'], bins=10, kde=True, ax=axes[2])
    axes[2].set_title("Distribuição da Monetização (R$)")
    x_ticks = axes[2].get_xticks() 
    axes[2].set_xticklabels([f"{np.expm1(x):,.0f}" for x in x_ticks]) 
    axes[2].set_xlabel("Monetização (R$)")

    st.pyplot(fig)

if __name__ == '__main__':

    params_graph()

    file_id = '1BRpzjOtt9egGwMCHe7tb0Sxs7MNm4VRN'
    ordersDF = read_drive(file_id)

    st.set_page_config(page_title='Análise de Vendas por Estado', layout='wide')

    # Titulo
    st.title('Dashboard  de Análises Avançadas')

    # Side bar
    customer_df_filtered, seller_df_filtered = filters(ordersDF)

    st.subheader("📊 Análise RFM (Recência, Frequência e Monetização)")

    rfm_analysis(customer_df_filtered)