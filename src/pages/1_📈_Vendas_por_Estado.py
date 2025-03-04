import pandas as pd
import streamlit as st
import seaborn as sns   
import matplotlib.pyplot as plt
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

    # Filtro de valor pedido
    valor_min = df['total_price'].min()
    valor_max = df['total_price'].max()
    valor_selecionado = st.sidebar.slider('Selecione um intervalo de valor (R$) para o item', valor_min, valor_max, (valor_min, valor_max))

    # filtro de data
    periodo = df['order_purchase_year_month'].unique()
    data_selecionado = st.sidebar.multiselect('Selecione os períodos (Mês/Ano)', options=periodo, default=periodo)

    customer_df_filtered = df[(ordersDF['customer_state'].isin(estados_selecionado)) & 
                              (ordersDF['order_status'].isin(status_selecionado)) & 
                              (ordersDF['total_price'].between(valor_selecionado[0], valor_selecionado[1])) 
                              & (ordersDF['order_purchase_year_month'].isin(periodo))]
    
    seller_df_filtered = df[(ordersDF['seller_state'].isin(estados_selecionado)) &
                            (ordersDF['order_status'].isin(status_selecionado)) &
                            (ordersDF['total_price'].between(valor_selecionado[0], valor_selecionado[1]))
                            & (ordersDF['order_purchase_year_month'].isin(periodo))]

    return customer_df_filtered, seller_df_filtered

def big_numbers(df1, df2):
    total_vendas = df1['total_price'].sum()
    total_customers = df1['customer_id'].nunique()
    total_sellers = df2['seller_id'].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric('Total de Vendas', f'R$ {total_vendas:,.2f}')
    col2.metric('Total de Clientes', f"{total_customers:,.0f}")
    col3.metric('Total de Vendedores', f"{total_sellers:,.0f}")

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

if __name__ == '__main__':

    params_graph()

    file_id = '1BRpzjOtt9egGwMCHe7tb0Sxs7MNm4VRN'
    ordersDF = read_drive(file_id)

    st.set_page_config(page_title='Análise de Vendas por Estado', layout='wide')

    # Titulo
    st.title('Dashboard  de Análise de Vendas por Estado')

    # Side bar
    customer_df_filtered, seller_df_filtered = filters(ordersDF)

    # -----------------------------------Big Numbers
    st.subheader('Indicadores Gerais')

    big_numbers(customer_df_filtered, seller_df_filtered)

    # -----------------------------------Visões Gerais
    st.subheader('Visão Geral das Vendas por Estado')

    overview(customer_df_filtered, seller_df_filtered)

    # -----------------------------------Visões Temporais para o Estado Selecionado

    st.subheader('Visão Temporal por Estado')

    temporal_visions(customer_df_filtered, seller_df_filtered)