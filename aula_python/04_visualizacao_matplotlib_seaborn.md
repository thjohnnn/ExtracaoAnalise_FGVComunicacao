# Visualização com Matplotlib e Seaborn

Gráficos ajudam a contar histórias com dados. Vamos ver o básico de `matplotlib` e `seaborn`.

## Instalação
```bash
pip install matplotlib seaborn pandas numpy
```

## Matplotlib básico
```python
import matplotlib.pyplot as plt

# Tamanho e estilo
dpi = 120
plt.style.use("seaborn-v0_8-whitegrid")

# Linha
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.figure(figsize=(6, 3.5), dpi=dpi)
plt.plot(x, y, marker="o", linewidth=2, color="#1f77b4", label="views")
plt.title("Evolução de Views")
plt.xlabel("Semana")
plt.ylabel("Views")
plt.legend()
plt.tight_layout()
plt.show()

# Barras
categorias = ["YouTube", "Instagram", "TikTok"]
valores = [1200, 800, 600]
plt.figure(figsize=(6, 3.5), dpi=dpi)
plt.bar(categorias, valores, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
plt.title("Views por Canal")
plt.tight_layout()
plt.show()

# Histograma
import numpy as np
amostras = np.random.normal(loc=100, scale=15, size=200)
plt.figure(figsize=(6, 3.5), dpi=dpi)
plt.hist(amostras, bins=20, color="#1f77b4", edgecolor="white")
plt.title("Distribuição de Views")
plt.tight_layout()
plt.show()
```

## Subplots e eixos gêmeos
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5), dpi=120)
ax1.plot([1,2,3], [2,3,2], marker="o")
ax1.set_title("Linha")
ax2.bar(["A","B","C"], [3,1,4])
ax2.set_title("Barras")
fig.suptitle("Exemplos lado a lado", y=1.02)
fig.tight_layout()
plt.show()

# Eixos gêmeos (escala diferente)
fig, ax = plt.subplots(figsize=(6,3.5), dpi=120)
x = np.arange(0, 10, 1)
views = x ** 1.5
likes = np.sqrt(x + 1)
ax.plot(x, views, color="#1f77b4", label="views")
ax.set_ylabel("views", color="#1f77b4")
ax2 = ax.twinx()
ax2.plot(x, likes, color="#ff7f0e", label="likes")
ax2.set_ylabel("likes", color="#ff7f0e")
plt.title("Views e Likes")
fig.tight_layout()
plt.show()
```

## Anotações e salvar figura
```python
fig, ax = plt.subplots(figsize=(6, 3.5), dpi=120)
ax.plot([1,2,3,4], [10, 20, 15, 25], marker="o")
ax.annotate("pico", xy=(2, 20), xytext=(2.5, 22),
            arrowprops=dict(arrowstyle="->", color="gray"))
ax.set_title("Evolução de Views")
fig.tight_layout()
fig.savefig("views.png", dpi=200)
plt.show()
```

## Seaborn básico
Seaborn simplifica e estiliza os gráficos.
```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="talk")

df = pd.DataFrame({
    "canal": ["YouTube", "Instagram", "TikTok", "YouTube", "Instagram", "TikTok"],
    "views": [1200, 800, 600, 1400, 900, 700],
    "likes": [130, 90, 70, 150, 95, 75],
})

# Dispersão (relação entre duas variáveis)
sns.scatterplot(data=df, x="views", y="likes", hue="canal", s=80)
plt.title("Likes vs Views por Canal")
plt.show()

# Barras (estatística por categoria)
sns.barplot(data=df, x="canal", y="views", estimator=sum, ci=None)
plt.title("Soma de Views por Canal")
plt.show()

# Linha (evolução)
sns.lineplot(data=df, x="views", y="likes", hue="canal")
plt.title("Likes em função de Views")
plt.show()

# Distribuição
sns.histplot(data=df, x="views", kde=True)
plt.title("Distribuição de Views")
plt.show()

# Boxplot (distribuição por categoria)
sns.boxplot(data=df, x="canal", y="likes")
plt.title("Likes por Canal")
plt.show()
```

## Pairplot, Heatmap e FacetGrid
```python
# Pairplot: relações pairwise e distribuições
sns.pairplot(df, hue="canal")
plt.show()

# Heatmap de correlações
corr = df.drop(columns=["canal"]).corr()
sns.heatmap(corr, annot=True, cmap="Blues", vmin=0, vmax=1)
plt.title("Correlação")
plt.show()

# FacetGrid: múltiplos gráficos por facetas
penguins = sns.load_dataset("penguins").dropna()
g = sns.FacetGrid(penguins, col="species", row="sex")
g.map_dataframe(sns.scatterplot, x="bill_length_mm", y="bill_depth_mm")
g.add_legend()
plt.show()
```

## Paletas e contextos
```python
sns.set_theme(style="whitegrid", context="paper", palette="Set2")
```

## Dicas
- Use títulos e rótulos claros; conte a história do dado.
- Evite poluição visual; menos é mais.
- Cores consistentes ajudam a leitura.
- Lembre de `tight_layout()` e `savefig()` para exportar.

## Exercícios
1. Recrie um gráfico de barras com erro padrão (use `estimator=np.mean`, `errorbar=('ci', 95)`).
2. Faça um `FacetGrid` com 2 variáveis categóricas e um `scatterplot` para explorar padrões.
3. Construa um `heatmap` de correlações com `annot=True` para um DataFrame próprio e interprete os resultados.