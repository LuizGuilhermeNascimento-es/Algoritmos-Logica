# ----- Ex 1 -----
a=[1,2,3,4,5]
print(a)

# ----- Ex 2 -----
cores = ['vermelho', 'azul', 'verde', 'amarelo']
print(cores[1])

# ----- Ex 3 -----
numeros = [1, 2, 3]
numeros.append(10)
print(numeros)

# ----- Ex 4 -----
frutas = ['maçã', 'banana', 'laranja']
del frutas[1]
print(frutas)

# ----- Ex 5 -----
itens = [10, 20, 30, 40, 50]
tamanho=len(itens)
print("O tamanho da lista itens é de:",tamanho)

# ----- Ex 6 -----
valores = [1, 3, 5, 7, 9]
if 7 in valores:
  print(1)
else:
  print(0)

# ----- Ex 7 -----
lista1=[1,2]
lista2=[3,4]
lista3=lista1+lista2
print(lista3)

# ----- Ex 8 -----
letras=["a","b","c","d"]
i=0
x=int(len(letras)-1)
while i<=x:
  letras[i],letras[x]=letras[x],letras[i]
  i+=1
  x-=1
print(letras)

# ----- Ex 9 -----
numeros=[1, 2, 2, 3, 2, 4]
n2=numeros.count(2)
print("A quantia de números 2 nessa lista é de:",n2)

# ----- Ex 10 -----
precos = [10.5, 20.0, 15.5]
total=sum(precos)
print("A soma de todos os valores é:",total)

# ----- Ex 11 -----
listanum=[1,1,1,2,2,3,4,4,5,5,5,5]
listaF=list(dict.fromkeys(listanum))
print(listaF)

# ----- Ex 12 -----
lista=[12,12,55,34,62,98,75,4]
i=0; maior=0; menor=lista[0]
while i<len(lista):
  if lista[i]>maior:
    maior=lista[i]
  elif lista[i]<=menor:
    menor=lista[i]
  i+=1
print("O maior valor da lista é:",maior,"e o menor é:",menor)

# ----- Ex 13 -----
valores=[i**2 for i in range(1,11)]
print(valores)

# ----- Ex 14 -----
lista_og=[1,2,3,4,5,6,7,8,9,10,21,22,23]
impares=[i for i in lista_og if i%2 !=0]
print(impares)

# ----- Ex 15 -----
original=[1, 2, 3, 4, 5]
n=int(input("Insira quantas rotações deseja fazer"))
for i in range(n):
  ultimo=original.pop()
  original.insert(0,ultimo)
print(original)

# ----- Ex 16 -----
lista1=[1, 2, 3, 4, 5]
lista2=[1, 3, 5, 7, 9]
intersecao=[item for item in lista1 if item in lista2]
print(intersecao)

# ----- Ex 17 -----
num=[[1,2],[3,4],[5,6],[7,8]]
achatada=[item for lista in num for item in lista]
print(achatada)

# ----- Ex 18 -----
numeros=[5,6,2,9,7,8,0,1,3,4]
numeros.sort()
print(numeros)

# ----- Ex 19 -----
def kadane(nums):
    if not nums:
        return 0
    soma_atual=soma_maxima=nums[0]
    for i in range(1, len(nums)):
        soma_atual=max(nums[i], soma_atual + nums[i])
        soma_maxima=max(soma_maxima, soma_atual)
    return soma_maxima
numeros=[-5,4,-1,3,-2,-2,5]
print(kadane(numeros))

# ----- Ex 20 -----
def permutar(lista):
    if len(lista) <= 1:
      return [lista]
    resultado=[]
    for i in range(len(lista)):
      fixo=lista[i]
      restante=lista[:i]+lista[i+1:]
      for p in permutar(restante):
        resultado.append([fixo]+p)        
    return resultado
numeros=[1, 2, 3, 4]
print(permutar(numeros))

# ----- TESTE DE COMMIT -----
numeros=[-9,15,34,-29,-4,5,7]
#organizar do menor para o maior todos negativos
negativos=[n for n in numeros if n<=0]
negativos.sort()
print(negativos)