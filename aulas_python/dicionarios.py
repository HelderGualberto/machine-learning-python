#Dicionarios

#Inicializacao parecida com JSON

dc = {'chave0':123,'chave1':153,'chave2':12,'chave3':14}

print(dc)

#O acesso ao objeto e dado atraves da chave dentro de colchetes
print(dc['chave0'])


#Quando outros elementos sao inseridos com a mesma chave,
#o valor atual e substutuido, pois o hash e mutavel

dc['chave0'] = 978234
print(dc)

#A iteracao e feita com for tradicional

#Para recuperar as chaves do dicionario
print(dc.keys())

#Valores
print(dc.values())

