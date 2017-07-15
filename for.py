#Aqui vamos mostrar algumas utilizações da função for

lista = [0,1,2,3,4,5,6,7,8,9]


#Para cada indice da lista 'i' irá representar o seu valor
#Começando do indice 0 e indo até (len -1)
for i in lista:
	print(i)
print('\n')

#Neste caso tem-se o equivalente ao for(int i=0;i<10;i++) em C
#Ele irá contar dentro do range
for i in range(10):
	print(i, end=' ')
print('\n')
#para um range limitado podemos utilizar
for i in range(5, 10):
	print(i, end=' ')
print('\n')
#Podemos alterar o incremento
for i in range(2, 11, 2):
	print(i, end=' ')
print('\n')
#de maneira geral a função range é determinada por
#range (inicio, fim, incremento)
#Lembrando que ele vai até (fim-1)


