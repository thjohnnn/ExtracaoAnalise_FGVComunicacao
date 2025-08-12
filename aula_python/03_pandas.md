# Pandas para Análise de Dados

Pandas é a biblioteca mais popular de Python para trabalhar com dados em formato de tabela (tipo planilha do Excel).

## Instalação
```bash
pip install pandas
```

## Conceitos básicos
- `Series`: coluna única de dados.
- `DataFrame`: tabela com linhas e colunas.

## Criando dados
```python
import pandas as pd

# Series
s = pd.Series([10, 20, 30], name="vendas")

# DataFrame
dados = {
    "canal": ["YouTube", "Instagram", "TikTok", "YouTube"],
    "views": [1000, 800, 600, 1200],
    "likes": [100, 90, 70, 130],
}
df = pd.DataFrame(dados)
print(df)
```

## Lendo e salvando CSV
```python
# Ler
df = pd.read_csv("metricas.csv")  # primeira linha é o cabeçalho

# Salvar
df.to_csv("saida.csv", index=False)
```

## Seleção e filtro
```python
# Colunas
print(df["canal"])             # uma coluna
print(df[["canal", "views"]])  # várias

# Linhas por condição
filtro = df["views"] > 900
print(df[filtro])

# Loc/iloc
print(df.loc[0, "canal"])  # por rótulo
print(df.iloc[0, 0])        # por posição
```

## Operações comuns
```python
# Nova coluna
df["ctr"] = df["likes"] / df["views"]

# Ordenar
ordenado = df.sort_values(by="views", ascending=False)

# Agrupar e agregar
agrupado = (
    df.groupby("canal")["views"]
      .agg(["count", "mean", "sum"])  # quantas linhas, média e soma
      .reset_index()
)
print(agrupado)
```

## Juntar tabelas (merge)
```python
info = pd.DataFrame({
    "canal": ["YouTube", "Instagram", "TikTok"],
    "categoria": ["vídeo", "foto", "vídeo curto"],
})

resultado = df.merge(info, on="canal", how="left")
```

## Tratar valores ausentes
```python
# Ver nulos
print(df.isna().sum())

# Preencher
df["likes"] = df["likes"].fillna(0)

# Remover linhas com nulos
sem_nulos = df.dropna()
```

## Dica
- Sempre confira `df.head()` e `df.info()` para entender seus dados.
- Atenção a tipos: números como texto atrapalham contas. Use `pd.to_numeric` se precisar.