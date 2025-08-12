# Visualização com Matplotlib e Seaborn

Gráficos ajudam a contar histórias com dados. Vamos ver o básico de `matplotlib` e `seaborn`.

## Instalação
```bash
pip install matplotlib seaborn pandas
```

## Matplotlib básico
```python
import matplotlib.pyplot as plt

# Linha
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.plot(x, y, marker="o")
plt.title("Evolução de Views")
plt.xlabel("Semana")
plt.ylabel("Views")
plt.show()

# Barras
categorias = ["YouTube", "Instagram", "TikTok"]
valores = [1200, 800, 600]
plt.bar(categorias, valores, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
plt.title("Views por Canal")
plt.show()

# Histograma
import numpy as np

amostras = np.random.normal(loc=100, scale=15, size=200)
plt.hist(amostras, bins=20, color="#1f77b4")
plt.title("Distribuição de Views")
plt.show()
```

## Seaborn básico
Seaborn simplifica e estiliza os gráficos.
```python
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")

df = pd.DataFrame({
    "canal": ["YouTube", "Instagram", "TikTok", "YouTube", "Instagram", "TikTok"],
    "views": [1200, 800, 600, 1400, 900, 700],
    "likes": [130, 90, 70, 150, 95, 75],
})

# Dispersão (relação entre duas variáveis)
sns.scatterplot(data=df, x="views", y="likes", hue="canal")
plt.title("Likes vs Views por Canal")
plt.show()

# Barras (média por categoria)
sns.barplot(data=df, x="canal", y="views", estimator=sum, ci=None)
plt.title("Soma de Views por Canal")
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

## Dicas
- Use títulos e rótulos claros; conte a história do dado.
- Evite poluição visual; menos é mais.
- Cores consistentes ajudam a leitura.