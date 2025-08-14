# Apps Interativos com Streamlit

Streamlit permite criar páginas web de forma simples para explorar dados e criar protótipos.

## Instalação e execução
```bash
pip install streamlit pandas matplotlib numpy

# Executar um app
streamlit run app.py
```

## Exemplo fácil: app básico
Crie um arquivo `app.py` com:
```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Meu app", page_icon="📊", layout="wide")
st.title("Meu primeiro app Streamlit")

nome = st.text_input("Qual é o seu nome?", "Ana")
st.write(f"Olá, {nome}!")

opcao = st.selectbox("Escolha um canal", ["YouTube", "Instagram", "TikTok"]) 
st.write("Você escolheu:", opcao)

# Layout em colunas
col1, col2 = st.columns(2)
with col1:
    st.subheader("Tabela aleatória")
    df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
    st.dataframe(df)
with col2:
    st.subheader("Estatísticas")
    st.write(df.describe())
```

Execute `streamlit run app.py` e abra o link no navegador.

## Exemplo médio: upload de CSV e gráfico
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analisador de CSV")

arquivo = st.file_uploader("Envie um CSV", type=["csv"]) 
if arquivo:
    df = pd.read_csv(arquivo)
    st.subheader("Prévia dos dados")
    st.dataframe(df.head())

    coluna = st.selectbox("Coluna numérica para histograma", df.select_dtypes(include="number").columns)

    fig, ax = plt.subplots()
    ax.hist(df[coluna].dropna(), bins=20, color="#1f77b4")
    ax.set_title(f"Distribuição: {coluna}")
    st.pyplot(fig)

    # Download do CSV processado
    st.download_button(
        "Baixar amostra",
        data=df.head(100).to_csv(index=False).encode("utf-8"),
        file_name="amostra.csv",
        mime="text/csv",
    )
```

## Sidebar, Tabs e Forms
```python
st.sidebar.header("Configurações")
alpha = st.sidebar.slider("Opacidade", 0.1, 1.0, 0.8)

aba1, aba2 = st.tabs(["Tabela", "Gráfico"]) 

with st.form("filtro_form"):
    minimo = st.number_input("Mínimo de views", value=0)
    submitted = st.form_submit_button("Aplicar")

st.write("Aplicado:", submitted, minimo)
```

## Estado e cache
```python
# Estado (entre interações)
if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("+1"):
    st.session_state.contador += 1

st.write("Contador:", st.session_state.contador)

# Cache de dados e recursos
@st.cache_data(ttl=600)
def carregar_csv(caminho: str) -> pd.DataFrame:
    return pd.read_csv(caminho)

@st.cache_resource
def get_modelo_carregado():
    import joblib
    return joblib.load("modelo.pkl")
```

## Dicas
- Use `st.cache_data` para acelerar leituras pesadas.
- Combine com `pandas` e `seaborn` para análises visuais.
- Use `st.sidebar` para filtros e configurações.
- `st.secrets` guarda credenciais com segurança.
- Compartilhe o app com `streamlit share` ou hospedagens como Render/Cloud.

## Exercícios
1. Crie um app com filtros por categoria e um gráfico que responde aos filtros.
2. Adicione `st.cache_data` para a função que lê dados e meça o ganho.
3. Implemente um formulário (`st.form`) que valida entradas e gera um relatório para download.