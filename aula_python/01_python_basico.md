# Python Básico para Comunicação

## Como instalar e executar
- Recomendado: instalar o [Anaconda](https://www.anaconda.com/) ou `miniconda` e criar um ambiente.
- Alternativa: `pip` e `python3` do seu sistema.

```bash
# Verificar versão
python3 --version

# Instalar pacotes (ex.: pandas)
pip install pandas

# Executar um arquivo
python3 meu_script.py
```

## Variáveis e tipos
Python infere o tipo automaticamente quando você atribui um valor.

```python
idade = 21              # int (inteiro)
altura = 1.75           # float (decimal)
nome = "Maria"          # str (texto)
é_aluna = True          # bool (booleano)
notas = [8, 9, 7.5]     # list (lista)
aluna = {"nome": "Maria", "idade": 21}  # dict (dicionário)
coordenadas = (10, 20)  # tuple (tupla, imutável)
frutas = {"maçã", "banana"} # set (conjunto, sem repetição)
```

Dica: use `type(valor)` para ver o tipo.

```python
print(type(nome))  # <class 'str'>
```

- Imutáveis: `int`, `float`, `str`, `tuple`. Mutáveis: `list`, `dict`, `set`.
- Igualdade vs identidade: `==` compara valores; `is` compara se é o mesmo objeto em memória.
- Verdade/False (truthiness): valores vazios (`""`, `[]`, `{}`, `0`, `None`) contam como falso em condicionais.

## Operadores comuns
- Matemáticos: `+ - * / // % **`
- Comparação: `== != > < >= <=`
- Lógicos: `and or not`

```python
media = sum(notas) / len(notas)
print("Média:", media)
print(media >= 7 and é_aluna)
```

## Strings (textos)
```python
frase = f"{nome} tem {idade} anos"
print(frase.upper())      # MAIÚSCULAS
print(frase.lower())      # minúsculas
print(frase.split())      # lista de palavras
print("Maria" in frase)   # True
print(frase.replace("anos", "anos de idade"))
print(frase[:4])          # slicing
```

- f-strings: prefixo `f"...{expr}..."` avalia expressões dentro de chaves.
- Multilinha: use `"""texto\nmultilinha"""`.

## Listas e dicionários
```python
# Lista
canais = ["YouTube", "Instagram", "TikTok"]
canais.append("X")
for canal in canais:
    print(canal)

# Dicionário
perfil = {"nome": "João", "seguidores": 1200}
perfil["seguindo"] = 340
print(perfil.get("bio", "sem bio"))
```

- Cópias: `lista2 = lista1.copy()` (cópia rasa) vs `lista2 = lista1` (apenas outra referência).
- Comandos úteis: `len()`, `in`, `list.sort()`, `sorted(iterável, key=..., reverse=...)`.

## Unpacking e Slicing
```python
x, y = (10, 20)
primeiro, *meio, ultimo = [1, 2, 3, 4, 5]
texto = "comunicação"
print(texto[0:5], texto[-3:])
```

## Funções
Funções ajudam a reutilizar código e dar nomes às suas ideias.

```python
def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"  # retorna um texto

print(saudacao("Ana"))
```

Parâmetros com valores padrão:
```python
def calcular_desconto(preco: float, taxa: float = 0.1) -> float:
    return preco * (1 - taxa)

print(calcular_desconto(100))      # 90.0 (10%)
print(calcular_desconto(100, 0.2)) # 80.0 (20%)
```

- Args/kwargs: `def f(*args, **kwargs): ...` para aceitar número variável de argumentos.
- Anotações de tipo ajudam na leitura e em IDEs, mas não são obrigatórias em runtime.

## Lambda, map, filter, comprehensions
```python
quadrado = lambda n: n * n
print(list(map(quadrado, [1, 2, 3])))
print(list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4])))
pares = [n for n in range(10) if n % 2 == 0]
```

## Módulos e ambientes
```bash
python3 -m venv .venv
source .venv/bin/activate  # no Windows: .venv\\Scripts\\activate
pip install requests
python -c "import requests; print(requests.__version__)"
```

## Classes (orientação a objetos)
Use classes para representar "coisas" com dados e comportamento.

```python
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> str:
        return f"Sou {self.nome} e tenho {self.idade} anos."

p = Pessoa("Carla", 22)
print(p.apresentar())
```

- `__init__` inicializa o objeto; `self` referencia a própria instância.
- Métodos especiais: `__str__`, `__repr__`, `__len__`, etc.

## Entrada e saída
```python
nome = input("Qual é o seu nome? ")
print("Olá,", nome)

with open("anotações.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha!\n")
```

- Use `with` para fechar arquivos automaticamente.
- Leia CSVs com `csv` (padrão) ou `pandas`.

## Boas práticas rápidas
- Dê nomes claros às variáveis: `num_artigos`, `taxa_cliques`.
- Escreva funções curtas com uma responsabilidade.
- Comente o necessário, não o óbvio.
- Evite duplicação; extraia funções reutilizáveis.
- Trate erros previsíveis (entrada do usuário, IO, rede).

## Armadilhas comuns
- Comparar floats: use tolerância (`math.isclose`) ao invés de `==` puro.
- Mutabilidade: evitar usar listas mutáveis como argumento padrão (`def f(x=[]): ...`). Prefira `None` e crie dentro.
- Cópia rasa vs profunda: para estruturas aninhadas, use `copy.deepcopy`.

## Exercícios sugeridos
1. Escreva uma função que recebe uma lista de números e retorna a média.
2. Crie uma classe `Post` com `titulo`, `autor` e um método `resumo()`.
3. Leia um arquivo `.txt` e conte quantas linhas ele tem.
4. Escreva uma função que normaliza uma lista de números para o intervalo [0, 1].

## Referências
- Documentação oficial de Python (`https://docs.python.org/pt-br/3/`)
- PEP 8: guia de estilo (`https://peps.python.org/pep-0008/`)
