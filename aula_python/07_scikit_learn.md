# Introdução ao scikit-learn (Machine Learning)

`scikit-learn` é uma biblioteca de ML com ferramentas para classificação, regressão, agrupamento e mais. Vamos focar em exemplos simples e práticos.

## Instalação
```bash
pip install scikit-learn pandas numpy joblib
```

## Conceitos rápidos
- **Treino/Teste**: separe dados para treinar e avaliar o modelo.
- **Features**: colunas que explicam o fenômeno (variáveis independentes).
- **Alvo (target)**: o que queremos prever.
- **Validação cruzada**: avaliar o modelo em diferentes divisões dos dados.

## Exemplo fácil: classificar flores Iris
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Dados
X, y = load_iris(return_X_y=True)

# Separar treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Modelo
model = LogisticRegression(max_iter=1000, n_jobs=None)
model.fit(X_train, y_train)

# Avaliação
pred = model.predict(X_test)
print("Acurácia:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
```

## Exemplo: regressão linear
```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

rng = np.random.default_rng(42)
X = np.arange(0, 100).reshape(-1, 1)
y = 2.5 * X.squeeze() + 10 + rng.normal(0, 5, size=len(X))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
reg = LinearRegression().fit(X_train, y_train)
pred = reg.predict(X_test)
print("MAE:", mean_absolute_error(y_test, pred))
print("R2:", r2_score(y_test, pred))
```

## Pipeline com pré-processamento (numérico + categórico)
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Exemplo com dados tabulares (substitua por seu CSV)
df = pd.DataFrame({
    "canal": ["YouTube", "Instagram", "TikTok", "YouTube", "TikTok", "Instagram"],
    "views": [100, 200, 150, 180, 90, 300],
    "likes": [10, 25, 15, 22, 8, 40],
    "compart": [2, 5, 3, 4, 1, 8],
    "viral": [0, 1, 0, 1, 0, 1],
})

X = df[["canal", "views", "likes", "compart"]]
y = df["viral"]

num_cols = ["views", "likes", "compart"]
cat_cols = ["canal"]

preprocess = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
])

pipe = Pipeline([
    ("prep", preprocess),
    ("rf", RandomForestClassifier(n_estimators=200, random_state=42)),
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
print(classification_report(y_test, pred))
```

## Busca de hiperparâmetros
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "rf__n_estimators": [100, 200, 400],
    "rf__max_depth": [None, 5, 10],
}

grid = GridSearchCV(pipe, param_grid, cv=3, n_jobs=-1)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)
```

## Salvar e carregar modelo
```python
import joblib

joblib.dump(pipe, "modelo.pkl")
modelo = joblib.load("modelo.pkl")
```

## Dicas
- Sempre avalie com dados que o modelo não viu (teste ou validação cruzada).
- Evite vazamento de dados: faça pré-processamento dentro do `Pipeline`.
- Controle a aleatoriedade com `random_state` para reprodutibilidade.
- Comece simples e só complique se necessário.

## Exercícios
1. Aplique `GridSearchCV` para tunar um `LogisticRegression` (parâmetros C e penalty) e compare.
2. Construa um `Pipeline` com `ColumnTransformer` para um dataset com colunas categóricas e numéricas próprios.
3. Calcule matriz de confusão e curva ROC para um classificador (ex.: `sklearn.metrics.roc_auc_score`).