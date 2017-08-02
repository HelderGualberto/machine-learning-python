
#Acesso indexado de strings

# string = "Helder" ou 'Helder' -> aspas simples e duplas tem a mesma função para strings
# string[0] -> Acessa o primeiro elemento da string
# string[-1] -> Acessa o último elemento da string

#Acesso aos métodos de Objetos string

# help(string) -> mostra uma lista de métodos disponíveis para o objeto do tipo string

# len(string) -> retorna o tamanho da string
# Outra forma de acessar os métodos dos objetos é através
# de algo conhecido cmo "Dunder" (souble underscore)
# que pode ser acessado atraves do operador '.'
# string.__len__() -> retorna o tamanho da string

#Em strings é possível fazer slice através de operações por indexação
# Por exemplo:
# a = string[0:3] -> irá retornar uma parte da string
# string[0:3] se lê -> começando de zero, retorne o conteúdo
#						das três próximas posições

#string[-3:] -> começa do indice (len -3) e retorna tudo até o final da string

#Basicamente o operador ':' indica a sua esquerda a posição de inicio
#e a direita a quantidade de iterações
# inicio:iterações

#A concatenação de strings é feita através do operador soma '+'
#print("Helder " + "Rodrigues")
#Helder Rodrigues

#A operação de repetição de strings pode ser feita pelo operador '*'
#print(3 * "A")
#AAA
#Não é possível multiplicar strings por valores não inteiros

#Para representar int em strings basta acrescentar %
#idade = 22
#print("Helder tem %d anos" %idade )
#Para ter mais de uma entrada
#namorada = "andressa"
#print("Helder tem %d e sua namorada é %s" % (idade, namorada))


#Imutabilidade de strings
#Quando iniciamos uma string e depois utilizamos o mesmo nome para outra coisa
#nome = "helder"
#nome = "Andressa"
#A variável nome não foi alterada, e sim uma nova variável foi criada
#O objeto nome anterior já não existe mais
