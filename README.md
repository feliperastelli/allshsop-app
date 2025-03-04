# AllShop Data Analytics Dashboard
## Descrição
Este projeto é uma aplicação web interativa construída com Streamlit, que permite a visualização de análises de dados da AllShop, uma loja de departamentos que opera como marketplace. O objetivo da aplicação é fornecer insights valiosos sobre o comportamento dos clientes e otimizar os processos de vendas através de análises de dados.

## A plataforma oferece duas principais categorias de análise:

**Análise Macro:** Focada em identificar tendências e padrões amplos de vendas e comportamento de clientes.
**Análise RFM (Recência, Frequência, e Valor Monetário):** Focada em segmentar os clientes com base em seu comportamento de compra.

## Tecnologias Utilizadas
- Streamlit: Para construção da interface interativa.
- Python: Linguagem de programação utilizada.
- pandas: Para manipulação e análise de dados.
- numpy: Para cálculos numéricos.
- matplotlib e seaborn: Para visualização de dados.

## Instalação
Pré-requisitos
Python 3.11.9
pip (gerenciador de pacotes do Python)

## Passos para instalação
1) Clone o repositório do projeto:

``` bash
git clone https://github.com/seu-usuario/allshop-analytics-dashboard.git
cd allshop-analytics-dashboard
```

2) Crie um ambiente virtual:

``` bash
python -m venv venv
```
3) Ative o ambiente virtual:

No Windows:
``` bash
venv\Scripts\activate
```

No MacOS/Linux:

```bash
source venv/bin/activate
```
4) Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```
5) Execute a aplicação Streamlit:

```bash
streamlit run app.py
```

6) Acesse a aplicação em seu navegador através do link fornecido no terminal.

## Como Usar
### Análise Macro: Exibe gráficos e tabelas que ajudam a identificar tendências de vendas, padrões de comportamento de clientes, e insights gerais sobre o desempenho da loja.
### Análise RFM: Segmenta os clientes em diferentes grupos com base em três métricas principais: Recência (tempo desde a última compra), Frequência (número de compras realizadas) e Valor Monetário (total gasto).

## Contribuições
Se você deseja contribuir para o projeto, siga os seguintes passos:

1) Fork o repositório.
2) Crie uma branch para a sua feature (git checkout -b feature/nova-feature).
3) Faça as alterações desejadas.
4) Envie as alterações para o repositório remoto (git push origin feature/nova-feature).
5) Abra um Pull Request.

## Licença
Este projeto é licenciado sob a MIT License.
