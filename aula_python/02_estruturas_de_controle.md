# Estruturas de Controle: if, for, while, try/except

As estruturas de controle definem o fluxo do seu programa: quando fazer algo, quantas vezes repetir, como tratar erros.

## Condicionais: if / elif / else
```python
numero = 15

if numero > 20:
    print("maior que 20")
elif numero == 20:
    print("igual a 20")
else:
    print("menor que 20")
```

Condição em uma linha (cuidado com legibilidade):
```python
status = "aprovado" if numero >= 10 else "reprovado"
```

- Curto-circuito: em `A and B`, se `A` for falso, `B` nem é avaliado; em `A or B`, se `A` for verdadeiro, `B` é ignorado.
- Walrus (`:=`): atribui e avalia ao mesmo tempo, útil para ler entrada/condição:
```python
while (linha := input().strip()) != "":
    print(linha.upper())
```

## Repetições: for
```python
plataformas = ["YouTube", "Instagram", "TikTok"]

for p in plataformas:
    print("Publicar em:", p)

for i in range(3):
    print("Tentativa", i)
```

Com `enumerate` e `zip`:
```python
for indice, p in enumerate(plataformas, start=1):
    print(indice, p)

views = [1200, 800, 600]
for canal, v in zip(plataformas, views):
    print(canal, v)
```

## Repetições: while
Use quando não souber o número de repetições de antemão.
```python
contador = 0
while contador < 3:
    print("Rodando...", contador)
    contador += 1
```

Pare ou pule iterações com `break` e `continue`:
```python
for n in range(10):
    if n == 5:
        break      # sai do loop
    if n % 2 == 0:
        continue   # pula números pares
    print(n)
```

## Blocos else em loops
O `else` após `for/while` executa somente se o loop NÃO foi interrompido por `break`.
```python
for n in range(3):
    if n == 10:
        break
else:
    print("Loop terminou sem break")
```

## Comprehensions (atalhos para criar listas/dicionários)
```python
# Lista de quadrados
quadrados = [n ** 2 for n in range(5)]  # [0, 1, 4, 9, 16]

# Filtrar apenas palavras com mais de 5 letras
palavras = ["comunicação", "arte", "mídia", "jornalismo"]
longas = [p for p in palavras if len(p) > 5]

# Dicionário: palavra -> tamanho
mapa = {p: len(p) for p in palavras}

# Generator (preguiçoso)
nums = (n*n for n in range(1_000_000))
```

## Tratamento de erros: try / except / else / finally
```python
try:
    x = int(input("Digite um número: "))
    print(10 / x)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
except ZeroDivisionError:
    print("Não dá para dividir por zero!")
else:
    print("Sem erros!")
finally:
    print("Fim do programa.")
```

Levantar exceções e criar suas próprias:
```python
class ErroDeNegocio(Exception):
    pass

def processar(valor: int) -> None:
    if valor < 0:
        raise ErroDeNegocio("Valor não pode ser negativo")
```

## Gerenciadores de contexto (with)
```python
from contextlib import suppress

with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("ok")

# Suprimir erro específico
with suppress(FileNotFoundError):
    open("nao_existe.txt").read()
```

## Dicas
- Prefira `for` quando souber o tamanho da sequência.
- Use `while` para repetir até uma condição mudar.
- Trate erros previsíveis para melhorar a experiência do usuário.
- Evite `except:` genérico; capture apenas o que espera.
- Simplifique condicionais complexas extraindo funções ou variáveis descritivas.