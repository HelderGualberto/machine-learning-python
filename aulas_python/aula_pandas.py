#Biblioteca pandas é utilizada para criação de listas tabuladas
#Otimiza o processamento em matrizes N dimensionais
#Utiliza o NumPy

import pandas as pd

#Cria um array unidimensional
a = pd.Series([0,1,2,3,4,5,6,7,8,9])
print(a)

#Lista algumas informações como media, mediana, desvio padrao, max, min,etc
a.describe()

#Retorna true se ha elementos repretidos (Treu e false para cada indice)
a.duplicated()

a2 = a[:]



#No Pandas a indexacao padrao e um hash numerico por padrao
#Portanto podem existir indices iguais

#Funcao de append padrao. Os indices tamben entram no append, entao ele repete
a.append(a2)

#Cria matrizes N dimensionais
#Recebe listas de listas
#Neste exemplo tem indexacao normal
fd = pd.DataFrame(
	[['kurento',2345],['github',5346],['pandas',10234]],
	
	)

print(fd.ix[0])

#neste caso nao ha indexacao e sim hash devido a nomenclatua das colunas
fd = pd.DataFrame(
	[['kurento',2345],['github',5346],['pandas',10234]],
	columns=['repository','stars']
	)
print(fd['stars'])


#Funcoes sobre os indices
print(fd['stars'].mean())

print(fd['stars'].median())

#retorna apenas a linha especificada como um hash
#retorna ate i-1
print(fd.iloc[0]['stars'])

#Para acessar um indice diretamente
#retorna ate 'i'
print(fd.ix[0:1])

#ler aquivos com pandas

arq_csv = pd.read_csv('../data/data3.csv')

#Para utilizar a leitura sao necessarias duas bibliotecas extras
#xlrd para leitura e xlwt para escrita
arq_xls = pd.read_excel('../data/data4.xls')

print("ARQUIVO CSV")
print(arq_csv)

print("ARQUIVO XLS")
print(arq_xls)

#Filtros e selecao no Pandas

copacabana = pd.read_csv('../data/copacabana.csv', delimiter=';')

print(copacabana)

print(copacabana['Quartos'].describe())

#Aplicando filtros no Pandas

#Retornar o objeto que possui 6 quartos
quartos_6 = copacabana.loc[copacabana['Quartos'] == 6]

print(quartos_6)


#Operacoes diretas entre tabelas
#faz o produto escalar dos campos discriminados
print(copacabana['AreaConstruida'] * copacabana['VAL_UNIT'])

#Cria um novo campo no csv copacabana
copacabana['TOTAL'] = copacabana['AreaConstruida'] * copacabana['VAL_UNIT']

print(copacabana)