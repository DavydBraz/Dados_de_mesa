import random

#funçao para jogar varios dados de um mesmo dado
def Jogar_varios_Dados():
  try:
    opcao=int(input("\nDigite quantos dados dejesa jogar: "))
    escolha=input("\nQual dos dados deseja jogar d4, d6, d8, d20, d100: ")
    sum=0
    dado=0
  
    if escolha=="d4":
      for i in range(opcao):
        dado=int(random.randint(1,4))
        sum+=dado
    elif escolha=="d6":
      for i in range(opcao):
        dado=int(random.randint(1,6))
        sum+=dado
    elif escolha=="d8":
      for i in range(opcao):
        dado=int(random.randint(1,8))
        sum+=dado
    elif escolha=="d20":
      for i in range(opcao):
        dado=int(random.randint(1,20))
        sum+=dado
    elif escolha=="d100":
      for i in range(opcao):
        dado=int(random.randint(1,100))
        sum+=dado
    else:
      print("\nFora das escolhas padrões")
    print("A soma dos dados jogados deu: ",sum)
  except:
    print("Erro, tente utilizar o programa mais tarde!")
    
  #funcao para decidir qual dos dados deve se jogar
def Jogar_Dado():
  try:
    escolha=input("\nQual dos dados deseja jogar d4, d6, d8, d20, d100: ")
    dado=0
    if escolha=="d4":
      dado=int(random.randint(1,4))
    elif escolha=="d6":
      dado=int(random.randint(1,6))
    elif escolha=="d8":
      dado=int(random.randint(1,8))
    elif escolha=="d20":
      dado=int(random.randint(1,20))
    elif escolha=="d100":
      dado=int(random.randint(1,100))
    else:
      print("\nFora das escolhas padrões")
    print(dado)
  except:
    print("Erro de execucao, tente utilizar o programa mais tarde!")
#laco infinito para continuar jogando os dados ate que se digite "n"=nao
while True:
  Jogar_varios_Dados()
  continuar=input("\nQuer utilizar novamente o programa (s/n): ")
  if continuar=="n":
    break
  elif continuar!="n" and continuar!="s":
    print("\nDigitou algo fora dos parametros, devido a isso o programa sera finalisado")
    break
print("\nEncerrado o programa, obrigado pela utilização!")
