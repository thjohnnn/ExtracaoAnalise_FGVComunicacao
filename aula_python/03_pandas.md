# Pandas para Análise de Dados

Pandas é a biblioteca mais popular de Python para trabalhar com dados em formato de tabela (tipo planilha do Excel).

## Instalação
```bash
pip install pandas numpy
```

## Conceitos básicos
- `Series`: coluna única de dados, com um índice.
- `DataFrame`: tabela com linhas e colunas.
- `Index`: rótulos das linhas e colunas (eixo). Ajuda na alinhamento de operações.
- `dtype`: tipo de dados de cada coluna (ex.: `int64`, `float64`, `object`, `category`, `datetime64[ns]`).

## Criando dados
```python
import pandas as pd
import numpy as np

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
# parse_dates tenta converter colunas para datas
# sep e encoding variam conforme a origem do arquivo
sales = pd.read_csv("metricas.csv", sep=",", encoding="utf-8", parse_dates=["data"], dayfirst=True)

# Salvar
sales.to_csv("saida.csv", index=False)
```

## Inspeção inicial
```python
print(df.head())     # primeiras linhas
print(df.tail())     # últimas linhas
print(df.info())     # tipos e nulos
print(df.describe()) # estatísticas numéricas básicas
```

## Seleção e filtro
```python
# Colunas
df["canal"]                 # Series
df[["canal", "views"]]     # DataFrame

# Linhas por condição
filtro = df["views"] > 900
high = df[filtro]

# loc/iloc
valor = df.loc[0, "canal"]  # por rótulo
valor2 = df.iloc[0, 0]        # por posição

# Múltiplas condições (use parênteses)
engajado = df[(df["views"] > 700) & (df["likes"] >= 90)]

# isin e query
subset = df[df["canal"].isin(["YouTube", "TikTok"])]
subset2 = df.query("views >= 800 and canal != 'Instagram'")
```

## Operações comuns
```python
# Nova coluna (vetorizado)
df["ctr"] = df["likes"] / df["views"]

# Transformações
df["likes_log"] = (df["likes"] + 1).pipe(np.log)

# map/apply
mapa_categorias = {"YouTube": "vídeo", "Instagram": "foto", "TikTok": "vídeo curto"}
df["categoria"] = df["canal"].map(mapa_categorias)

def escala_100(x: pd.Series) -> pd.Series:
    return 100 * (x - x.min()) / (x.max() - x.min())

num_cols = ["views", "likes"]
df[[c + "_norm" for c in num_cols]] = df[num_cols].apply(escala_100)

# Ordenar
ordenado = df.sort_values(by=["views", "likes"], ascending=[False, False])
```

## Agrupar e agregar
```python
agrupado = (
    df.groupby("canal")["views"]
      .agg(contagem="count", media="mean", soma="sum")
      .reset_index()
)

# Usando múltiplas colunas e transform
zscore = (
    df.groupby("canal")["views"]
      .transform(lambda x: (x - x.mean()) / x.std(ddof=0))
)
df["views_z"] = zscore

# Tabelas dinâmicas
pivot = pd.pivot_table(
    df, values="views", index="canal", columns=None, aggfunc=["mean", "sum"], fill_value=0
)
```

## Juntar tabelas (merge/concat)
```python
info = pd.DataFrame({
    "canal": ["YouTube", "Instagram", "TikTok"],
    "categoria": ["vídeo", "foto", "vídeo curto"],
})

# inner, left, right, outer
resultado = df.merge(info, on="canal", how="left")

# Concatenar várias tabelas
partes = [df.iloc[:2], df.iloc[2:]]
unido = pd.concat(partes, ignore_index=True)
```

## Tratar valores ausentes
```python
# Ver nulos
print(df.isna().sum())

# Preencher
df["likes"] = df["likes"].fillna(0)

# Remover linhas com nulos
sem_nulos = df.dropna(subset=["views"])   # só se views for nulo

# Interpolar séries temporais
serie = pd.Series([1, None, 3, None, 5])
serie_interp = serie.interpolate()
```

## Datas e tempos
```python
# Conversão
vendas = pd.DataFrame({
    "data": ["2024-01-01", "2024-01-02", "2024-01-03"],
    "views": [100, 120, 90],
})
vendas["data"] = pd.to_datetime(vendas["data"])  # datetime64[ns]

# Atributos dt
vendas["ano"] = vendas["data"].dt.year
vendas["mes"] = vendas["data"].dt.month

# Reamostrar (séries temporais com índice de data)
serie = vendas.set_index("data")["views"].resample("D").sum()
```

## Tipos categóricos e memória
```python
df["canal"] = df["canal"].astype("category")
print(df["canal"].cat.categories)
```

## Performance e armadilhas
- Prefira operações vetorizadas a `for`/`apply` sempre que possível.
- Evite encadeamento de indexação ("chained indexing"): `df[cond]["col"] = ...` pode não ter efeito. Prefira `df.loc[cond, "col"] = ...`.
- Cópia vs view: use `df.copy()` quando precisar de uma cópia independente.
- Ao lidar com grandes CSVs, use `usecols`, `dtype`, `chunksize` no `read_csv`.

## Dica
- Sempre confira `df.head()` e `df.info()` para entender seus dados.
- Atenção a tipos: números como texto atrapalham contas. Use `pd.to_numeric` se precisar.

## Exercícios
1. Carregue um CSV com colunas `data`, `canal`, `views` e calcule a média de `views` por mês e canal.
2. Some `likes` por canal e crie uma coluna `ctr = likes / views` ordenando do maior para o menor.
3. Una duas tabelas (`posts` e `autores`) pelo `autor_id` e crie um ranking por autor.
4. Dado um DataFrame com valores nulos, experimente diferentes estratégias de imputação (`fillna`, `interpolate`) e compare os resultados.