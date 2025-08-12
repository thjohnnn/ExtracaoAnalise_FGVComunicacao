## 02 — Navegação e manipulação de arquivos

Aprenda a navegar entre pastas e criar, mover, copiar e apagar arquivos pelo terminal do VS Code.

### Onde estou? (diretório atual)

```powershell
# Windows PowerShell (VS Code Terminal)
pwd
```

```bash
# macOS/Linux (VS Code Terminal)
pwd
```

### Listar arquivos

```powershell
# Windows PowerShell (VS Code Terminal)
ls
ls -Force   # inclui ocultos
```

```bash
# macOS/Linux (VS Code Terminal)
ls
ls -la      # inclui ocultos e detalhes
```

### Criar pastas e arquivos

```powershell
# Windows PowerShell (VS Code Terminal)
mkdir dados
New-Item -ItemType file notas.txt
```

```bash
# macOS/Linux (VS Code Terminal)
mkdir dados
touch notas.txt
```

### Copiar, mover e remover

```powershell
# Windows PowerShell (VS Code Terminal)
Copy-Item dados arquivo_copiado.txt
Move-Item notas.txt docs\notas.txt
Remove-Item arquivo_copiado.txt
Remove-Item -Recurse -Force dados
```

```bash
# macOS/Linux (VS Code Terminal)
cp -r dados arquivo_copiado.txt
mv notas.txt docs/notas.txt
rm arquivo_copiado.txt
rm -rf dados
```

### Caminhos absolutos vs relativos

- Absoluto: começa da raiz do sistema (ex.: `C:\Usuarios\Voce\Projetos` no Windows, `/Users/voce/Projetos` no macOS).
- Relativo: a partir da pasta atual (ex.: `../Projetos`, `./dados/arquivo.csv`).

### Dicas

- Aspas em caminhos com espaços: `cd "C:\\Meus Documentos"` (Windows) ou `cd "/Users/voce/Meus Documentos"` (macOS/Linux).
- Autocomplete com Tab.

No VS Code, use o Explorador (barra lateral) para ver o efeito dos comandos em tempo real e o botão de lixeira para apagar arquivos com segurança.


