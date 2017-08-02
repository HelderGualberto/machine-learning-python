#Permite acesso direto a banco de dados
#Ja tem internamente diversos datasets linkados a biblioteca

import pandas as pd
import pydataset 

#Lista todos os datasets que o repositorio possui
print(pydataset.data())

#Tipo dos dados (DataFrame Pandas)
print(type(pydataset.data()))

#Retorna o dataset do titanic
titanic = pydataset.data('titanic')

print(titanic.describe())
print(titanic.head())
print(titanic.tail())


#Utilizando-se tecnicas para performance no Pandas
#Categorizar um atributo
print('Sem categoria')
print(titanic['class'].nbytes)

titanic['class'] = titanic['class'].astype('category')

print('Com categoria')
print(titanic['class'].nbytes)

