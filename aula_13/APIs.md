# APIs

### API Harry Potter

url_base: https://potterapi-fedeperin.vercel.app/pt (/en, /es, /fr, /it, /uk disponíveis)

endpoints: 

GET /[lang]/books
GET /[lang]/characters
GET /[lang]/houses
GET /[lang]/spells

Exemplo de uso: 

https://potterapi-fedeperin.vercel.app/pt/spells

Uso em Python:

```python
import requests
response = requests.get('https://potterapi-fedeperin.vercel.app/pt/books')
books = response.json()
print(books)
```

---

### Dolar API

url_base: https://br.dolarapi.com/

endpoints:

GET /v1/cotacoes
GET /v1/cotacoes/usd
GET /v1/cotacoes/eur
GET /v1/cotacoes/ars
GET /v1/cotacoes/clp
GET /v1/cotacoes/uyu

---

### Fatos inúteis

url_base: https://uselessfacts.jsph.pl/api/v2/

endpoints: 

GET /facts/today
GET /facts/random

---

### Game of Thrones

url_base: https://www.anapioficeandfire.com/api/

endpoints:

GET /books
GET /characters
GET /houses

---

### Random Fake User

url_base: https://randomuser.me/

endpoints:

GET /api

---

###  Outro Fake Generator

url_base: https://fakerapi.it/api/v2/

endpoints:

GET persons
PARAMETERS: _locale=pt_BR

Como usar: url_base + persons?_locale=pt_BR --> ATENçÃO AO ? 
