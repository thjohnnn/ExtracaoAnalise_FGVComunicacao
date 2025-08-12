# Introdução ao scikit-learn (Machine Learning)

`scikit-learn` é uma biblioteca de ML com ferramentas para classificação, regressão, agrupamento e mais. Vamos focar em exemplos simples e práticos.

## Instalação
```bash
pip install scikit-learn pandas numpy
```

## Conceitos rápidos
- **Treino/Teste**: separe dados para treinar e avaliar o modelo.
- **Features**: colunas que explicam o fenômeno (variáveis independentes).
- **Alvo (target)**: o que queremos prever.

## Exemplo fácil: classificar flores Iris
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Dados
X, y = load_iris(return_X_y=True)

# Separar treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Avaliação
pred = model.predict(X_test)
print("Acurácia:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
```

## Exemplo médio: pipeline com padronização
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Exemplo com dados tabulares (substitua por seu CSV)
df = pd.DataFrame({
    "views": [100, 200, 150, 180, 90, 300],
    "likes": [10, 25, 15, 22, 8, 40],
    "compart": [2, 5, 3, 4, 1, 8],
    "viral": [0, 1, 0, 1, 0, 1],
})

X = df[["views", "likes", "compart"]]
y = df["viral"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("rf", RandomForestClassifier(n_estimators=200, random_state=42)),
])

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
print(classification_report(y_test, pred))
```

## Dicas
- Sempre avalie com dados que o modelo não viu (teste ou validação cruzada).
- Evite overfitting com regularização, menos complexidade e mais dados.
- Comece simples e só complique se necessário.