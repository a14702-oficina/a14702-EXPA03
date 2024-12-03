"""

A escola necessita de um sistema para gerir o stock de materiais (como canetas, cadernos, borrachas, etc.). Atualmente, o registo é feito manualmente, o que dificulta a atualização e a consulta rápida. Pretende-se um programa que automatize este processo, utilizando funções.

O programa deve:
Registar novos materiais no stock.
Consultar o stock de um material específico.
AtuaLIzar a quantidade em stock (adição ou remoção).
Exibir o estado geral do stock.

O programa será composto pelas seguintes funções:
adicionar_material(): Para registar novos materiais.
consultar_stock(): Para verificar o stock de um material específico.
atualizar_stock(): Para adicionar ou remover itens do stock.
exibir_stock(): Para mostrar o estado geral do stock.
"""



def adicionar_material(stock):
  nome = input("Nome do material para consulta: ")
  if nome in stock:
      print("O material já existe no stock!")
  else:
      quantidade = int(input(f"Quantidade inicial de {nome}: "))
      stock[nome] = quantidade
      print(f"{nome} adicionado com sucesso!")
def consultar_stock(stock):
  nome = input("Nome do material para consulta: ")
  if nome in stock:
    print(f"Quantidade em stock de {nome}: {stock[nome]}")
  else:
    print("O material não existe no stock!")
def atualizar_stock(stock):
  nome = input("Nome do material a atualizar: ")
  if nome in stock:
      operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
      quantidade = int(input("Quantidade: "))
      if operacao == "A":
          stock[nome] += quantidade
          print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
      elif operacao == "R":
          if quantidade <= stock[nome]:
              stock[nome] -= quantidade
              print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
          else:
              print("Quantidade insuficiente em stock!")
      else:
          print("Operação inválida!")
  else:
    print(f"{nome} não encontrado no stock.")    
def exibir_stock(stock):
  print("Estado geral do stock:")
  for nome, quantidade in stock.items():
    print(f"{nome}: {quantidade}")
stock = {}
while True:
  print("1. Adicionar material")
  print("2. Consultar stock")
  print("3. Atualizar stock")
  print("4. Exibir stock")
  print("5. Sair")
  opcao = input("Escolha uma opção: ")
  if opcao == "1":
    adicionar_material(stock)
  elif opcao == "2":
    consultar_stock(stock)
  elif opcao == "3":
    atualizar_stock(stock)
  elif opcao == "4":
    exibir_stock(stock)
  elif opcao == "5":
    break
  else:
    print("Opção inválida!")



