# Web Scraping com Requests e BeautifulSoup

Scraping é coletar dados de páginas web. Use com responsabilidade, respeitando termos do site.

## Instalação
```bash
pip install requests beautifulsoup4 lxml pandas
```

## Baixar HTML com Requests
```python
import requests

url = "https://example.org"
res = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
print(res.status_code)
print(res.text[:500])  # mostra os primeiros 500 caracteres
```

### Sessões e retries
```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retry))
session.headers.update({"User-Agent": "Mozilla/5.0"})

res = session.get(url, timeout=10)
```

## Parsear HTML com BeautifulSoup (prefira find/find_all)
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "lxml")  # parser mais rápido e tolerante

# Encontrar pelo nome da tag
h1 = soup.find("h1")
print("Título:", h1.get_text(strip=True) if h1 else None)

# Encontrar múltiplos elementos (links)
links = soup.find_all("a")
for a in links[:5]:
    print(a.get("href"))

# Filtrar por classe/atributos
cards = soup.find_all("div", class_="card")
for card in cards:
    titulo = card.find("span", attrs={"data-role": "principal"})
    if titulo:
        print(titulo.get_text(strip=True))

# Buscar um único elemento específico
site_title = soup.find("h1", class_="site-title")
```

> Observação: `select`/`select_one` (seletores CSS) podem ser úteis, mas priorize `find`/`find_all` por clareza e compatibilidade.

## Exemplo prático: buscar manchetes
```python
import time
import requests
from bs4 import BeautifulSoup

base = "https://news.ycombinator.com/"  # exemplo educativo
res = requests.get(base, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(res.text, "lxml")

manchetes = [
    a.get_text(strip=True)
    for a in soup.find_all("a", class_=["storylink", "titlelink"])  # classes comuns no HN
]
for i, t in enumerate(manchetes[:10], start=1):
    print(i, t)

# Paginação (se existir)
pagina = 1
noticias = []
while pagina <= 3:
    url = f"{base}?p={pagina}"
    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, "lxml")
    noticias.extend(a.get_text(strip=True) for a in soup.find_all("a", class_="titlelink"))
    time.sleep(1)  # educação com o servidor
    pagina += 1
```

## Limpeza e exportação (com pandas)
```python
import pandas as pd

def limpar_texto(t: str) -> str:
    return " ".join(t.split())  # normaliza espaços

# Criar DataFrame e exportar
manchetes_df = pd.DataFrame({"titulo": [limpar_texto(t) for t in manchetes]})
manchetes_df.to_csv("manchetes.csv", index=False, encoding="utf-8")
```

## Boas práticas e ética
- Verifique `robots.txt` do site e termos de uso.
- Adicione `User-Agent` e `timeout` nos requests.
- Evite sobrecarregar o servidor (espere entre requisições, paginação limitada).
- Prefira APIs oficiais quando existirem.
- Páginas dinâmicas (JS pesado) podem exigir ferramentas como Selenium/Playwright. Só use se for permitido e necessário.

## Exercícios
1. Extraia títulos e links de uma seção de notícias e salve em CSV com colunas `titulo`, `url` usando pandas.
2. Implemente retries com backoff exponencial e limite de taxa (ex.: 1 req/s).
3. Baixe várias páginas paginadas e conte quantos itens únicos foram coletados.