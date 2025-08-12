# Web Scraping com Requests e BeautifulSoup

Scraping é coletar dados de páginas web. Use com responsabilidade, respeitando termos do site.

## Instalação
```bash
pip install requests beautifulsoup4
```

## Baixar HTML com Requests
```python
import requests

url = "https://example.org"
res = requests.get(url, timeout=10)
print(res.status_code)
print(res.text[:500])  # mostra os primeiros 500 caracteres
```

## Parsear HTML com BeautifulSoup
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "html.parser")

# Encontrar pelo nome da tag
h1 = soup.find("h1")
print("Título:", h1.get_text(strip=True))

# Encontrar múltiplos elementos
links = soup.find_all("a")
for a in links[:5]:
    print(a.get("href"))

# Usar seletores CSS
itens = soup.select("div.card .titulo")
for item in itens:
    print(item.get_text(strip=True))
```

## Exemplo prático: buscar manchetes
```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"  # exemplo educativo
res = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(res.text, "html.parser")

manchetes = [a.get_text(strip=True) for a in soup.select("a.storylink, a.titlelink")]
for i, t in enumerate(manchetes[:10], start=1):
    print(i, t)
```

## Boas práticas e ética
- Verifique `robots.txt` do site e termos de uso.
- Adicione `User-Agent` e `timeout` nos requests.
- Evite sobrecarregar o servidor (espere entre requisições).
- Prefira APIs oficiais quando existirem.