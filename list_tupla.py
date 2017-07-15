#Listas são objetos heterogêneos em python, ou seja
#podem ter objetos de diferetnes tipos dentro de uma mesma lista

lista = [] #Inicializa uma lista vazia

lista = [1, 1.3, "Helder", ["Nome1","Nome2","nome3"]]

#listas são objetos mutáveis, ou seja, é possível modificar o
#objeto dentro de uma lista

#O acesso indexado da lista segue o padrão da linguagem C

print(lista[-1][0]) #Imprime o primeiro elemento da sublista

print(lista[-1][-1]) #Imprime o ultimo elemento da sublista


#As listas em python tembém são objetos
#Quando atribui-se uma lista a outra vaiável tem-se o mesmo
#comportamento da linguagem C, onde a lista é como um ponteiro

lista1 = [1,2,3,4,5]
lista2 = lista1 #Copia apenas a referência para a lista, não os dados literais

lista2[0] = 10

print(lista1) 
# [10,2,3,4,5]

#Por ser um ponteiro para lista1, a lista2 irá alterar
#o conteúdo da lista1, como ponteiros em C

#Para copiar o conteúdo da lista basta utilizar a seguinte notação
lista1 = [1,2,3,4,5]
lista2 = lista1[:]

lista2[0] = 10
print (lista1)
print (lista2)

#Outros operadores em lista são:

lista1.append("Helder") #Insere um novo elemento na lista
print(lista1)

concat = lista1 + lista2 #Concatena as listas
print(concat)

lista1.pop(0) #Remove o objeto por indexação
print(lista1)

lista1.remove("Helder") #Remove o objeto especificado
print(lista1)


#Tuplas são objetos imutáveis
#Tem propriedade homogênia como as listas

tupla = (1,2,3)
print(tupla)

#O acesso aos elementos é feita  da mesma forma que as listas
print(tupla[0])

#funções da tupla
tupla = (1,2,2,2,3,'Helder','Carro')
print(tupla.count(2)) #imprime quantas vezes o 2 aparece
print(tupla.index('Helder')) #imprime o indice do valor "Helder"
