import random

#funcao menu base
def Menu():
  print("\n-------------------------------------------------------")
  print("\n Escolha uma das opcoes abaixo:\n")
  print("1-Jogar um unico dado\n")
  print("2-Jogar varios dados\n")
  print("3-Sair\n")
  print("-------------------------------------------------------\n")
  escolha=int(input("\nDigite qual das opcoes acima deseja escolher: "))
  return escolha
  
#funçao para jogar varios dados de um mesmo dado
def Jogar_varios_Dados():
  try:
    escolha=input("\nQual dos dados deseja jogar d4, d6, d8, d20, d100: ")
    opcao=int(input("\nDigite quantos dados dejesa jogar: "))
    sum=0
    dado=0
  
    if escolha=="d4":
      for i in range(opcao):
        dado=int(random.randint(1,4))
        print("O dado {} foi igual a: \'{}\'.". format(i+1,dado))
        sum+=dado
        
    elif escolha=="d6":
      for i in range(opcao):
        dado=int(random.randint(1,6))
        print("O dado {} foi igual a: \'{}\'.". format(i+1,dado))
        sum+=dado
        
    elif escolha=="d8":
      for i in range(opcao):
        dado=int(random.randint(1,8))
        print("O dado {} foi igual a: \'{}\'.". format(i+1,dado))
        sum+=dado
        
    elif escolha=="d20":
      for i in range(opcao):
        dado=int(random.randint(1,20))
        print("O dado {} foi igual a: \'{}\'.". format(i+1,dado))
        sum+=dado
        
    elif escolha=="d100":
      for i in range(opcao):
        dado=int(random.randint(1,100))
        print("O dado {} foi igual a: \'{}\'.". format(i+1,dado))
        sum+=dado
        
    else:
      print("\nFora das escolhas padrões")
    print("\nA soma dos dados jogados deu: \"{}\"".format(sum))
  except:
    print("\nErro, tente utilizar o programa mais tarde.")
    
#funcao para decidir qual dos dados deve se jogar
def Jogar_Dado():
  try:
    escolha=input("\nQual dos dados deseja jogar d4, d6, d8, d20, d100: ")
    dado=0
    if escolha=="d4":
      dado=int(random.randint(1,4))
      print("\nResultado do dado foi de: \'{}\'". format(dado))
  
    elif escolha=="d6":
      dado=int(random.randint(1,6))
      print("\nResultado do dado foi de: \'{}\'". format(dado))

    elif escolha=="d8":
      dado=int(random.randint(1,8))
      print("\nResultado do dado foi de: \'{}\'". format(dado))

    elif escolha=="d20":
      dado=int(random.randint(1,20))
      print("\nResultado do dado foi de: \'{}\'". format(dado))

    elif escolha=="d100":
      dado=int(random.randint(1,100))
      print("\nResultado do dado foi de: \'{}\'". format(dado))

    else:
      print("\nFora das escolhas padrões!")
  except:
    print("\nErro de execucao, tente utilizar o programa mais tarde!")

    
#laco infinito para continuar jogando os dados ate que se digite "n"=nao

while True:
  try:
    escolha=Menu()
    if escolha==1:
      Jogar_Dado()
    elif escolha==2:
      Jogar_varios_Dados()
    elif escolha==3:
      print("\nObrigado por utilizar este sistema de dados :)")
      print("\n----------------------------------------------------")
      print("\nSistema finalisado!")
      break
    else:
      print("\nNao existe a opcao solicitada, digite uma das opcoes disponiveis")
  except:
    print("\nOcorreu algum erro no momento de selecao, tente novamente mais tarde.")
