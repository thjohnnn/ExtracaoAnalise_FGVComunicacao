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

## Repetições: for
```python
plataformas = ["YouTube", "Instagram", "TikTok"]

for p in plataformas:
    print("Publicar em:", p)

for i in range(3):
    print("Tentativa", i)
```

Com `enumerate` para ter posição e valor:
```python
for indice, p in enumerate(plataformas, start=1):
    print(indice, p)
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

## Comprehensions (atalhos para criar listas/dicionários)
```python
# Lista de quadrados
quadrados = [n ** 2 for n in range(5)]  # [0, 1, 4, 9, 16]

# Filtrar apenas palavras com mais de 5 letras
palavras = ["comunicação", "arte", "mídia", "jornalismo"]
longas = [p for p in palavras if len(p) > 5]

# Dicionário: palavra -> tamanho
mapa = {p: len(p) for p in palavras}
```

## Tratamento de erros: try / except / finally
```python
try:
    x = int(input("Digite um número: "))
    print(10 / x)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
except ZeroDivisionError:
    print("Não dá para dividir por zero!")
finally:
    print("Fim do programa.")
```

## Dicas
- Prefira `for` quando souber o tamanho da sequência.
- Use `while` para repetir até uma condição mudar.
- Trate erros previsíveis para melhorar a experiência do usuário.