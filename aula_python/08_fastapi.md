# APIs Rápidas com FastAPI

FastAPI é um framework moderno para criar APIs em Python, rápido e fácil de usar. Ótimo para conectar seu modelo/ análise de dados a uma interface web ou outros sistemas.

## Instalação
```bash
pip install fastapi uvicorn[standard] pydantic
```

## Executar o servidor
```bash
uvicorn main:app --reload
```
- `main` é o nome do arquivo `main.py`.
- `app` é o objeto FastAPI dentro desse arquivo.
- `--reload` recarrega automático quando o código muda.

## Exemplo fácil: Hello, API!
Crie `main.py`:
```python
from fastapi import FastAPI

app = FastAPI(title="Minha API")

@app.get("/")
def root():
    return {"mensagem": "Olá, mundo!"}

@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    return {"oi": nome}
```

Rode com `uvicorn main:app --reload` e acesse `http://localhost:8000/docs` para a documentação interativa automática.

## Parâmetros de query
```python
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/busca")
def buscar(q: Optional[str] = None, limite: int = 10):
    return {"query": q, "limite": limite}
```

## Validação com modelos (Pydantic)
```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Usuario(BaseModel):
    nome: str = Field(..., min_length=2)
    email: str
    idade: int | None = None

@app.post("/usuarios")
def criar_usuario(user: Usuario):
    return {"ok": True, "dados": user}
```

## Exemplo médio: CRUD simples de tarefas
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List

app = FastAPI(title="Tarefas API")

class Tarefa(BaseModel):
    id: UUID
    titulo: str
    feito: bool = False

# "Banco" em memória
TAREFAS: list[Tarefa] = []

@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    return TAREFAS

@app.post("/tarefas", response_model=Tarefa, status_code=201)
def criar_tarefa(titulo: str):
    tarefa = Tarefa(id=uuid4(), titulo=titulo, feito=False)
    TAREFAS.append(tarefa)
    return tarefa

@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: UUID, feito: bool):
    for t in TAREFAS:
        if t.id == tarefa_id:
            t.feito = feito
            return t
    raise HTTPException(404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{tarefa_id}", status_code=204)
def remover_tarefa(tarefa_id: UUID):
    global TAREFAS
    antes = len(TAREFAS)
    TAREFAS = [t for t in TAREFAS if t.id != tarefa_id]
    if len(TAREFAS) == antes:
        raise HTTPException(404, detail="Tarefa não encontrada")
```

Teste pelos `docs` em `http://localhost:8000/docs`.

## Dicas
- Use `response_model` para documentar e validar saídas.
- Adicione CORS se for consumir do navegador:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
- Para produção, use `uvicorn`/`gunicorn` e um proxy (Nginx) ou serviços gerenciados.