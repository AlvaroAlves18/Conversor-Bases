resp = "sim"
while resp == 'sim':
  peso = float(input('Digite seu peso (em Kg): '))
  altura = float(input('Digite sua alturo (em metros): '))
  imc = peso / altura**2
  print('Seu IMC é ', imc, 'Kg/m²')
  
  if imc <= 16:
	   print("Magreza grave")
  elif imc <= 17:
	   print("Magreza moderada")
  elif imc <= 18.5:
	   print("Magreza leve")
  elif imc <= 25:
	   print("Saudável")
  elif imc <= 30:
	   print("Sobrepeso")
  elif imc <= 35:
	   print("Obesidade Grau I")
  elif imc <= 40:
	   print("Obesidade Grau II (severa)")
  elif imc <= 50:
	   print("Obesidade Grau III (mórbida)")
 
  resp = input('Deseja continuar (sim ou não)? ')
else:
 print('Até logo')