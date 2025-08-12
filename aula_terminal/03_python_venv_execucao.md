## 03 — Python: `venv`, `pip` e execução de scripts (no VS Code)

Nesta aula, você vai criar um ambiente virtual, instalar dependências e rodar scripts Python usando o terminal integrado do VS Code.

### Checar Python e pip

```powershell
# Windows PowerShell (VS Code Terminal)
python --version
pip --version
```

```bash
# macOS/Linux (VS Code Terminal)
python3 --version
pip3 --version
```

Se o comando `python` não funcionar no Windows, tente `py -3 --version`. Em macOS/Linux, use `python3`/`pip3`.

### Criar e ativar um ambiente virtual (`venv`)

```powershell
# Windows PowerShell (VS Code Terminal)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux (VS Code Terminal)
python3 -m venv .venv
source .venv/bin/activate
```

Desativar:

```bash
deactivate
```

### Instalar dependências do curso

Com o `venv` ativo, execute:

```bash
pip install --upgrade pip
pip install -r requirements.py
```

Sempre que atualizar o repositório do curso, rode novamente:

```bash
pip install -r requirements.py
```

### Executar scripts Python

```powershell
# Windows PowerShell (VS Code Terminal)
python aula_04\seu_script.py
```

```bash
# macOS/Linux (VS Code Terminal)
python3 aula_04/seu_script.py
```

### Jupyter e notebooks (opcional)

Para usar notebooks, instale e inicie o Jupyter no `venv`:

```bash
pip install ipykernel jupyter
jupyter notebook
```

No VS Code, você também pode usar a extensão "Python" para executar células interativas e notebooks diretamente no editor.


