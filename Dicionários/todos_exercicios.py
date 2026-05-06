# ===== Exercício 1 =====
dic={"nome":"Luiz",
     "idade":18,
     "cidade":"Curitiba"}
pesq=(input("Digite qual chave da pessoa você deseja acessar: "))
if pesq in dic:
  print("O valor correspondente dessa chave é:",dic[pesq])
else:
  print("Chave válida")

# ===== Exercício 2 =====
produtos={"Salgadinho":11.50,
         "Arroz":15,
         "Redbull":10}
print(produtos)
while True:
  alt=input("\nQue produto deseja alterar o valor? ")
  if alt in produtos:
    try:
      produtos[alt]=float(input("Insira o novo valor: R$"))
      break
    except ValueError:
      print("Insira apenas números!")
  else:
      print("Digite um produto que esteja dentro da lista de produtos")

print(produtos)

# ===== Exercício 3 =====
dic={}
nome=input("Digite um nome: ")
while True:
  try:
    idade=int(input("Digite a idade dessa pessoa: "))
    break
  except ValueError:
    print("Insira uma idade válida")
atlz={"Nome":nome,
      "Idade":idade}
dic.update(atlz)
print("\n",dic)

# ===== Exercício 4 =====
inf=dict()
i=0
for i in range(3):
  chave=input(f"Digite o nome da chave a ser adicionada. Chave número: {i+1}: ")
  valor=input(f"Insira o valor para a chave número: {i+1}: ")
  inf[chave]=valor
print(inf)

# ===== Exercício 5 =====
dic={"Nome":"Luiz",
     "Idade":18,
     "Sexo":"Masculino",
     "Altura(m)":1.8}
resp=input("Você deseja apagar todos os dados do dicionário? Digite sim ou não: ")
if resp=="sim":
  dic.clear()
  print("\nTodos os dados foram apagados com sucesso!",dic)
else:
  print("\nO dicionário não foi apagado!",dic)

# ===== Exercício 6 =====
dados=dict(Nome="Luiz",Idade=18, Estado_Civíl="Solteiro")
dados_atualizados=dados.copy()
print(dados)
dados_atualizados.update(Estado_Civíl="Casado")
print(dados_atualizados)

# ===== Exercício 7 =====
nome=input("Digite o nome das pessoas que deseja adicionar a essa lista separados por vírgula: ")
nomes=[item.strip() for item in nome.split(",")]
#nome.strip() serve para remover espaços extras; split(",") separa o input em strings a cada ","
dic_nomes=dict.fromkeys(nomes,0)
print(dic_nomes)

# ===== Exercício 8 =====
notas={"Luiz":10,
       "Amanda":9,
       "Pedro":7.2,
       "Samuel":0,
       "Gabriel":8.7,
       "Rafaela":5.5}
pesq=input("Digite o nome do aluno que deseja buscar a nota: ")
if pesq in notas:
  print("A nota do(a) aluno(a) foi de: ",notas.get(pesq))
else:
  print("Nome não encontrado na lista!")

# ===== Exercício 9 =====
produtos={"Sabão":9.5,
          "Shampoo":12,
          "Refri":8.99,
          "Arroz":22,
          "Energético":11}
print("As chaves dessa lista são: ",produtos.keys())
print("Os valores são: ",produtos.values())
print("Os itens são: ",produtos.items())

# ===== Exercício 10 =====
dic={"Rafael":24,
     "Amanda":17,
     "Luiz":18,
     "Alice":40,
     "Ana":15}
print(dic)
apagar=input("Digite a chave que deseja apagar: ")
dic1=dic.pop(apagar)
print("Você excluiu: ",dic1)
print("A nova lista é:\n",dic)
dic.popitem(), print("O último item foi removido!")
print(dic)
nova_chave=input("\nDigite o nome de uma nova informação: ")
novo_valor=input(f"Digite o valor para {nova_chave}: ")
dic.update({nova_chave:novo_valor})
print("A lista final é:\n",dic)

