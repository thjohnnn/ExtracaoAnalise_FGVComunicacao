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

## Parâmetros de query e validações
```python
from typing import Optional
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/busca")
def buscar(q: Optional[str] = Query(None, min_length=2, max_length=50), limite: int = Query(10, ge=1, le=100)):
    return {"query": q, "limite": limite}

@app.get("/itens/{item_id}")
def get_item(item_id: int = Path(..., ge=1)):
    return {"id": item_id}
```

## Validação com modelos (Pydantic)
```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class Usuario(BaseModel):
    nome: str = Field(..., min_length=2)
    email: EmailStr
    idade: int | None = Field(default=None, ge=0)

@app.post("/usuarios", response_model=Usuario, status_code=201)
def criar_usuario(user: Usuario):
    return user
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

## Dependências (injeção)
```python
from fastapi import Depends

def get_db():
    # Retorne uma conexão/sessão real na prática
    return {"conn": "fake"}

@app.get("/status")
def status(db = Depends(get_db)):
    return {"ok": True, "db": bool(db)}
```

## Tarefas em segundo plano
```python
from fastapi import BackgroundTasks

@app.post("/processar")
def processar(background_tasks: BackgroundTasks, dado: str):
    def tarefa():
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(dado + "\n")
    background_tasks.add_task(tarefa)
    return {"agendado": True}
```

## Routers e organização
```python
from fastapi import APIRouter, FastAPI

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/ping")
def ping():
    return {"pong": True}

app = FastAPI()
app.include_router(router)
```

## Middleware simples
```python
from fastapi import Request

@app.middleware("http")
async def log_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App"] = "MinhaAPI"
    return response
```

## Autenticação simples (API Key)
```python
from fastapi import Header, HTTPException

API_KEY = "segredo"

async def check_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(401, detail="API key inválida")

@app.get("/segredo", dependencies=[Depends(check_api_key)])
async def segredo():
    return {"ok": True}
```

## CORS
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

## Dicas
- Use `response_model` para documentar e validar saídas.
- Tipos assíncronos (`async def`) escalam melhor IO.
- Para produção, use `uvicorn`/`gunicorn` e um proxy (Nginx) ou serviços gerenciados.
- Teste endpoints com `pytest` + `httpx.AsyncClient`.

## Exercícios
1. Separe seu CRUD em um `APIRouter` e inclua com `include_router`.
2. Adicione paginação (parâmetros `offset` e `limit`) à lista de tarefas.
3. Proteja um endpoint com API key via header e retorne 401 quando inválida.