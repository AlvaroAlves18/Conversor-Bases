#Primeiro o usuario entra com um numero, em seguida com a a opção desejada
num = int(input('Digite um número inteiro: '))
opção = 0
while opção != 5:
  print( '''opções:
      [1] Base Binária
      [2] Base Octal
      [3] Base Hexadecimal
      [4] Digite um novo valor
      [5] Finalizar Conversões''')
  opção = int(input('selecione uma das opções: '))
  
  #agora vamos para as condições de cada opção
  #para a opção 1) Base Binária
  if opção == 1:
   print('{} Convertido para base Binária é igual a: {}' .format(num, bin(num)[2:]))
  #.format indica uma conversão a ser realizada
  #bin significa binário em python
  
  #Para a aopção 2) Base Octal
  elif opção == 2:
   print('{} Convertido para base Octal é igual a: {}'. format(num, oct(num)[2:]))
    #oct significa octal em python
    
    #Para a opção 3) Hexadecimal
  elif opção == 3:
   print('{} Convertido para base Hexadecimal é igual a: {}'.format(num, hex(num)[2:]))
    #O [2:], indica que  o resultado deve-se começar a partir da terceira casa pra frente.
  #hex significa Hexadecimal em python

    # Para a opção 4) Digite um novo valor 
  elif opção == 4:
   num = int(input("Digite um novo número inteiro que deseja converter: "))

    #Para a opção 5) Encerrar as conversões
  elif opção == 5:
   print('Finalizando as conversões! ')
  
  else:
   print("Opção inválida, digite novamente: ")
 
  print('*' * 60)   
print('Obrigado por ultilizar nosso sistema de conversão de bases numéricas; Volte Sempre!')
