# Apps Interativos com Streamlit

Streamlit permite criar páginas web de forma simples para explorar dados e criar protótipos.

## Instalação e execução
```bash
pip install streamlit pandas matplotlib

# Executar um app
streamlit run app.py
```

## Exemplo fácil: app básico
Crie um arquivo `app.py` com:
```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("Meu primeiro app Streamlit")

nome = st.text_input("Qual é o seu nome?", "Ana")
st.write(f"Olá, {nome}!")

opcao = st.selectbox("Escolha um canal", ["YouTube", "Instagram", "TikTok"]) 
st.write("Você escolheu:", opcao)

# Tabela aleatória
st.subheader("Dados de exemplo")
df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
st.dataframe(df)
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
```

## Dicas
- Use `st.cache_data` para acelerar leituras pesadas.
- Combine com `pandas` e `seaborn` para análises visuais.
- Compartilhe o app com `streamlit share` ou hospedagens como Render/Cloud.