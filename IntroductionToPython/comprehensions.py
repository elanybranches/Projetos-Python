#LIST, SET E DICT COMPREHENSIONS
##Permitem a composição de uma nova lista de modo conciso, filtrando elementos de uma coleção, transformando os elemetos ao passar o filtro.


#SINTAXE 
#LIST COMPREHENSIONS
# [expr for val in collection if condition]

#O equivalente a essa sintaxe, seria:

# result = []
# for val in collection:
#     if condition:
#         result.append(expr)

#Dado uma lista de strings, filtra-se, eliminando aqueles de tamanho 2 ou menores e convertendo para maiusculas as strings selecionadas.

strings = ['a','bab','cas','b','hu','jau','ki','lowo',jut','htre']

s_filter = [x.upper() for x in strings if len(x)>2]

#Outro exemplo - Obtendo como saida o dobro do valor

valores = [2,6,8,9,10]
valores_saida = [x*x for in valores]  

#Outro exemplo - Separar os valores em uma lista em pares e ímpares

val = [5,1,2,15,12,10,4,6,9,51,2,32]
par = [x for x in val if x%2==0]
impar = [x for x in val if x%2!=0]


#DICT COMPREHENSIONS

#SINTAXE

#dict_comp = {expr-chave:expr-valor for value in collection if condition}


#SET COMPREHENSIONS

#SINTAXE

#set_comp = {expr for value in collection if condition}

#De acordo com a variável strings e quissémos apenas os valores dos tamanhos das strings.
#Lembrando que Set é uma coleção de elementos únicos- set()

unique_lengths = {len(x) for x in strings}
