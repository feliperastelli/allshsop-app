import streamlit as st

st.set_page_config(
    page_title="AllShop - Dashboards",
    page_icon="👋",
)

st.write("# Olá, bem vindo ao Dash da AllShop! 👋")

st.sidebar.success("Selecione uma categoria de análise")

st.markdown(
    """
    A AllShop é uma loja de departamentos que opera como marketplace, conectando diversos vendedores a consumidores em uma única plataforma. 
    Com um amplo portfólio de produtos, a empresa busca oferecer variedade, conveniência e preços competitivos. 
    Nos últimos anos, a AllShop experimentou um crescimento acelerado, impulsionado pela digitalização do varejo e pelo aumento da demanda por compras online.

    No entanto, esse crescimento trouxe desafios complexos na gestão de dados, dificultando a tomada de decisões estratégicas. 
    Para aprimorar sua eficiência operacional e competitividade, a empresa está investindo em análises de dados para compreender melhor o comportamento dos clientes, otimizar processos de vendas 
    e melhorar a experiência do consumidor.

    A AllShop utiliza dados de pedidos e transações para identificar tendências de mercado, aperfeiçoar seu modelo de negócios e fortalecer sua presença no setor de marketplaces.
"""
)

st.markdown(
    """
         **👈 Selecione uma das análises disponíveis ao lado**
"""
)