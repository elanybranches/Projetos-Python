#Métodos para utilização de lista.

#Inserindo elementos  - OBJETO.APPEND(ELEMENTO) 
#append() adiciona ao final da lista o elemento desejado. O append() adiciona elemento por elemento, e quando é utilizado para inserção
# de lista de elementos, ele o insere como um único elemento.

lista = [1,5,2,90,4,2,5]
lista.append(45)

#Inserindo elementos - OBJETO.INSERT(LOCAL, ELEMENTO)
#Insere o elemento em um local específico da lista

lista.insert(2, 25) ## Inserir o elemento 25 no índice 2 da lista.

#REMOVENDO ELEMENTOS - OBJETO.POP(LOCAL) 
#Remove e devolve um elemento de um índice. 

lista.pop(2)

#REMOVENDO ELEMENTOS -  OBJETO.REMOVE(ELEMENTO)
#Elementos que podem ser removidos pelo valor, localiza o primeiro valor desse tipo e remove-o da lista.

lista.remove(90)


#Para verificar se um determinado valor contém em uma lista...

'220' in lista
'550' not in lista

#Concatenar listas

#EXTEND()
#Permite a adição de uma lista de elementos a outra lista.

lista.extend([1,2,5,6])
