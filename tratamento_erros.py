#TRATAMENTO DE ERROS 

#EXEMPLO

list =[]
for value in range(5):
    list.append(int(input('Número:')))
    
#O código acima cria uma lista vazia chamada list em que é adicionado  5 entradas que são convertidas em int. Mas caso a pessoa digitasse 
#um valor diferente de números, não haveria um tratamento elegante.

for value in range(5):
  while 1:
      try:
          list.append(int(input('Digite um número:')
          break
      except:
          print('Somente números!')
          
          
