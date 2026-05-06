# ----- Ex 1 -----
import numpy as np
matriz=np.random.randint(0,10,(3,3))
print(matriz)
print(np.sum(matriz))

# ----- Ex 2 -----
import numpy as np
n=int(input("Digite o tamanho que deseja da sua matriz identidade: "))
matriz=np.eye(n)
print(matriz)

# ----- Ex 3 -----
import numpy as np
matriz_primos=np.array([[2,3,5,7],
                 [11,13,17,19],
                 [23,29,31,37],
                 [41,43,47,53]
])
p=int(input("Insira o numero que deseja buscar na Matriz: "))
if p in matriz_primos:
  print(f"{p} está na lista!")
else:
  print(f"{p} não está na lista!")

# ----- Ex 4 -----
import numpy as np
matriz=np.array([[0,1],
                 [2,3]
])
matriz_invertida = matriz[[1, 0], :]
print(matriz_invertida)
# ----- Para tamanho qualquer de matriz: -----
import numpy as np
matriz=np.array([[0,1, 2],
                 [3,4,5],
                 [6,7,8]
])
inv=[]; i=matriz.shape[0]-1
while i>=0:
  inv.append(i)
  i-=1
matriz_invertida = matriz[[inv], :]
print(matriz_invertida)

# ----- Ex 5 -----
import numpy as np
matriz=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]
])
matriz=matriz*3
print(matriz)

# ----- Ex 6 -----
import numpy as np
matriz=np.array([[0,1,2,3],
                 [4,5,6,7],
                 [8,9,10,11]
])
a=matriz.flatten()
pares=a[a % 2 == 0]
print(pares)

# ----- Ex 7 -----
import numpy as np
matriz=np.random.randint(1,99,(3,3))
print(matriz)
print("O maior valor da matriz é: ", np.max(matriz))

# ----- Ex 8 -----
import numpy as np 
matriz=np.random.randint(1,10,(3,3))
print(matriz)
media1=float(matriz[0].sum()/3)
media2=float(matriz[1].sum()/3)
media3=float(matriz[2].sum()/3)
print(f"A média da primeira linha é: {media1}, da segunda é: {media2}, e da terceira linha é: {media3}")

# ----- Ex 9 -----
import numpy as np 
matriz=np.random.randint(1,10,(4,4))
print(matriz)
diagonal=np.eye(4,4)
soma=np.sum(matriz*diagonal)
print("A soma dos valores da diagonal é: ",soma)

# ----- Ex 10 -----
import numpy as np
m=np.random.randint(1,9,(3,2))
n=np.transpose(m)
print("Matriz original:\n",m)
print("Matriz transposta:\n",n)

# ----- Ex 11 -----
import numpy as np
matriz=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]
])
i=0
soma=[]
while i < matriz.shape[0]:
  soma.append(int(sum(matriz[i])))
  i+=1
print(soma)

# ----- Ex 12 -----
import numpy as np
m=np.array([[1,2,3],
            [2,4,5],
            [3,5,6]
])
print("Matriz original:\n",m); print("Matriz transposta:\n",np.transpose(m))
def simetria(matriz):
  if matriz.shape[0] != matriz.shape[1]:
    return False
  return np.allclose(matriz, np.transpose(matriz))

if simetria(m) == False:
  print("A matriz não é simétrica")
else:
  print("A matriz é simétrica")

# ----- Ex 13 -----
import numpy as np
matriz_ds=np.flip(np.eye(5), axis=1)
matriz=np.random.randint(1,9,(5,5))
diagonal_s=(matriz*matriz_ds)
print(diagonal_s)

# ----- Ex 14 -----
import numpy as np
def multmat(matrizA, matrizB):
  if matrizA.shape[1] != matrizB.shape[0]:
    return "Dimensões Incompatíveis!"
  return np.dot(matrizA, matrizB)

matA=np.random.randint(1,5,(3,3))
matB=np.random.randint(1,5,(3,3))

print(multmat(matA,matB))

# ----- Ex 15 -----
def rotacionar_90_horario(matriz):
    n=len(matriz)
    transposta=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        transposta[j][i] = matriz[i][j]
    for i in range(n):
        transposta[i].reverse()       
    return transposta
    
matriz_original=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
resultado=rotacionar_90_horario(matriz_original)

print("Matriz Rotacionada:")
for linha in resultado:
    print(linha)