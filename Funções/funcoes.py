# ----- Ex 1 -----
def somar(a, b):
  return a+b
print(somar(10,89))

# ----- Ex 2 -----
def multiplicar(a, b):
  return a*b
print(multiplicar(5,6))

# ----- Ex 3 -----
def mensagem(nome):
  return (f"Olá, {nome}!")
print(mensagem("Luiz"))

# ----- Ex 4 -----
def maior(a, b):
  if a>b:
    return a
  else:
    return b
print(maior(9,70))

# ----- Ex 5 -----
def dividir(a, b):
  q=int(a/b)
  r=(a%b)
  return (f"O quociente é: {q}, e o resto da divisão é: {r}")
print(dividir(5,2))

# ----- Ex 6 -----
def par_ou_impar(n):
  if n%2==0:
    return True
  else:
    return False
print(par_ou_impar(3))

# ----- Ex 7 -----
#Irá retornar "Olá" por conta da definição da função e no print(resultado) retornará None por não haver

# ----- Ex 8 -----
def apresentar(nome, idade, cidade):
  return (f"Seu nome é: {nome}, você tem {idade} anos e mora em: {cidade}")
print(apresentar("Luiz",18,"Curitiba"))

# ----- Ex 9 -----
def apresentar(nome, idade, cidade):
  return (f"Seu nome é: {nome}, você tem {idade} anos e mora em: {cidade}")
print(apresentar("Curitiba","Amanda",20))

print(apresentar(cidade="Porto Alegre", nome="Ana", idade=16))

# ----- Ex 10 -----
Se a ordem na função for nome, cidade e idade, irá funcionar normalmente, porém se a ordem for diferente os dados ficaram embaralhados (tal como idade=Curitiba)

# ----- Ex 11 -----
def saudacao(nome, periodo='dia'):
  return (f"Bom {periodo}, {nome}!")
print(saudacao("Luiz"))

# ----- Ex 12 -----
#No código dado já aceita os dois valores.

# ----- Ex 13 -----
#Resposta : Parâmetros obrigatórios não podem vir depois de parâmetros opcionais

# ----- Ex 14 -----
def somar_todos(*args):
  return sum(args)
print(somar_todos(1,2,3,4,5))

# ----- Ex 15 -----
def mostrar_dados(**dados):
  for chave, valor in dados.items():
    print(f"{chave}:{valor}")
mostrar_dados(Nome="Alice", Idade=22, Sexo="Feminino")

# ----- Ex 16 -----
#Resposta: args lida com uma lista de valores, enquanto o kwargs lida com um dicionário de nomes e valores.

# ----- Ex 17 -----
#Resposta: Em "teste()" retornará 5 já que dentro da função x é definido como 5 e logo após é exibido, e em print(x) será exibido 10.

# ----- Ex 18 -----
contador = 0
def incrementar():
  global contador
  contador+=1
incrementar()
print(contador)
incrementar()
print(contador)

# ----- Ex 19 -----
def triplo(x):
    return x * 3
mult_3=triplo
print(mult_3(5))

# ----- Ex 20 -----
def executar(funcao, valor):
  return funcao(valor)
print(executar(sum, [1,2,3,4]))

# ----- Ex 21 -----
quadrado=lambda x: x ** 2
print(quadrado(5))

# ----- Ex 22 -----
numeros=[1,2,3,4,5]
dobro=map(lambda x: x * 2, numeros)
print(list(dobro))

# ----- Ex 23 -----
numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares=filter(lambda x: x % 2 == 0, numeros)
print(list(pares))

# ----- Ex 24 -----
def fatorial(n):
  if n <= 1:
    return 1
  return n * fatorial(n - 1)
print(fatorial(5))

# ----- Ex 25 -----
lista=[]
def cont_rec(n):
  global lista
  lista.append(n)
  while n > 0 :
    lista.append(n-1)
    n-=1
  return list(lista) 
print(cont_rec(10)) 

# ----- Ex 26 -----
#Resposta: A função tenta chamar a si mesma infinitamente

# ----- Ex 27 -----
def media(lista):
    """
    Calcula a média aritmética de uma lista de números.

    Argumentos:
        lista: Uma sequência de números (int ou float).

    Retorna:
        float: O valor da média calculada.
        None: Se a lista estiver vazia, para evitar erro de divisão por zero.

    Exemplo:
        media([10, 0, 5])
        5.0
    """
    if not lista:
        return None
    
    return sum(lista) / len(lista)
print(media([1, 2, 4, 9]))

# ----- Ex 28 -----
help(media)

# ----- Ex 29 -----
def calculadora(a, b, operacao):
  if operacao == "+":
    return a+b
  elif operacao == "-":
    return a-b
  elif operacao == "*":
    return a*b
  elif operacao == "/":
    if b==0:
      return "ERRO! Divisão por zero"
    else:
      return a/b
  else:
    return "ERRO! Insira valores aceitáveis. Use: '+', '-', '*', '/'."
print(calculadora(5, 5, "+"))