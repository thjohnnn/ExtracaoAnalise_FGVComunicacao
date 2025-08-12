## 05 — Resolução de problemas comuns (no VS Code)

Lista de erros frequentes e como resolver no terminal do VS Code, focando em Windows (PowerShell) e equivalentes macOS/Linux.

### 1) `python` não é reconhecido

- Windows: instale o Python pelo site oficial e, durante a instalação, marque "Add python.exe to PATH". Tente `py -3 --version`.
- macOS: use `python3` (instale via Xcode Command Line Tools ou Homebrew).
- Linux: instale via gerenciador de pacotes da distribuição.

### 2) Falha ao ativar o `venv` no PowerShell

Erro: execução de scripts está bloqueada.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force
```

Feche e reabra o painel de terminal do VS Code, então ative novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3) `pip` instala fora do `venv`

- Certifique-se de ativar o `venv` antes de instalar (`Activate.ps1` no Windows ou `source .venv/bin/activate` em macOS/Linux).
- Verifique onde o `pip` está instalando:

```bash
which pip    # macOS/Linux
```

```powershell
Get-Command pip    # Windows PowerShell
```

### 4) Problemas com permissões ou arquivos bloqueados

- No Windows, feche arquivos abertos por outros programas (ex.: Excel) antes de apagar/mover via terminal.
- Em macOS/Linux, use `sudo` apenas se souber o que está fazendo. Evite em ambientes de estudo.

### 5) `git` não instalado ou não reconhecido

- Instale o Git (Windows: Git for Windows; macOS: Homebrew; Linux: gerenciador da distro).
- Depois, reinicie o terminal.

### 6) Conflitos de merge ao atualizar o fork (`git pull --rebase upstream main`)

- Siga as mensagens do Git no terminal do VS Code, edite os arquivos conflitados e conclua o rebase:

```bash
git status
# edite os arquivos com conflito
git add <arquivos>
git rebase --continue
```

Se ficar difícil, você pode abortar e tentar novamente:

```bash
git rebase --abort
```


