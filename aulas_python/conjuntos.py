#Conjuntos sao estruturas de agrupamento
#Nao existem elementos repetidos em conjuntos
#Eles nao sao ordenados
#Conjuntos nao permitem fatiamento nem indexacao
#Conjuntos tambem sao heterogeneos

conjunto = set()

conjunto.add(10)
conjunto.add(20)
conjunto.add(30)
conjunto.add(10)

print(conjunto)

#Nota-se que ele nao acrescenta o elemento 10 novamente

#Outra forma de se inicializar conjunto e utilizando-se {}
c2 = {1,20,3}

#Operacoes com conjuntos

#uniao
uniao = c2.union(conjunto)
print(uniao)

#interseccao
inter = c2.intersection(conjunto)
print(inter)

#diferenca
diff = c2.difference(conjunto)
print(diff)

#Podemos fazer transformar listas em conjuntos. 
#A vantagem e a eliminacao de repeticoes

s = [1,2,2,2,3,4,5,5,5,6,6,6]
_set = set(s)
print(_set)

