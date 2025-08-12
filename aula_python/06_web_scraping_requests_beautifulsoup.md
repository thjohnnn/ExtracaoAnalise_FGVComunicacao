# Web Scraping com Requests e BeautifulSoup

Scraping é coletar dados de páginas web. Use com responsabilidade, respeitando termos do site.

## Instalação
```bash
pip install requests beautifulsoup4 lxml
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

## Parsear HTML com BeautifulSoup
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "lxml")  # parser mais rápido e tolerante

# Encontrar pelo nome da tag
h1 = soup.find("h1")
print("Título:", h1.get_text(strip=True) if h1 else None)

# Encontrar múltiplos elementos
links = soup.find_all("a")
for a in links[:5]:
    print(a.get("href"))

# Usar seletores CSS (poderosos)
itens = soup.select("div.card .titulo[data-role='principal']")
for item in itens:
    print(item.get_text(strip=True))

# Selecionar um só
titulo = soup.select_one("h1.site-title")
```

## Exemplo prático: buscar manchetes
```python
import time
import requests
from bs4 import BeautifulSoup

base = "https://news.ycombinator.com/"  # exemplo educativo
res = requests.get(base, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(res.text, "lxml")

manchetes = [a.get_text(strip=True) for a in soup.select("a.storylink, a.titlelink")]
for i, t in enumerate(manchetes[:10], start=1):
    print(i, t)

# Paginação (se existir)
pagina = 1
noticias = []
while pagina <= 3:
    url = f"{base}?p={pagina}"
    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, "lxml")
    noticias.extend(a.get_text(strip=True) for a in soup.select("a.titlelink"))
    time.sleep(1)  # educação com o servidor
    pagina += 1
```

## Limpeza e exportação
```python
import csv

def limpar_texto(t: str) -> str:
    return " ".join(t.split())  # normaliza espaços

registros = [(limpar_texto(t),) for t in manchetes]
with open("manchetes.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["titulo"])  # cabeçalho
    w.writerows(registros)
```

## Boas práticas e ética
- Verifique `robots.txt` do site e termos de uso.
- Adicione `User-Agent` e `timeout` nos requests.
- Evite sobrecarregar o servidor (espere entre requisições, paginação limitada).
- Prefira APIs oficiais quando existirem.
- Páginas dinâmicas (JS pesado) podem exigir ferramentas como Selenium/Playwright. Só use se for permitido e necessário.

## Exercícios
1. Extraia títulos e links de uma seção de notícias e salve em CSV com colunas `titulo`, `url`.
2. Implemente retries com backoff exponencial e limite de taxa (ex.: 1 req/s).
3. Baixe várias páginas paginadas e conte quantos itens únicos foram coletados.