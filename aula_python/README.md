# Aula de Python: Roteiro e Guia

Este diretório reúne materiais introdutórios e práticos para começar com Python, análise de dados e desenvolvimento de APIs/Apps.

## Pré-requisitos
- Python 3.10+ instalado
- Editor (VS Code, Cursor) e terminal
- Opcional: Anaconda/Miniconda

## Setup rápido
```bash
# (opcional) ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instalar pacotes conforme for usando cada aula
pip install -r ../requirements.txt  # se existir
```

## Roteiro das aulas
- [01_python_basico.md](./01_python_basico.md): tipos, estruturas, funções, classes e IO.
- [02_estruturas_de_controle.md](./02_estruturas_de_controle.md): if/elif/else, loops, comprehensions e exceções.
- [03_pandas.md](./03_pandas.md): DataFrames, filtros, groupby, joins, datas e boas práticas.
- [04_visualizacao_matplotlib_seaborn.md](./04_visualizacao_matplotlib_seaborn.md): gráficos com Matplotlib/Seaborn, subplots e estilos.
- [05_streamlit.md](./05_streamlit.md): apps interativos, layouts, cache e estado.
- [06_web_scraping_requests_beautifulsoup.md](./06_web_scraping_requests_beautifulsoup.md): scraping responsável, seletores e exportação.
- [07_scikit_learn.md](./07_scikit_learn.md): pipelines, validação e busca de hiperparâmetros.
- [08_fastapi.md](./08_fastapi.md): endpoints, validações, dependências, routers e CORS.

## Como rodar exemplos
- Scripts Python: `python3 arquivo.py`
- Streamlit: `streamlit run app.py`
- FastAPI: `uvicorn main:app --reload` e acesse `http://localhost:8000/docs`

## Dicas gerais
- Prefira nomes claros e funções curtas.
- Faça inspeções iniciais (`head`, `info`) ao abrir dados.
- Documente decisões e trate erros previsíveis.

Bom estudo! 🚀