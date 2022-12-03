import random

#funcao para decidir qual dos dados deve se jogar
def Jogar_Dados():
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

#laco infinito para continuar jogando os dados ate que se digite "n"=nao
while True:
  Jogar_Dados()
  continuar=input("\nQuer utilizar novamente o programa (s/n): ")
  if continuar=="n":
    break
  elif continuar!="n" and continuar!="s":
    print("\nDigitou algo fora dos parametros, devido a isso o programa sera finalisado")
    break
print("\nEncerrado o programa, obrigado pela utilização!")
