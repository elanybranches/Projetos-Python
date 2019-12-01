## Exemplos de funções lambda
##Chamadas também de funções anônimas , são constituídas  de uma única instrução, cujo resultado é o valor d retorno.


## código de uma função comum
def quadrado(x):
  return x*2
  
  
 ##código utilizando lambda
 func_eq = lambda x: x*2
 
 
 ##Dado um dicionário que contém dados de usurário, tem-se o objetivo de filtrar apenas os usuários maiores de 27 anos.
 
 users = [
  {
    "id": 1, 
    "name": "Allan", 
    "age": 27, 
    "profile_picture": "http://…", 
    "city": "São Paulo"
  },
  {
    "id": 2, 
    "name": "Julie", 
    "age": 29, 
    "profile_picture": "http://…", 
    "city": "Curitiba"
  },
  {
    "id": 3, 
    "name": "Pedro", 
    "age": 31, 
    "profile_picture": "http://…", 
    "city": "Rio de Janeiro"
  }
]

def users_27(user):
  return user["age"]>27
  
filtered_users = filter(users_27, users)

##utilizando funções lambda 
_filtered_users = filter(lambda user: user["age"]>27, users)
