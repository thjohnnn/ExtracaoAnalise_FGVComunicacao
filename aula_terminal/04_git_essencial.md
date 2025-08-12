## 04 — Git essencial para o curso (no VS Code)

Conjunto mínimo de comandos Git para acompanhar o curso usando o terminal do VS Code, com foco em clonar, atualizar, forkar e trabalhar sem afetar o repositório do professor.

### Configuração inicial (uma vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### Clonar o repositório do curso (somente leitura)

```bash
git clone https://github.com/mateuspestana/ExtracaoAnalise_FGVComunicacao
cd ExtracaoAnalise_FGVComunicacao
```

Atualizar:

```bash
git pull
```

### Fork (recomendado)

1) Faça um fork no GitHub para a sua conta.
2) Clone seu fork:

```bash
git clone https://github.com/SEU_USUARIO/ExtracaoAnalise_FGVComunicacao
cd ExtracaoAnalise_FGVComunicacao
```

3) Aponte `upstream` para o repositório do professor:

```bash
git remote add upstream https://github.com/mateuspestana/ExtracaoAnalise_FGVComunicacao
git remote -v
```

4) Sincronizar novidades do professor para o seu fork:

```bash
git fetch upstream
git checkout main
git pull --rebase upstream main
git push origin main
```

### Cópia para repositório de anotações (alternativa)

Crie um repositório seu e copie os arquivos da disciplina (sem a pasta `.git`). No Windows, use `robocopy`; no macOS/Linux, use `rsync`.

Windows PowerShell:

```powershell
robocopy "C:\caminho\ExtracaoAnalise_FGVComunicacao" "C:\caminho\MinhasAnotacoesDados" /E /XD .git .venv
```

macOS/Linux:

```bash
rsync -av --exclude='.git' --exclude='.venv' /caminho/ExtracaoAnalise_FGVComunicacao/ /caminho/MinhasAnotacoesDados/
```

### Ciclo básico de trabalho no seu repositório

```bash
git status
git add .
git commit -m "Mensagem do que mudou"
git push origin main
```

No VS Code, você pode também usar a aba Source Control para visualizar alterações, fazer stage (`+`), commit e push com botões.


