def func_speed():
 kmporlitros=int(input("O veículo faz quantos Km por Litro? "))
 conversor=kmporlitros*1000#Multiplicou o kmporlitro por mil já que era duas dezenas ex:12km
#vlcombustivel=float(input("Digite o valor do litro de combustível"))
 kmpercorrido=float(input("Digite km percorrido"))
 formula=1000/conversor
 totalml=formula*kmpercorrido
 print("gastou em Combustível %.2f"%totalml,"ml")
 try:
  vlcombustivel=float(input("Digite o valor do litro de combustível"))
  custo=vlcombustivel/1000#valor do combustivel dividido por mil ml
  preço=totalml*vlcombustivel
  print("O Custo da Viagem foi de ""R$%.2f"%preço,)
 except ValueError:
    print(" preço do combutível não aceita vírgula")

func_speed()    
    