# ===== Exercício 11 =====
def exibir_menu():
    print("\n--- SISTEMA DE GESTÃO DE USUÁRIOS ---")
    print("1.  Exibir usuários (keys, values, items)")
    print("2.  Buscar usuário (get)")
    print("3.  Adicionar usuário")
    print("4.  Atualizar idade")
    print("5.  Remover usuário específico")
    print("6.  Remover último usuário inserido")
    print("7.  Testar cópia do dicionário")
    print("8.  Novo dicionário com idade padrão")
    print("9.  Mesclar novos dados")
    print("10. Limpar sistema")
    print("11. Criar dicionário de lista de tuplas")
    print("0.  Sair")
    return int(input("Escolha uma opção: "))

usuarios={"Rafael":24,
          "Amanda":17,
          "Luiz":18,
}

while True:
  opcao=exibir_menu()
  if opcao==1:
    print("Nomes :",usuarios.keys())
    print("Idades :",usuarios.values())
    print("Pares :",usuarios.items())
  
  elif opcao==2:
    busca=input("Digite o nome do usuário que deseja buscar: ")
    if usuarios.get(busca)==None:
      print("Usuário não encontrado no sistema")
    else:
      print(usuarios.get(busca))
  
  elif opcao==3:
    nome=input("Insira o nome do usuário: ")
    idade=int(input(f"Insira a idade do(a){nome}"))
    usuarios[nome]=idade
    print(f"Usuário {nome} adicionado(a) com sucesso.")

  elif opcao==4:
    nome=input("Nome do usuário a atualizar: ")
    if nome in usuarios:
      nova_idade=int(input("Nova idade: "))
      usuarios[nome]=nova_idade
      print("Idade atualizada.")
    else:
      print("Usuário não encontrado.")
  
  elif opcao==5:
    nome=input("Digite o nome do usuário a ser excluído: ")
    if nome in usuarios:
      usuarios.pop(nome)
    else:
      print("Usuário não encontrado")
    
  elif opcao==6:
    usuarios.popitem()
    print("O ultimo usuário foi removido do dicionário")
  
  elif opcao==7:
    copia_usuarios=usuarios.copy()
    print("Cópia criada.")
    if copia_usuarios:
      nome=list(copia_usuarios.keys())[0]
      nova_idade=int(input(f"Altere a idade de {nome} na CÓPIA: "))
      copia_usuarios[nome]=nova_idade
      print(f"\nOriginal: {usuarios}")
      print(f"Cópia:    {copia_usuarios}")
    else:
      print("Dicionário vazio para testar cópia.")
    
  elif opcao==8:
    nomes_str=input("Digite nomes separados por vírgula: ")
    lista_nomes=[n.strip() for n in nomes_str.split(',')]
    idade_padrao=int(input("Idade padrão para todos: "))
    novo_dic=dict.fromkeys(lista_nomes,idade_padrao)
    print(f"Novo dicionário criado:{novo_dic}")
  
  elif opcao==9:
    print("Crie um pequeno lote de atualização.")
    quant=int(input("Digite quantos novos usuários deseja adicionar ao dicionário: "))
    for i in range(quant):
      nome=input("Nome: ")
      idade=int(input("Idade: "))
      lote={nome: idade}
      usuarios.update(lote)
      quant+=1
    print("Dicionário principal atualizado.")
  
  elif opcao==10:
    confir=input("Tem certeza de que deseja apagar tudo?(s/n)")
    if confir.lower() == 's':
      usuarios.clear()
      print("Sistema limpo.")
    else:
      print("O sistema não foi apagado!")

  elif opcao == '11':
    print("Criação através de lista de tuplas")
    entrada=input("Digite no formato Nome:Idade, Nome:Idade: ")
    try:
      lista_tuplas=[(item.split(':')[0].strip(), int(item.split(':')[1])) 
    for item in entrada.split(',')]
      novo_dic_tupla=dict(lista_tuplas)
      print(f"Dicionário criado:{novo_dic_tupla}")
    except:
      print("Erro no formato. Use Nome:Idade.")
  elif opcao == 0:
    print("Encerrando programa...")
    break
  else:
    print("Opção inválida.")