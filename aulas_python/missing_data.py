#Como tratar o problema de dados perdidos


import pandas as pd 
import numpy as np 


data = np.genfromtxt('../data/data2.txt', filling_values=np.nan)
print(data)


df = pd.DataFrame(data)
print(df)

#Removendo nan

df_nan = df.dropna()
print(df_nan)

#Para remover a linha que apenas todos elementos sao nan
df_nan = df.dropna(how='all')

#Para remover a coluna que apenas todos elementos sao nan
df_nan = df.dropna(how='all', axis=1)


#cria uma coluna nan
df['value4'] = np.nan
print(df)

#Substitui o nan
df['value4'] = df['value4'].fillna('150')
print(df)
