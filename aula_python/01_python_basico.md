# Python Básico para Comunicação

Bem-vinda(o)! Este material foi feito para quem está começando em programação e quer usar Python no dia a dia. O foco é em exemplos práticos e linguagem simples.

## Por que Python?
- **Fácil de aprender**: sintaxe simples e próxima do português/inglês.
- **Versátil**: análise de dados, web, automação, visualização, IA.
- **Comunidade enorme**: muita documentação e exemplos.

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
```

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

## Entrada e saída
```python
nome = input("Qual é o seu nome? ")
print("Olá,", nome)

with open("anotações.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha!\n")
```

## Boas práticas rápidas
- Dê nomes claros às variáveis: `num_artigos`, `taxa_cliques`.
- Escreva funções curtas com uma responsabilidade.
- Comente o necessário, não o óbvio.

## Exercícios sugeridos
1. Escreva uma função que recebe uma lista de números e retorna a média.
2. Crie uma classe `Post` com `titulo`, `autor` e um método `resumo()`.
3. Leia um arquivo `.txt` e conte quantas linhas ele tem.
