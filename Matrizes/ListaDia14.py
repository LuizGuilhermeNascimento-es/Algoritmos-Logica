# ----- Ex 1 -----
import numpy as np
manha=np.random.randint(1,10,(3,3))
tarde=np.random.randint(1,10,(3,3))
print("A quantia de chuva no período da manhã foi de:","\n",manha,"\n","E no período da tarde foi de:","\n",tarde)
matriz_total=manha+tarde
print("A quantia de chuva total em cada cidade nos determinados dias foi de:","\n",matriz_total)

# ----- Ex 2 -----
import numpy as np
estoque_inicial=np.array([[32,43,28],
                        [56,78,101],
                        [32,45,60]
])
vendidos=np.array([[21,19,5],
                  [52,34,86],
                  [27,33,18]
])
estoque_final=estoque_inicial-vendidos
print("O estoque inicial foi de:\n",estoque_inicial,"\nA quantia de produtos vendidos foi de\n",vendidos,"\nE o estoque final foi de:\n",estoque_final)

# ----- Ex 3 -----
import numpy as np
ingredientes=np.random.randint(1,8,(2,3))
pedidos=np.random.randint(1,20,(3,2))
total=np.dot(ingredientes,pedidos)
print("O total de ingredientes utilizados para cada um dos lanches é de:\n",total)

# ----- Ex 4 -----
import numpy as np
salarios=np.random.randint(1512, 3000,(3,3))
novo_salario=(salarios*1.1)
print("O salário antigo dos funcionários era:","\n",salarios)
print("Os salários após o aumento é de:","\n",novo_salario)

# ----- Ex 5 -----
import numpy as np
matriz=np.random.randint(1,5,(3,3))
print("Matriz inicial:\n",matriz)
matriz=matriz*0
print("Matriz final\n",matriz)

# ----- Ex 6 -----
import numpy as np
matriz=np.random.rand(4,4)
i=0
while i<matriz.shape[0]:
  matriz[i]=1
  i+=1
print(matriz)

# ----- Ex 7 -----
import numpy as np
matriz=np.random.randint(1,99,(5,5))
print("A matriz inicial era:\n",matriz)
matriz[0][1]=88
matriz[2][4]=99
print("Após a alteração a matriz é:","\n",matriz)