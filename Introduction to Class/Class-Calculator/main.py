from classes import Calculadora

#inicia calculadora com um valor no registrador
c = Calculadora()
print(Calculadora.DESCRIPTION)

while True:
  print('='*20)
  print("\t",c.getRegistrador())
  print('='*20)
  print('''
  [1] - Somar
  [2] - Subtrair
  [3] - Dividir
  [4] - Multiplicar
  [5] - Reset
  [6] - Undo
  ''')
  opcao = int(input("Digite a Opção:"))
  if(opcao == 1):
    valor = float(input("+: "))
    c.somar(valor)
  elif(opcao == 2):
    valor = float(input("- :"))
    c.subtrair(valor)
  elif(opcao == 3):
    valor = float(input("/ :"))
    c.dividir(valor)
  elif(opcao == 4):
    valor = float(input("* :"))
    c.multiplicar(valor)
  elif(opcao == 5):
    c.reset()
  elif(opcao == 6):
    c.undo()
  else:
    print("Operação Invalida!")