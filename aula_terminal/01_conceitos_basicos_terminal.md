## 01 — Conceitos básicos do terminal

Este guia apresenta conceitos fundamentais do terminal para quem está começando, usando o terminal integrado do Visual Studio Code (VS Code). Priorizamos Windows (PowerShell) e mostramos equivalentes em macOS/Linux.

### O que é o terminal?

- Uma interface de linha de comando para executar instruções no computador.
- No Windows, usaremos o PowerShell. No macOS/Linux, usaremos o Terminal.

### Usando o terminal do VS Code

1) Abra a pasta do projeto no VS Code: File → Open Folder… e selecione `ExtracaoAnalise_FGVComunicacao`.
2) Abra o terminal integrado: View → Terminal (atalho: Ctrl + `).
3) Escolha o shell (se necessário) clicando na setinha ao lado do + no painel do terminal:
   - Windows: PowerShell (recomendado). Também pode usar Git Bash ou Command Prompt.
   - macOS/Linux: zsh ou bash.
4) O terminal abrirá na pasta do projeto. Se não, navegue com `cd` até a raiz do projeto.

### Prompt e diretórios

- O terminal mostra um "prompt" indicando onde você está (diretório atual) e pronto para receber comandos.
- Diretório atual = pasta onde os comandos serão executados.

### Comandos básicos (Windows PowerShell vs macOS/Linux)

- Caminho atual:
  - Windows: `pwd`
  - macOS/Linux: `pwd`
- Listar arquivos:
  - Windows: `ls`
  - macOS/Linux: `ls -la` (para ver detalhes e ocultos)
- Mudar de pasta:
  - Windows e macOS/Linux: `cd <caminho>`
- Criar pasta:
  - Windows e macOS/Linux: `mkdir nome_da_pasta`
- Remover arquivo:
  - Windows: `Remove-Item arquivo.txt`
  - macOS/Linux: `rm arquivo.txt`
- Remover pasta (recursivo):
  - Windows: `Remove-Item -Recurse -Force nome_da_pasta`
  - macOS/Linux: `rm -rf nome_da_pasta`

### Dicas de navegação

- `cd ..` volta uma pasta.
- Use Tab para autocompletar caminhos e nomes de arquivos.
- Em caminhos com espaços, use aspas: `cd "C:\\Meus Arquivos"` (Windows) ou `cd "/Users/voce/Meus Arquivos"` (macOS).

No VS Code, você pode abrir múltiplos terminais (ícone +) e renomeá-los (menu do terminal → Rename) para organizar tarefas.

### Variáveis de ambiente (noções)

- São valores que programas leem do sistema (ex.: `PATH`).
- Em nível iniciante, foque em usar `python`, `pip` e ativação do `venv` conforme explicado nas próximas lições.


